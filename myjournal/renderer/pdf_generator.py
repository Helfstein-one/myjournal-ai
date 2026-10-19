import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"
STYLE_PATH = Path(__file__).resolve().parent / "style.css"

def format_event_time(event: Dict[str, Any]) -> str:
    start_str = event.get("start", "")
    end_str = event.get("end", "")
    try:
        if "T" in start_str:
            dt_start = datetime.fromisoformat(start_str)
            weekday_pt = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"][dt_start.weekday()]
            time_part = dt_start.strftime("%H:%M")
            if "T" in end_str:
                dt_end = datetime.fromisoformat(end_str)
                return f"{weekday_pt}, {time_part}–{dt_end.strftime('%H:%M')}"
            return f"{weekday_pt}, {time_part}"
        elif start_str:
            dt_start = datetime.fromisoformat(start_str)
            weekday_pt = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"][dt_start.weekday()]
            return f"{weekday_pt}, Dia Todo"
    except Exception:
        pass
    return start_str

class PDFGenerator:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
        self.template = self.env.get_template("newspaper.html")

    def render_html(self, data: Dict[str, Any], events: List[Dict[str, Any]], word_search: Dict[str, Any], news_items: List[Dict[str, Any]] = None, crossword: Dict[str, Any] = None, images: Dict[str, Any] = None, agenda_days: List[Dict[str, Any]] = None) -> str:
        # Prepara formatação de horários nos eventos
        formatted_events = []
        for ev in events:
            ev_copy = dict(ev)
            ev_copy["formatted_time"] = format_event_time(ev)
            formatted_events.append(ev_copy)

        html_content = self.template.render(
            data=data,
            events=formatted_events,
            word_search=word_search,
            crossword=crossword or {},
            news_items=news_items or [],
            images=images or {},
            agenda_days=agenda_days or []
        )
        return html_content

    def generate_pdf(self, html_content: str, output_path: str) -> str:
        from playwright.sync_api import sync_playwright

        output_file = Path(output_path).resolve()
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Grava HTML temporário no mesmo diretório dos templates para carregar style.css
        temp_html_path = TEMPLATE_DIR / "temp_render.html"
        
        # Garante que style.css esteja copiado em templates se necessário
        temp_css_dest = TEMPLATE_DIR / "style.css"
        if not temp_css_dest.exists() or temp_css_dest.stat().st_mtime < STYLE_PATH.stat().st_mtime:
            temp_css_dest.write_text(STYLE_PATH.read_text(encoding="utf-8"), encoding="utf-8")

        temp_html_path.write_text(html_content, encoding="utf-8")

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{temp_html_path}", wait_until="networkidle")
            
            # Gera PDF em formato A4 perfeito
            page.pdf(
                path=str(output_file),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
            )
            browser.close()

        # Remove HTML temporário
        if temp_html_path.exists():
            temp_html_path.unlink()

        return str(output_file)
