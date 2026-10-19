from typing import List, Dict, Any
from myjournal.games.word_search import WordSearchGenerator, normalize_word
from myjournal.games.crossword import CrosswordGenerator

CULTURAL_LEXICON: Dict[str, Dict[str, str]] = {
    "OURIVES": {
        "clue": "Mestre artífice dedicado à fundição, cinzelagem e conformação de ligas nobres",
        "category": "Ofícios de Bancada",
        "difficulty": "Fácil",
        "definition": "Profissional especializado na manipulação e cinzelagem de metais preciosos como ouro, prata e platina.",
        "etymology": "Do latim 'aurifex' (auri = ouro + facere = fazer); preserva técnicas milenares de bancada."
    },
    "RESTAURO": {
        "clue": "Intervenção técnica deliberada para devolver integridade e legibilidade a um bem cultural",
        "category": "Conservação & Acervo",
        "difficulty": "Médio",
        "definition": "Ato crítico-metodológico voltado a preservar a matéria original sem falseamento histórico.",
        "etymology": "Fundamentado na Teoria do Restauro de Cesare Brandi: primado da reversibilidade e mínima intervenção."
    },
    "ACERVO": {
        "clue": "Conjunto ordenado de bens materiais ou imateriais sob salvaguarda institucional",
        "category": "Museologia & Acervos",
        "difficulty": "Fácil",
        "definition": "Totalidade de peças, documentos e testemunhos históricos catalogados em museus e arquivos.",
        "etymology": "Do latim 'acervus' (montão ordenado, reunião de bens valiosos para a memória coletiva)."
    },
    "MUSEU": {
        "clue": "Espaço permanente e público dedicado à investigação, salvaguarda e difusão do patrimônio",
        "category": "Patrimônio & Sociedade",
        "difficulty": "Fácil",
        "definition": "Instituição cultural sem fins lucrativos que preserva e expõe a herança material e imaterial da humanidade.",
        "etymology": "Do grego 'mouseion' (templo sagrado consagrado às Musas protetoras das artes e ciências)."
    },
    "VENDOME": {
        "clue": "Octogonal praça parisiense que se tornou epicentro mundial da alta joalheria",
        "category": "Alta Joalheria",
        "difficulty": "Médio",
        "definition": "Praça monumental em Paris que concentra as mais prestigiadas maisons joalheiras desde o século XIX.",
        "etymology": "Projetada pelo arquiteto Jules Hardouin-Mansart sob o reinado de Luís XIV."
    },
    "PLATINA": {
        "clue": "Metal nobre, denso e refratário introduzido nas joias da Era Eduardiana",
        "category": "Alta Joalheria",
        "difficulty": "Médio",
        "definition": "Metal de alta dureza e ponto de fusão elevado (1.768 °C), ideal para estruturas finíssimas e duráveis.",
        "etymology": "Do espanhol 'platina' (pequena prata); símbolo de perenidade e sobriedade na orfebreria."
    },
    "CRAVACAO": {
        "clue": "Ato de assentar e prender gemas preciosas em virolas, garras ou pavês de metal",
        "category": "Ofícios de Bancada",
        "difficulty": "Desafio",
        "definition": "Técnica mecânica de alta destreza para imobilizar pedras preservando sua passagem de luz.",
        "etymology": "Procedimento artesanal que define o acabamento invisível ou tradicional de uma alta joia."
    },
    "LAPIDACAO": {
        "clue": "Técnica geométrica de esculpir facetas em gemas para maximizar reflexão e fogo",
        "category": "Gemologia Histórica",
        "difficulty": "Médio",
        "definition": "Arte de facetar cristais brutos revelando o índice de refração e o pleocroísmo ótico.",
        "etymology": "Do latim 'lapidare' (trabalhar a pedra); evoluiu do corte em cabochão para as 57 facetas modernas."
    },
    "IMIGRACAO": {
        "clue": "Fluxo histórico de povos e saberes fundamentais na formação da metrópole paulistana",
        "category": "História & Cidade",
        "difficulty": "Fácil",
        "definition": "Movimento de acolhimento transcontinental simbolizado pelo complexo da Hospedaria do Brás.",
        "etymology": "Do latim 'immigratio'; patrimônio imaterial vivo da cultura e da diversidade de São Paulo."
    },
    "ESMERALDA": {
        "clue": "Gema nobre de berilo cujo tom verde intenso é originado por traços de cromo e vanádio",
        "category": "Gemologia Histórica",
        "difficulty": "Médio",
        "definition": "Pedra preciosa clássica, famosa por suas inclusões naturais conhecidas poeticamente como 'jardin'.",
        "etymology": "Do grego 'smaragdos'; apreciada desde o Antigo Egito e a corte dos czares."
    },
    "ARTDECO": {
        "clue": "Estilo geométrico dos anos 1920 que celebrou o dinamismo da era industrial e das artes decorativas",
        "category": "História da Arte",
        "difficulty": "Médio",
        "definition": "Movimento visual sintetizado na Exposição Internacional de Paris de 1925.",
        "etymology": "Abreviação de 'Arts Décoratifs'; marcou a arquitetura paulistana e a alta joalheria geométrica."
    },
    "GRAVURA": {
        "clue": "Obra impressa obtida por incisão manual sobre metal, pedra ou xilogravura",
        "category": "Artes Gráficas",
        "difficulty": "Desafio",
        "definition": "Técnica de reprodução artística em matriz entalhada, base dos tratados e broadsheets clássicos.",
        "etymology": "Do francês 'gravure'; técnica usada por Albrecht Dürer e Rembrandt."
    },
    "ALFAIATE": {
        "clue": "Artífice da alfaiataria focado na arquitetura corporal e corte sob medida",
        "category": "História da Moda",
        "difficulty": "Médio",
        "definition": "Mestre do tecido estruturado, do alinhavo de entretelas e do caimento anatômico.",
        "etymology": "Do árabe 'al-khayyāt' (aquele que cose com precisão métrica)."
    },
    "CONSERVACAO": {
        "clue": "Conjunto de ações preventivas voltadas a prolongar a vida útil de bens culturais",
        "category": "Conservação & Acervo",
        "difficulty": "Fácil",
        "definition": "Controle de umidade, temperatura e manuseio para retardar a degradação material de acervos.",
        "etymology": "Do latim 'conservatio' (manter intacto e protegido de agentes de deterioração)."
    },
    "PATRIMONIO": {
        "clue": "Herança coletiva material e imaterial herdada do passado e legada às gerações futuras",
        "category": "Patrimônio & Sociedade",
        "difficulty": "Fácil",
        "definition": "Bens móveis, imóveis e saberes orais protegidos por instituições de tutela e museus.",
        "etymology": "Do latim 'patrimonium' (herança paterna, bens transmitidos através dos séculos)."
    }
}

