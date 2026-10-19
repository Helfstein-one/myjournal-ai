import urllib.parse
from typing import List, Dict, Any

class MetropoleSPAgent:
    """Agente especialista em garimpar gastronomia de alta qualidade e roteiros arquitetônicos em São Paulo."""

    @staticmethod
    def get_prompt_instructions(blacklist: Dict[str, List[str]], agenda_diag: Dict[str, Any]) -> str:
        past_rests = blacklist.get("past_restaurants", [])
        intensity = agenda_diag.get("intensity", "moderada")
        busiest_day = agenda_diag.get("busiest_day", "Quarta-feira")

        instructions = f"""
Diretrizes do Caderno Metrópole & Estilo de Vida (São Paulo) — EDIÇÃO EXPANDIDA:
- O leitor tem uma semana de intensidade {intensity.upper()}, com pico na {busiest_day}.
- Selecione 6 estabelecimentos gastronômicos excepcionais e diversificados em São Paulo:
  1. Café Especial de Bancada / Confeitaria Fina (para foco ou reuniões rápidas)
  2. Bistrô de Almoço Autoral (para descompressão no meio da semana)
  3. Clássico da Alta Gastronomia Paulistana (para celebração de fim de semana)
  4. Bar de Coquetelaria & Balcão Intimista
  5. Padaria Artesanal / Brunch de Domingo
  6. Casa Tradicional / Cantina Histórica ou Empório
- Para cada restaurante, forneça:
  • "name": Nome do estabelecimento
  • "neighborhood": Bairro
  • "type": Categoria (ex: Alta Gastronomia Italiana, Café Especial & Pâtisserie)
  • "highlight": Resenha sensorial da atmosfera
  • "dish": Prato ou bebida imperdível sugerida
  • "hours": Melhor horário ou ocasião recomendada
- ANTI-REPETIÇÃO CRÍTICA: Não repita os seguintes restaurantes já recomendados:
  • Já visitados/recomendados: {', '.join(past_rests) if past_rests else 'Nenhum registro prévio'}

- Selecione 4 passeios e exposições culturais/arquitetônicas imperdíveis em São Paulo:
  1. Museu & Acervo Histórico (com foco em conservação/patrimônio, ex: Museu da Imigração, Museu Paulista, Pinacoteca)
  2. Grande Exposição de Arte em Cartaz (ex: MASP, Instituto Tomie Ohtake, IMS Paulista)
  3. Circuito Arquitetônico Urbano (ex: Centro Histórico e edifícios modernistas, Higienópolis ou Jardins)
  4. Parque & Refúgio Verde com Café (ex: Parque Ibirapuera / Pavilhão da Bienal, Parque Augusta)
- Para cada passeio, forneça:
  • "title": Título evocativo do roteiro ou exposição
  • "institution": Instituição ou região
  • "itinerary": Trajeto detalhado ou foco curatorial da visita
  • "tip": Dica prática de curadoria (melhor luz, horário silencioso, ingressos)
  • "hours": Horário de funcionamento
"""
        return instructions

    @staticmethod
    def enrich_with_map_links(lifestyle_data: Dict[str, Any]) -> Dict[str, Any]:
        """Adiciona URLs clicáveis do Google Maps para cada estabelecimento e passeio."""
        data_copy = dict(lifestyle_data)
        for rest in data_copy.get("gastronomy", []):
            name = rest.get("name", "")
            bairro = rest.get("neighborhood", "")
            query = f"{name} {bairro} São Paulo"
            rest["map_url"] = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(query)}"

        for walk in data_copy.get("walks", []):
            title = walk.get("title", "")
            query = f"{title} São Paulo"
            walk["map_url"] = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(query)}"

        return data_copy
