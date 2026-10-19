import json
import re
from typing import Dict, Any, List
from myjournal.config import Config
from myjournal.content.mock_content import get_mock_journal_content

SYSTEM_PROMPT = """Você é o Editor-Chefe de um prestigioso jornal pessoal impresso estilo The New York Times (em Língua Portuguesa - PT-BR).
Sua missão é compilar uma edição semanal sofisticada, analítica, elegante e personalizada com base na agenda semanal do leitor e nas notícias do mundo.
O jornal tem 5 seções principais:
1. Capa (Front Page): Manchete de abertura sobre o ritmo e foco da semana do leitor, resumo do itinerário semanal dos compromissos (trabalho vs pessoal), e narrativa editorial.
2. Política & Assuntos Internacionais: Análise sóbria sobre os principais movimentos geopolíticos e econômicos da semana com manchete e notas breves.
3. Cultura, Arte & Saberes: Ensaios profundos sobre:
   - História Geral
   - História da Moda (evolução de silhuetas, alfaiataria, designers icônicos)
   - História da Joalheria (gemas, épocas como Art Déco / Belle Époque / Eduardiana, mestres joalheiros)
   - Cursos / Masterclasses recomendados para aprofundar nesses temas.
4. Metrópole & Estilo (São Paulo): Recomendações gastronômicas refinadas (bistrôs, confeitarias, cafés de origem) e passeios arquitetônicos/culturais para o fim de semana em São Paulo.
5. Palavras-chave temáticas para o Caça-Palavras (10 a 14 palavras sem acento, com 4 a 12 letras cada, refletindo os compromissos da semana, história da joalheria, moda e cultura).

Responda SEMPRE E APENAS em JSON válido com a estrutura especificada."""