class PuzzleArchitectAgent:
    """Agente responsável por criar o caça-palavras inédito e as palavras cruzadas estilo NYT."""

    @classmethod
    def build_word_search(cls, suggested_words: List[str], blacklist: Dict[str, List[str]], size: int = 15) -> Dict[str, Any]:
        used_set = set(normalize_word(w) for w in blacklist.get("used_words", []))

        novel_words = []
        for w in suggested_words:
            norm = normalize_word(w)
            if 3 <= len(norm) <= size and norm not in used_set:
                novel_words.append(w)

        pool = list(CULTURAL_LEXICON.keys()) + [
            "CARTIER", "PINHEIROS", "JARDINS", "MODERNISMO", "BRUTALISMO",
            "CRONOMETRO", "ESTRATEGIA", "DIOR", "SCHIAPARELLI", "RUBI",
            "SAFIRA", "CONFEITARIA", "BISTRO", "CRONICA"
        ]

        for candidate in pool:
            if len(novel_words) >= 12:
                break
            norm = normalize_word(candidate)
            if norm not in used_set and candidate not in novel_words:
                novel_words.append(candidate)

        generator = WordSearchGenerator(size=size)
        result = generator.generate(novel_words)

        # Enriquece cada palavra posicionada com mini-glossário cultural
        enriched_glossary = {}
        for w in result["placed_words"]:
            clean = normalize_word(w)
            if clean in CULTURAL_LEXICON:
                enriched_glossary[clean] = CULTURAL_LEXICON[clean]
            else:
                enriched_glossary[clean] = {
                    "category": "Léxico Cultural",
                    "difficulty": "Médio",
                    "definition": f"Conceito e vocábulo temático da edição dominical ({w.title()}).",
                    "etymology": "Termo selecionado pela curadoria editorial do The Personal Dispatch."
                }

        result["glossary"] = enriched_glossary
        return result

    @classmethod
    def build_crossword(cls, clues_list: List[Dict[str, str]], size: int = 11) -> Dict[str, Any]:
        curated_clues = []
        for word, meta in CULTURAL_LEXICON.items():
            curated_clues.append({
                "word": word,
                "clue": meta["clue"],
                "category": meta["category"],
                "difficulty": meta["difficulty"],
                "glossary": meta["definition"]
            })

        # Se houver pistas geradas pela IA, mescla com as curadas de prestígio
        if clues_list:
            for item in clues_list:
                w = item.get("word", "").upper()
                if w and len(normalize_word(w)) <= size - 1:
                    meta = CULTURAL_LEXICON.get(normalize_word(w), {})
                    curated_clues.append({
                        "word": w,
                        "clue": item.get("clue", meta.get("clue", "Pista editorial da semana")),
                        "category": meta.get("category", "Geral"),
                        "difficulty": meta.get("difficulty", "Médio"),
                        "glossary": meta.get("definition", "")
                    })

        generator = CrosswordGenerator(size=size)
        return generator.generate(curated_clues)
