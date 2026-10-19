import random
import unicodedata
from typing import List, Dict, Tuple, Optional

def normalize_word(word: str) -> str:
    nfkd = unicodedata.normalize('NFKD', word.strip().upper())
    return "".join([c for c in nfkd if not unicodedata.combining(c) and c.isalpha()])

class WordSearchGenerator:
    DIRECTIONS = [
        (0, 1),   # Direita
        (0, -1),  # Esquerda
        (1, 0),   # Baixo
        (-1, 0),  # Cima
        (1, 1),   # Diagonal baixo-direita
        (-1, -1), # Diagonal cima-esquerda
        (1, -1),  # Diagonal baixo-esquerda
        (-1, 1)   # Diagonal cima-direita
    ]

    def __init__(self, size: int = 15):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
        self.placed_words: List[Dict[str, any]] = []

    def can_place(self, word: str, row: int, col: int, dr: int, dc: int) -> bool:
        length = len(word)
        end_r = row + dr * (length - 1)
        end_c = col + dc * (length - 1)
        
        if not (0 <= end_r < self.size and 0 <= end_c < self.size):
            return False

        r, c = row, col
        for char in word:
            current = self.grid[r][c]
            if current != '' and current != char:
                return False
            r += dr
            c += dc
        return True

    def place_word(self, word: str, row: int, col: int, dr: int, dc: int):
        r, c = row, col
        for char in word:
            self.grid[r][c] = char
            r += dr
            c += dc

    def generate(self, words: List[str]) -> Dict[str, any]:
        # Reset grid
        self.grid = [['' for _ in range(self.size)] for _ in range(self.size)]
        self.placed_words = []

        # Normaliza palavras e filtra tamanho
        valid_words = []
        for w in words:
            clean = normalize_word(w)
            if 3 <= len(clean) <= self.size:
                valid_words.append((w, clean))

        # Ordena palavras das mais longas para as mais curtas para facilitar encaixe
        valid_words.sort(key=lambda x: len(x[1]), reverse=True)

        for original, clean in valid_words:
            placed = False
            attempts = 0
            while not placed and attempts < 150:
                attempts += 1
                dr, dc = random.choice(self.DIRECTIONS)
                r = random.randint(0, self.size - 1)
                c = random.randint(0, self.size - 1)

                if self.can_place(clean, r, c, dr, dc):
                    self.place_word(clean, r, c, dr, dc)
                    self.placed_words.append({
                        "word": original.upper(),
                        "clean": clean,
                        "start": (r + 1, c + 1),
                        "direction": (dr, dc)
                    })
                    placed = True

        # Preenche vazios com letras aleatórias
        pt_letters = "AAAAAEEEEIIIOOOUUBCDFGHJLMNPQRSTVZ"
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == '':
                    self.grid[r][c] = random.choice(pt_letters)

        return {
            "size": self.size,
            "grid": self.grid,
            "placed_words": [p["word"] for p in self.placed_words],
            "solutions": self.placed_words
        }
