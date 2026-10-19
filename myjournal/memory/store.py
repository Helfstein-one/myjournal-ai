import json
from pathlib import Path
from typing import Dict, Any, List, Set
from myjournal.config import Config

MEMORY_FILE = Config.BASE_DIR / ".myjournal_memory.json"

class MemoryStore:
    def __init__(self, memory_file: Path = MEMORY_FILE):
        self.memory_file = memory_file
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if self.memory_file.exists():
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "editions": [],
            "used_words": [],
            "past_restaurants": [],
            "past_walks": [],
            "past_history_topics": [],
            "past_fashion_topics": [],
            "past_jewelry_topics": [],
            "past_courses": []
        }

    def save(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def get_blacklist_context(self) -> Dict[str, List[str]]:
        return {
            "used_words": self.data.get("used_words", [])[-120:],
            "past_restaurants": self.data.get("past_restaurants", [])[-30:],
            "past_history_topics": self.data.get("past_history_topics", [])[-20:],
            "past_fashion_topics": self.data.get("past_fashion_topics", [])[-20:],
            "past_jewelry_topics": self.data.get("past_jewelry_topics", [])[-20:]
        }

    def record_edition(self, edition_data: Dict[str, Any], word_search_data: Dict[str, Any]):
        # Registra palavras do caça-palavras
        placed = word_search_data.get("placed_words", [])
        for w in placed:
            if w not in self.data["used_words"]:
                self.data["used_words"].append(w)

        # Registra restaurantes de SP
        for rest in edition_data.get("lifestyle_sp", {}).get("gastronomy", []):
            name = rest.get("name")
            if name and name not in self.data["past_restaurants"]:
                self.data["past_restaurants"].append(name)

        # Registra temas culturais
        hist = edition_data.get("culture_history", {}).get("history_article", {}).get("title")
        if hist and hist not in self.data["past_history_topics"]:
            self.data["past_history_topics"].append(hist)

        fash = edition_data.get("culture_history", {}).get("fashion_history_article", {}).get("title")
        if fash and fash not in self.data["past_fashion_topics"]:
            self.data["past_fashion_topics"].append(fash)

        jew = edition_data.get("culture_history", {}).get("jewelry_history_article", {}).get("title")
        if jew and jew not in self.data["past_jewelry_topics"]:
            self.data["past_jewelry_topics"].append(jew)

        # Salva registro da edição
        self.data["editions"].append({
            "date": edition_data.get("metadata", {}).get("date_str", ""),
            "title": edition_data.get("front_page", {}).get("lead_headline", ""),
            "words_count": len(placed)
        })

        self.save()
