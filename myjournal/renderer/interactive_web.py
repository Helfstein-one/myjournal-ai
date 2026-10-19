import json
from pathlib import Path
from typing import Dict, Any, List
from jinja2 import Environment, FileSystemLoader
from myjournal.renderer.pdf_generator import format_event_time

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"

class InteractiveWebRenderer:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
        self.template = self.env.get_template("interactive_journal.html")

    def render_web_edition(self, data: Dict[str, Any], events: List[Dict[str, Any]], word_search: Dict[str, Any], pdf_filename: str, output_path: str, news_items: List[Dict[str, Any]] = None, crossword: Dict[str, Any] = None, images: Dict[str, Any] = None, agenda_days: List[Dict[str, Any]] = None) -> str:
        formatted_events = []
        for ev in events:
            ev_copy = dict(ev)
            ev_copy["formatted_time"] = format_event_time(ev)
            formatted_events.append(ev_copy)

        solutions_json = json.dumps(word_search.get("solutions", []))
        crossword_json = json.dumps(crossword or {})

        html = self.template.render(
            data=data,
            events=formatted_events,
            word_search=word_search,
            crossword=crossword or {},
            solutions_json=solutions_json,
            crossword_json=crossword_json,
            pdf_url=pdf_filename,
            news_items=news_items or [],
            images=images or {},
            agenda_days=agenda_days or []
        )

        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(html, encoding="utf-8")
        return str(out_file)
