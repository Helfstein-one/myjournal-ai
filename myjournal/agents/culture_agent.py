from typing import List, Dict, Any

CULTURE_DOMAINS = {
    "history": [
        "Art Déco e industrialização moderna",
        "A reconstrução renascentista e as cortes de Florença",
        "A rota da seda e o intercâmbio têxtil no Mediterrâneo",
        "O Iluminismo e os primeiros cafés literários europeus",
        "A arquitetura brutalista e o modernismo paulistano de Villanova Artigas",
        "A Era Eduardiana e a Belle Époque internacional"
    ],
    "fashion": [
        "A revolução da alfaiataria desestruturada por Giorgio Armani nos anos 80",
        "Madeleine Vionnet e a geometria do corte em viés",
        "Cristóbal Balenciaga e a invenção da silhueta tonel e baby-doll",
        "A linhagem dos casacos Bar da Maison Dior e a volta à opulência",
        "Schiaparelli e o surrealismo de Dalí aplicado à alta costura",
        "Paul Poiret e o fim definitivo do espartilho rígido"
    ],
    "jewelry": [
        "A introdução da platina e os engastes milgrain na Belle Époque",
        "Os relógios de mistério da Cartier e as influências orientais",
        "Diamantes Golconda e o charme orgânico do corte Old Mine",
        "A joalheria Retro dos anos 1940: ouro amarelo suntuoso e gemas lapidadas em almofada",
        "Jean Schlumberger e a flora marinha surrealista na Tiffany & Co.",
        "A técnica do Serti Mystérieux (engaste invisível) da Van Cleef & Arpels"
    ]
}

class CultureCuratorAgent:
    """Agente especialista em pautas eruditas de História, Moda e Alta Joalheria sem repetição."""

    @staticmethod
    def get_prompt_instructions(blacklist: Dict[str, List[str]]) -> str:
        past_hist = blacklist.get("past_history_topics", [])
        past_fash = blacklist.get("past_fashion_topics", [])
        past_jew = blacklist.get("past_jewelry_topics", [])

        instructions = f"""
Diretrizes do Caderno de Cultura, Arte & Saberes:
- Pesquise e redija 3 ensaios profundos, inéditos e fascinantes sobre:
  1. História Geral ou Arquitetura.
  2. História da Moda (técnica têxtil, alfaiataria, designers icônicos).
  3. História da Alta Joalheria (gemologia histórica, lapidações raras, grandes casas joalheiras).
- ANTI-REPETIÇÃO CRÍTICA: Não repita nenhum dos seguintes temas já cobertos em edições anteriores:
  • História já abordada: {', '.join(past_hist) if past_hist else 'Nenhum registro prévio'}
  • Moda já abordada: {', '.join(past_fash) if past_fash else 'Nenhum registro prévio'}
  • Joalheria já abordada: {', '.join(past_jew) if past_jew else 'Nenhum registro prévio'}
- Recomende 3 cursos ou masterclasses reais e de prestígio (instituições de renome como L'ÉCOLE Van Cleef, IFM Paris, Coursera, FAU-USP, MASP, etc.) com links e descrições claras.
"""
        return instructions
