import re
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Any

def parse_ics_datetime(dt_str: str) -> Optional[datetime]:
    if not dt_str:
        return None
    # Remove timezone tags se houver
    val = dt_str.split(":")[-1].strip()
    try:
        if "T" in val:
            if val.endswith("Z"):
                dt = datetime.strptime(val, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
                # Converte para horário de São Paulo (UTC-3)
                sp_tz = timezone(timedelta(hours=-3))
                return dt.astimezone(sp_tz).replace(tzinfo=None)
            else:
                return datetime.strptime(val[:15], "%Y%m%dT%H%M%S")
        else:
            return datetime.strptime(val[:8], "%Y%m%d")
    except Exception:
        return None

class ICSCalendarParser:
    @staticmethod
    def parse_events(ics_content: str, target_date: Optional[datetime] = None) -> List[Dict[str, Any]]:
        ref_date = target_date or datetime.now()
        # Janela de 1 semana a partir do dia de publicação (Domingo D+0 até o próximo Domingo D+7)
        start_of_window = datetime(ref_date.year, ref_date.month, ref_date.day, 0, 0, 0)
        end_of_window = start_of_window + timedelta(days=7, hours=23, minutes=59, seconds=59)

        byday_map = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6}

        # Parse de blocos VEVENT
        raw_events = []
        vevents = ics_content.split("BEGIN:VEVENT")

        for block in vevents[1:]:
            summary = ""
            dtstart_raw = ""
            dtend_raw = ""
            location = ""
            description = ""
            rrule = ""

            for line in block.splitlines():
                if line.startswith("SUMMARY:"):
                    summary = line[8:].replace("\\,", ",").replace("\\;", ";").strip()
                elif line.startswith("DTSTART"):
                    dtstart_raw = line.split(":", 1)[-1].strip()
                elif line.startswith("DTEND"):
                    dtend_raw = line.split(":", 1)[-1].strip()
                elif line.startswith("LOCATION:"):
                    location = line[9:].replace("\\,", ",").replace("\\;", ";").strip()
                elif line.startswith("DESCRIPTION:"):
                    description = line[12:].replace("\\n", "\n").replace("\\,", ",").strip()
                elif line.startswith("RRULE:"):
                    rrule = line[6:].strip()

            if not summary or not dtstart_raw:
                continue

            dt_start = parse_ics_datetime(dtstart_raw)
            dt_end = parse_ics_datetime(dtend_raw)

            if not dt_start:
                continue

            # Classificação inteligente de categoria
            work_keywords = [
                "fiap", "entrevista", "meeting", "reunião", "reuniao", "debrief", "thoughtworks",
                "work", "job", "alinhamento", "sprint", "museu", "imigração", "imigracao",
                "conservação", "conservacao", "restauro", "acervo", "cipa", "estágio", "estagio",
                "treinamento", "laudo"
            ]
            is_work = any(k in summary.lower() for k in work_keywords)
            category = "Trabalho" if is_work else "Pessoal"

            # 1. Evento direto caindo na janela D+0 a D+7
            if start_of_window <= dt_start <= end_of_window:
                raw_events.append({
                    "title": summary,
                    "category": category,
                    "dt_start": dt_start,
                    "dt_end": dt_end or dt_start,
                    "start": dt_start.isoformat(),
                    "end": dt_end.isoformat() if dt_end else dt_start.isoformat(),
                    "location": location,
                    "description": description[:180] if description else "",
                    "rrule": rrule
                })
            # 2. Evento recorrente semanal ativo (FREQ=WEEKLY)
            elif "FREQ=WEEKLY" in rrule:
                until_dt = None
                if "UNTIL=" in rrule:
                    m = re.search(r"UNTIL=(\d{8}(?:T\d{6}Z?)?)", rrule)
                    if m:
                        until_dt = parse_ics_datetime(m.group(1))

                # Se a recorrência já encerrou antes da janela, ignorar
                if until_dt and until_dt < start_of_window:
                    continue

                target_weekdays = []
                if "BYDAY=" in rrule:
                    m_days = re.search(r"BYDAY=([A-Z,]+)", rrule)
                    if m_days:
                        target_weekdays = [byday_map[d] for d in m_days.group(1).split(",") if d in byday_map]
                if not target_weekdays:
                    target_weekdays = [dt_start.weekday()]

                duration = (dt_end - dt_start) if dt_end else timedelta(hours=1)

                for day_offset in range(8):  # D+0 (domingo) até D+7 (domingo seguinte)
                    cand_day = start_of_window + timedelta(days=day_offset)
                    if cand_day.weekday() in target_weekdays and dt_start.date() <= cand_day.date():
                        if until_dt and cand_day.date() > until_dt.date():
                            continue
                        proj_start = cand_day.replace(hour=dt_start.hour, minute=dt_start.minute)
                        proj_end = proj_start + duration
                        raw_events.append({
                            "title": summary,
                            "category": category,
                            "dt_start": proj_start,
                            "dt_end": proj_end,
                            "start": proj_start.isoformat(),
                            "end": proj_end.isoformat(),
                            "location": location,
                            "description": description[:180] if description else "",
                            "rrule": rrule
                        })

        # Ordena cronologicamente
        raw_events.sort(key=lambda x: x["dt_start"])

        # Converte dt_start e dt_end para string ISO para total compatibilidade com JSON
        clean_events = []
        for ev in raw_events:
            ev_copy = dict(ev)
            ev_copy.pop("dt_start", None)
            ev_copy.pop("dt_end", None)
            clean_events.append(ev_copy)

        return clean_events