class LLMCurator:
    def __init__(self, provider: str = None):
        self.provider = (provider or Config.AI_PROVIDER).lower()

    def generate_journal(self, calendar_events: List[Dict[str, Any]], news_data: Dict[str, Any] = None) -> Dict[str, Any]:
        # Se nenhuma chave configurada, usa conteúdo modelo sofisticado
        if self.provider == "gemini" and not Config.GEMINI_API_KEY:
            print("[Info] GEMINI_API_KEY não configurada. Usando edição modelo curada.")
            return get_mock_journal_content(Config.OWNER_NAME)
        elif self.provider == "openai" and not Config.OPENAI_API_KEY:
            print("[Info] OPENAI_API_KEY não configurada. Usando edição modelo curada.")
            return get_mock_journal_content(Config.OWNER_NAME)

        context_prompt = f"""
Dados da Semana para a Edição:
- Leitor / Proprietário: {Config.OWNER_NAME}
- Cidade: {Config.CITY}
- Compromissos da Agenda na Semana:
{json.dumps(calendar_events, ensure_ascii=False, indent=2)}

- Notícias recentes coletadas:
{json.dumps(news_data or {}, ensure_ascii=False, indent=2)}

Gere um JSON exatamente com o seguinte formato:
{{
  "metadata": {{
    "title": "{Config.NEWSPAPER_TITLE}",
    "subtitle": "{Config.NEWSPAPER_SUBTITLE}",
    "date_str": "Data formatada da semana (ex: Segunda-feira, 20 de Outubro de 2026)",
    "volume": "VOL. CLXXV... No. 60.420",
    "edition": "EDIÇÃO PAULISTANA",
    "weather": "Previsão do tempo estimada para São Paulo nesta semana",
    "quote": "Citação clássica e erudita sobre arte, tempo ou elegância"
  }},
  "front_page": {{
    "lead_headline": "Manchete principal impactante em caixa alta sobre o tom da semana",
    "lead_subdeck": "Subtítulo analítico conectando a agenda de trabalho e pessoal",
    "lead_article": "Texto jornalístico elegante de 2 a 3 parágrafos narrando a semana e prioridades",
    "itinerary_summary": "Resumo sintético dos principais blocos do itinerário semanal"
  }},
  "politics_world": {{
    "headline": "Manchete de Política / Economia Internacional",
    "subdeck": "Subtítulo analítico",
    "main_article": "Artigo aprofundado estilo editorial de jornal sobre conjuntura global",
    "briefs": [
      {{"title": "Título Breve 1", "text": "Texto explicativo conciso"}},
      {{"title": "Título Breve 2", "text": "Texto explicativo conciso"}},
      {{"title": "Título Breve 3", "text": "Texto explicativo conciso"}}
    ]
  }},
  "culture_history": {{
    "history_article": {{
      "title": "Título do artigo de História",
      "content": "Texto erudito de história com detalhes e contexto"
    }},
    "fashion_history_article": {{
      "title": "Título do artigo de História da Moda",
      "content": "Texto fascinante sobre alfaiataria, estilistas ou movimentos de moda"
    }},
    "jewelry_history_article": {{
      "title": "Título do artigo de História da Joalheria",
      "content": "Texto aprofundado sobre lapidações, épocas (ex: Art Déco), pedras preciosas ou joalheiros históricos"
    }},
    "courses": [
      {{
        "title": "Nome do Curso / Workshop",
        "institution": "Instituição / Plataforma",
        "description": "Breve sinopse do conteúdo programático"
      }},
      {{
        "title": "Nome do Curso 2",
        "institution": "Instituição 2",
        "description": "Breve sinopse"
      }},
      {{
        "title": "Nome do Curso 3",
        "institution": "Instituição 3",
        "description": "Breve sinopse"
      }}
    ]
  }},
  "lifestyle_sp": {{
    "section_title": "METRÓPOLE & ESTILO: O GUIA PAULISTANO",
    "section_intro": "Breve parágrafo de introdução sobre a gastronomia e o fim de semana em SP",
    "gastronomy": [
      {{
        "name": "Nome do Restaurante / Bistrô / Café",
        "neighborhood": "Bairro (ex: Jardins, Pinheiros, Higienópolis)",
        "highlight": "Prato ou especialidade recomendada com detalhes",
        "ambience": "Descrição da atmosfera do local"
      }},
      {{
        "name": "Nome do Segundo Estabelecimento",
        "neighborhood": "Bairro",
        "highlight": "Especialidade",
        "ambience": "Atmosfera"
      }},
      {{
        "name": "Nome do Terceiro Estabelecimento",
        "neighborhood": "Bairro",
        "highlight": "Especialidade",
        "ambience": "Atmosfera"
      }}
    ],
    "walks": [
      {{
        "title": "Título do Passeio Cultural ou Arquitetônico",
        "itinerary": "Pontos e trajeto recomendado",
        "tip": "Dica especial de horário ou observação estética"
      }},
      {{
        "title": "Segundo Passeio em SP",
        "itinerary": "Trajeto",
        "tip": "Dica especial"
      }}
    ]
  }},
  "games_diversions": {{
    "title": "DIVERSÕES DA MENTE: CAÇA-PALAVRAS DA SEMANA",
    "instructions": "Encontre as palavras temáticas escondidas na grade.",
    "words_to_find": ["PALAVRA1", "PALAVRA2", "PALAVRA3", "PALAVRA4", "PALAVRA5", "PALAVRA6", "PALAVRA7", "PALAVRA8", "PALAVRA9", "PALAVRA10"]
  }}
}}
"""

        try:
            raw_text = ""
            if self.provider == "gemini":
                from google import genai
                client = genai.Client(api_key=Config.GEMINI_API_KEY)
                candidate_models = [
                    Config.GEMINI_MODEL,
                    "gemini-3.5-flash",
                    "gemini-flash-latest",
                    "gemini-3.1-flash-lite",
                    "gemini-2.5-flash-lite"
                ]
                
                raw_text = None
                last_err = None
                for m in candidate_models:
                    try:
                        print(f"      [IA] Solicitando geração editorial ao {m}...")
                        response = client.models.generate_content(
                            model=m,
                            contents=[SYSTEM_PROMPT, context_prompt]
                        )
                        raw_text = response.text
                        if raw_text:
                            print(f"      ✓ Sucesso na curadoria com {m}")
                            break
                    except Exception as err:
                        last_err = err
                        print(f"      [Aviso] Modelo {m} indisponível ({err}). Tentando alternativo...")

                if not raw_text:
                    raise last_err
            elif self.provider == "openai":
                from openai import OpenAI
                client = OpenAI(api_key=Config.OPENAI_API_KEY)
                response = client.chat.completions.create(
                    model=Config.OPENAI_MODEL,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": context_prompt}
                    ],
                    response_format={"type": "json_object"}
                )
                raw_text = response.choices[0].message.content

            # Extrai e parseia JSON
            clean_json = raw_text.strip()
            if "```json" in clean_json:
                clean_json = clean_json.split("```json")[1].split("```")[0].strip()
            elif "```" in clean_json:
                clean_json = clean_json.split("```")[1].split("```")[0].strip()

            data = json.loads(clean_json)
            return data

        except Exception as e:
            print(f"[Aviso] Falha na chamada da IA ({e}). Usando edição modelo de alta qualidade.")
            return get_mock_journal_content(Config.OWNER_NAME)
