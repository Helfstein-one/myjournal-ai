import os
import subprocess
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from myjournal.config import Config
from myjournal.calendar.mock_calendar import get_mock_calendar_events
from myjournal.calendar.ics_parser import ICSCalendarParser

SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]

class GoogleCalendarClient:
    def __init__(self, credentials_path: Optional[str] = None, token_path: Optional[str] = None):
        self.credentials_path = credentials_path or Config.GOOGLE_CREDENTIALS_PATH
        self.token_path = token_path or Config.GOOGLE_TOKEN_PATH

    @staticmethod
    def fetch_ics_events(url_or_path: str, default_category: str = "Pessoal") -> List[Dict[str, Any]]:
        """Lê e processa eventos de uma URL .ics ou arquivo local."""
        try:
            content = ""
            if url_or_path.startswith("http://") or url_or_path.startswith("https://"):
                import requests
                r = requests.get(url_or_path, timeout=12)
                if r.status_code == 200:
                    content = r.text
            elif os.path.exists(url_or_path):
                with open(url_or_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

            if content:
                events = ICSCalendarParser.parse_events(content)
                for ev in events:
                    if not ev.get("calendar_source"):
                        ev["calendar_source"] = default_category
                    if default_category.lower() in ["trabalho", "work", "empresa"]:
                        ev["category"] = "Trabalho"
                return events
        except Exception as e:
            print(f"[Aviso] Falha ao processar feed ({default_category}): {e}")
        return []

    def get_weekly_events(self, mock: bool = False) -> List[Dict[str, Any]]:
        if mock:
            return get_mock_calendar_events()

        all_collected: List[Dict[str, Any]] = []

        # 1. Checa suporte a múltiplas agendas no .env
        # Agenda Pessoal
        url_pessoal = os.getenv("CALENDAR_URL_PESSOAL") or os.getenv("CALENDAR_ICS_URL") or os.getenv("GOOGLE_CALENDAR_ICS")
        if url_pessoal:
            evs = self.fetch_ics_events(url_pessoal, default_category="Pessoal")
            if evs:
                print(f"      ✓ {len(evs)} eventos importados da Agenda Pessoal (.ics)")
                all_collected.extend(evs)

        # Agenda Trabalho
        url_trabalho = os.getenv("CALENDAR_URL_TRABALHO") or os.getenv("CALENDAR_ICS_WORK")
        if url_trabalho:
            evs_work = self.fetch_ics_events(url_trabalho, default_category="Trabalho")
            if evs_work:
                print(f"      ✓ {len(evs_work)} eventos importados da Agenda de Trabalho (.ics)")
                all_collected.extend(evs_work)

        # Múltiplas agendas em formato lista: CALENDAR_URLS="Pessoal=URL1,Trabalho=URL2,Estudos=URL3"
        urls_list = os.getenv("CALENDAR_URLS")
        if urls_list:
            for pair in urls_list.split(","):
                if "=" in pair:
                    label, url = pair.split("=", 1)
                    label = label.strip()
                    url = url.strip()
                    evs_extra = self.fetch_ics_events(url, default_category=label)
                    if evs_extra:
                        print(f"      ✓ {len(evs_extra)} eventos importados da Agenda '{label}'")
                        all_collected.extend(evs_extra)

        if all_collected:
            all_collected.sort(key=lambda x: str(x.get("start", "")))
            return all_collected

        # Se nenhuma URL foi configurada, tenta Calendário do macOS
        macos_events = self.get_events_from_macos_calendar()
        if macos_events:
            print(f"      ✓ {len(macos_events)} eventos importados do Calendário macOS")
            return macos_events

        # Fallback de demonstração
        print("      [Info] Usando agenda modelo de referência.")
        return get_mock_calendar_events()

    @staticmethod
    def get_events_from_macos_calendar() -> List[Dict[str, Any]]:
        apple_script = '''
        set now to current date
        set curWeekday to (weekday of now as integer) - 1
        if curWeekday is 0 then set curWeekday to 7
        set startOfWeek to now - (curWeekday - 1) * days
        set hours of startOfWeek to 0
        set minutes of startOfWeek to 0
        set seconds of startOfWeek to 0
        set endOfWeek to startOfWeek + 7 * days

        set res to "["
        set firstItem to true

        tell application "Calendar"
            repeat with c in calendars
                set cName to name of c
                if cName is not "Feriados" and cName is not "Aniversários" and cName is not "Sugestões da Siri" then
                    set evs to (every event of c whose (start date >= startOfWeek and start date <= endOfWeek))
                    repeat with ev in evs
                        if not firstItem then set res to res & ","
                        set firstItem to false
                        
                        set evTitle to summary of ev
                        set evLoc to location of ev
                        if evLoc is missing value then set evLoc to ""
                        set evStart to (start date of ev as «class isot» as string)
                        set evEnd to (end date of ev as «class isot» as string)
                        
                        set res to res & "{\\"title\\": \\"" & evTitle & "\\", \\"category\\": \\"" & cName & "\\", \\"calendar_source\\": \\"" & cName & "\\", \\"start\\": \\"" & evStart & "\\", \\"end\\": \\"" & evEnd & "\\", \\"location\\": \\"" & evLoc & "\\"}"
                    end repeat
                end if
            end repeat
        end tell
        set res to res & "]"
        return res
        '''
        try:
            p = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
            if p.returncode == 0 and p.stdout.strip():
                events = json.loads(p.stdout.strip())
                if events:
                    return events
        except Exception:
            pass
        return []
