import unicodedata
import random
from typing import List, Dict, Any, Tuple, Optional

def clean_word(word: str) -> str:
    nfkd = unicodedata.normalize('NFKD', word.strip().upper())
    return "".join([c for c in nfkd if not unicodedata.combining(c) and c.isalpha()])

class CrosswordGenerator:
    """Gerador algorítmico de Palavras Cruzadas no estilo clássico do The New York Times."""

    def __init__(self, size: int = 11):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
        self.across_words: List[Dict[str, Any]] = []
        self.down_words: List[Dict[str, Any]] = []

    def can_place_across(self, word: str, r: int, c: int) -> bool:
        length = len(word)
        if c + length > self.size:
            return False
        # Checa célula antes e depois para não colar palavras
        if c > 0 and self.grid[r][c - 1] != '':
            return False
        if c + length < self.size and self.grid[r][c + length] != '':
            return False

        has_intersection = False
        for i, char in enumerate(word):
            curr = self.grid[r][c + i]
            if curr != '' and curr != char:
                return False
            if curr == char:
                has_intersection = True
            elif curr == '':
                # Células vizinhas verticais devem estar vazias a menos que haja interseção
                if r > 0 and self.grid[r - 1][c + i] != '':
                    return False
                if r < self.size - 1 and self.grid[r + 1][c + i] != '':
                    return False

        return has_intersection

    def can_place_down(self, word: str, r: int, c: int) -> bool:
        length = len(word)
        if r + length > self.size:
            return False
        # Checa célula antes e depois
        if r > 0 and self.grid[r - 1][c] != '':
            return False
        if r + length < self.size and self.grid[r + length][c] != '':
            return False

        has_intersection = False
        for i, char in enumerate(word):
            curr = self.grid[r + i][c]
            if curr != '' and curr != char:
                return False
            if curr == char:
                has_intersection = True
            elif curr == '':
                # Células vizinhas horizontais devem estar vazias
                if c > 0 and self.grid[r + i][c - 1] != '':
                    return False
                if c < self.size - 1 and self.grid[r + i][c + 1] != '':
                    return False

        return has_intersection

    def place_across(self, word_obj: Dict[str, Any], r: int, c: int):
        word = word_obj["clean"]
        for i, char in enumerate(word):
            self.grid[r][c + i] = char
        self.across_words.append({
            "word": word_obj["word"],
            "clean": word,
            "clue": word_obj.get("clue", ""),
            "category": word_obj.get("category", "Geral"),
            "difficulty": word_obj.get("difficulty", "Médio"),
            "glossary": word_obj.get("glossary", ""),
            "row": r,
            "col": c,
            "direction": "across"
        })

    def place_down(self, word_obj: Dict[str, Any], r: int, c: int):
        word = word_obj["clean"]
        for i, char in enumerate(word):
            self.grid[r + i][c] = char
        self.down_words.append({
            "word": word_obj["word"],
            "clean": word,
            "clue": word_obj.get("clue", ""),
            "category": word_obj.get("category", "Geral"),
            "difficulty": word_obj.get("difficulty", "Médio"),
            "glossary": word_obj.get("glossary", ""),
            "row": r,
            "col": c,
            "direction": "down"
        })

    def generate(self, word_clues: List[Dict[str, str]]) -> Dict[str, Any]:
        self.grid = [['' for _ in range(self.size)] for _ in range(self.size)]
        self.across_words = []
        self.down_words = []

        valid_entries = []
        for item in word_clues:
            w = item.get("word", "")
            clue = item.get("clue", "")
            clean = clean_word(w)
            if 3 <= len(clean) <= self.size - 1:
                valid_entries.append({
                    "word": w.upper(),
                    "clean": clean,
                    "clue": clue,
                    "category": item.get("category", "Geral"),
                    "difficulty": item.get("difficulty", "Médio"),
                    "glossary": item.get("glossary", "")
                })

        valid_entries.sort(key=lambda x: len(x["clean"]), reverse=True)
        if not valid_entries:
            return self._empty_result()

        # Coloca a primeira palavra horizontal no meio
        first = valid_entries[0]
        start_r = self.size // 2
        start_c = (self.size - len(first["clean"])) // 2
        self.place_across(first, start_r, start_c)

        # Tenta encaixar palavras verticais e horizontais alternadas
        placed_indices = {0}
        for _ in range(8):
            for idx, entry in enumerate(valid_entries):
                if idx in placed_indices:
                    continue

                # Tenta vertical
                placed = False
                for r in range(self.size):
                    for c in range(self.size):
                        if self.can_place_down(entry["clean"], r, c):
                            self.place_down(entry, r, c)
                            placed_indices.add(idx)
                            placed = True
                            break
                    if placed:
                        break

                if placed:
                    continue

                # Tenta horizontal
                for r in range(self.size):
                    for c in range(self.size):
                        if self.can_place_across(entry["clean"], r, c):
                            self.place_across(entry, r, c)
                            placed_indices.add(idx)
                            placed = True
                            break
                    if placed:
                        break

        # Atribui números no estilo oficial de palavras cruzadas (1, 2, 3...)
        numbers_grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        current_num = 1

        all_starts = set()
        for w in self.across_words:
            all_starts.add((w["row"], w["col"]))
        for w in self.down_words:
            all_starts.add((w["row"], w["col"]))

        coord_to_num = {}
        for r in range(self.size):
            for c in range(self.size):
                if (r, c) in all_starts:
                    numbers_grid[r][c] = current_num
                    coord_to_num[(r, c)] = current_num
                    current_num += 1

        for w in self.across_words:
            w["num"] = coord_to_num[(w["row"], w["col"])]
        for w in self.down_words:
            w["num"] = coord_to_num[(w["row"], w["col"])]

        self.across_words.sort(key=lambda x: x["num"])
        self.down_words.sort(key=lambda x: x["num"])

        return {
            "size": self.size,
            "grid": self.grid,
            "numbers": numbers_grid,
            "across": self.across_words,
            "down": self.down_words,
            "total_words": len(self.across_words) + len(self.down_words)
        }

    def _empty_result(self) -> Dict[str, Any]:
        return {
            "size": self.size,
            "grid": self.grid,
            "numbers": [[0]*self.size for _ in range(self.size)],
            "across": [],
            "down": [],
            "total_words": 0
        }
