import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional
from myjournal.config import Config

class AgendaIntelligenceAgent:
    """Agente especialista em diagnosticar a semana, calcular densidade, traçar estratégia de ritmo e enriquecer cards com IA."""

    @staticmethod
    def analyze_schedule(events: List[Dict[str, Any]]) -> Dict[str, Any]:
        day_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        source_counts: Dict[str, int] = {}
        work_events = []
        personal_events = []

        weekday_names = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

        for ev in events:
            source = ev.get("calendar_source", ev.get("category", "Geral"))
            source_counts[source] = source_counts.get(source, 0) + 1

            cat = ev.get("category", "Pessoal")
            start = ev.get("start", "")
            if cat == "Trabalho" or "trabalho" in source.lower():
                work_events.append(ev)
            else:
                personal_events.append(ev)

            try:
                if "T" in start:
                    dt = datetime.fromisoformat(start)
                    day_counts[dt.weekday()] += 1
            except Exception:
                pass

        busiest_day_idx = max(day_counts, key=day_counts.get) if any(day_counts.values()) else 2
        busiest_day = weekday_names[busiest_day_idx]

        intensity = "moderada"
        if len(work_events) >= 6 or day_counts[busiest_day_idx] >= 3:
            intensity = "alta"
        elif len(work_events) <= 2:
            intensity = "leve"

        sources_summary = ", ".join([f"{src}: {cnt} eventos" for src, cnt in source_counts.items()])

        return {
            "total_events": len(events),
            "sources_summary": sources_summary,
            "source_counts": source_counts,
            "work_count": len(work_events),
            "personal_count": len(personal_events),
            "busiest_day": busiest_day,
            "busiest_count": day_counts[busiest_day_idx],
            "intensity": intensity
        }

    @staticmethod
    def _format_time_only(event: Dict[str, Any]) -> str:
        start_str = event.get("start", "")
        end_str = event.get("end", "")
        try:
            if "T" in start_str:
                dt_start = datetime.fromisoformat(start_str)
                time_part = dt_start.strftime("%H:%M")
                if "T" in end_str:
                    dt_end = datetime.fromisoformat(end_str)
                    return f"{time_part}–{dt_end.strftime('%H:%M')}"
                return time_part
            return "Dia Todo"
        except Exception:
            return start_str

    @classmethod
    def _heuristic_enrichment(cls, title: str, category: str) -> tuple[str, str]:
        t = title.lower()
        if "joalheria" in t or "jóia" in t or "joia" in t or "ourives" in t or "confeccionador" in t:
            return ("💎 Ateliê de Joalheria", "Prática manual de confecção, técnicas de bancada e estudo de joalheria avançada.")
        elif "museu" in t or "acervo" in t or "imigração" in t or "imigracao" in t:
            return ("🏛️ Gestão de Acervo & Museu", "Atuação institucional técnica e salvaguarda no Museu da Imigração.")
        elif "conservação" in t or "conservacao" in t or "restauro" in t or "laudo" in t:
            return ("🔍 Conservação & Restauro", "Diagnóstico de estado, laudo técnico e preservação de acervo histórico.")
        elif "cipa" in t:
            return ("🛡️ Gestão Interna & CIPA", "Acompanhamento e reuniões institucionais no museu.")
        elif "manicure" in t or "beleza" in t or "autocuidado" in t:
            return ("✨ Autocuidado & Bem-Estar", "Momento de pausa pessoal, autocuidado e renovação de energia.")
        elif "piano" in t:
            return ("🎼 Prática Musical", "Aprofundamento na técnica instrumental, leitura e harmonia.")
        elif "férias" in t or "ferias" in t:
            return ("🌿 Recuperação & Pausa", "Período reservado para desconexão deliberada e renovação de energia.")
        elif "oracle" in t or "inteligência artificial" in t or "ia" in t:
            return ("🤝 Networking & IA", "Participação e conexões estratégicas em ecossistema de tecnologia.")
        elif "mercado" in t or "compras" in t:
            return ("⚡ Rotina & Logística", "Organização essencial e abastecimento para a semana.")
        elif "academia" in t or "treino" in t:
            return ("🏃 Saúde & Vitalidade", "Manutenção física e condicionamento para alta disposição mental.")
        elif "idiomas" in t or "conversation" in t or "class" in t:
            return ("📚 Imersão em Idiomas", "Treinamento intensivo de fluência, vocabulário e escuta ativa.")
        elif "consultório" in t or "aves" in t or "veterin" in t or "médic" in t:
            return ("🐾 Cuidados & Bem-Estar", "Acompanhamento dedicado de saúde e atenção personalizada.")
        elif category == "Trabalho":
            return ("🤝 Alinhamento Executivo", "Compromisso tático voltado a resultados corporativos.")
        else:
            return ("🌿 Equilíbrio Pessoal", "Atividade dedicada ao bem-estar e organização pessoal.")

    @classmethod
    def enrich_schedule(cls, events: List[Dict[str, Any]], provider: str = None) -> List[Dict[str, Any]]:
        """
        Organiza os eventos em uma Grade Diária Estruturada com enriquecimento executivo da IA:
        - Cada dia possui: date_str, short_date, cognitive_demand, daily_advice
        - Cada evento possui: time_str, focus_tag, executive_summary, category, title, location
        """
        if not events:
            return []

        # 1. Agrupamento cronológico cobrindo a semana completa (D+0 a D+7)
        from datetime import timedelta
        ref_today = datetime.now()
        start_day = datetime(ref_today.year, ref_today.month, ref_today.day)
        days_map: Dict[str, List[Dict[str, Any]]] = {
            (start_day + timedelta(days=d)).strftime("%Y-%m-%d"): [] for d in range(8)
        }
        weekday_pt = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        short_pt = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

        for ev in events:
            st = ev.get("start", "")
            try:
                dt = datetime.fromisoformat(st) if "T" in st else datetime.fromisoformat(st[:10])
                date_key = dt.strftime("%Y-%m-%d")
            except Exception:
                date_key = "Outros"
            days_map.setdefault(date_key, []).append(ev)

        structured_days = []
        for date_key in sorted(days_map.keys()):
            day_events = days_map[date_key]
            try:
                dt = datetime.fromisoformat(date_key)
                w_idx = dt.weekday()
                date_str = f"{weekday_pt[w_idx]}, {dt.strftime('%d de %B')}"
                short_date = f"{short_pt[w_idx]} • {dt.strftime('%d/%m')}"
            except Exception:
                date_str = "Compromissos da Semana"
                short_date = "Semana"

            day_block = {
                "date_key": date_key,
                "date_str": date_str,
                "short_date": short_date,
                "cognitive_demand": "Moderada",
                "daily_advice": "Mantenha o foco nas prioridades e proteja as pausas de recuperação.",
                "events": []
            }

            for ev in day_events:
                tag, summary = cls._heuristic_enrichment(ev.get("title", ""), ev.get("category", "Pessoal"))
                day_block["events"].append({
                    "id": ev.get("id", ""),
                    "title": ev.get("title", ""),
                    "category": ev.get("category", "Pessoal"),
                    "calendar_source": ev.get("calendar_source", "Pessoal"),
                    "time_str": cls._format_time_only(ev),
                    "location": ev.get("location", ""),
                    "description": ev.get("description", ""),
                    "focus_tag": tag,
                    "executive_summary": summary
                })

            structured_days.append(day_block)

        # 2. Enriquecimento via LLM (Gemini) se disponível
        prov = (provider or Config.AI_PROVIDER).lower()
        if prov == "gemini" and Config.GEMINI_API_KEY:
            try:
                from google import genai
                client = genai.Client(api_key=Config.GEMINI_API_KEY)

                compact_events = []
                for d in structured_days:
                    for ev in d["events"]:
                        compact_events.append({
                            "day": d["short_date"],
                            "title": ev["title"],
                            "time": ev["time_str"],
                            "category": ev["category"],
                            "location": ev["location"]
                        })

                ai_prompt = f"""Você é o Estrategista de Produtividade e Ritmo de Vida do MY Journal (estilo The New York Times).
Analise a agenda semanal do leitor e enriqueça cada dia e cada compromisso com precisão analítica e concisa.

Compromissos estruturados da semana:
{json.dumps(compact_events, ensure_ascii=False, indent=2)}

Gere um JSON com o seguinte formato estrito:
{{
  "days": [
    {{
      "short_date": "ex: Seg • 12/10",
      "cognitive_demand": "Alta Demanda | Foco Criativo | Equilíbrio Tático | Recuperação",
      "daily_advice": "Recomendação executiva de uma única linha sobre a dinâmica de energia do dia",
      "events": [
        {{
          "title": "título exato do evento",
          "focus_tag": "etiqueta com emoji (ex: 🧠 Foco Profundo, 🤝 Alinhamento, ⚡ Operacional, 🌿 Bem-Estar, 🎼 Prática Musical, 🏃 Vitalidade, 📚 Idiomas, 🐾 Cuidados)",
          "executive_summary": "Resumo executivo de uma única linha contextualizando foco ou objetivo"
        }}
      ]
    }}
  ]
}}
Responda APENAS com JSON válido."""

                candidates = ["gemini-flash-latest", "gemini-2.5-flash-lite", Config.GEMINI_MODEL]
                for m in candidates:
                    try:
                        resp = client.models.generate_content(model=m, contents=ai_prompt)
                        raw = resp.text.strip()
                        if "```json" in raw:
                            raw = raw.split("```json")[1].split("```")[0].strip()
                        elif "```" in raw:
                            raw = raw.split("```")[1].split("```")[0].strip()
                        ai_data = json.loads(raw)

                        # Mapeia resultados da IA nos blocos estruturados
                        ai_days_map = {d.get("short_date", ""): d for d in ai_data.get("days", [])}
                        for d in structured_days:
                            matched_day = ai_days_map.get(d["short_date"])
                            if not matched_day:
                                # Tenta match parcial por dia (Seg, Ter, etc)
                                prefix = d["short_date"][:3]
                                for k, val in ai_days_map.items():
                                    if k.startswith(prefix):
                                        matched_day = val
                                        break

                            if matched_day:
                                if matched_day.get("cognitive_demand"):
                                    d["cognitive_demand"] = matched_day["cognitive_demand"]
                                if matched_day.get("daily_advice"):
                                    d["daily_advice"] = matched_day["daily_advice"]

                                ai_events = matched_day.get("events", [])
                                for ev in d["events"]:
                                    for aiev in ai_events:
                                        if aiev.get("title", "").strip().lower() == ev["title"].strip().lower() or ev["title"].strip().lower() in aiev.get("title", "").strip().lower():
                                            if aiev.get("focus_tag"):
                                                ev["focus_tag"] = aiev["focus_tag"]
                                            if aiev.get("executive_summary"):
                                                ev["executive_summary"] = aiev["executive_summary"]
                                            break
                        print("      ✓ Cards da agenda enriquecidos com IA com sucesso")
                        break
                    except Exception as e:
                        continue
            except Exception as e:
                print(f"      [Aviso] Falha ao consultar IA para agenda: {e}. Usando enriquecimento heurístico refinado.")

        return structured_days
