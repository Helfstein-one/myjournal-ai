"""Agente Especializado em Ofícios de Bancada, Restauro, Oportunidades e Ciência dos Materiais.
Responsável pela Página 12 com editais e vagas dos órgãos oficiais (SISEM-SP, IPHAN, IBRAM, ProAC, AJESP).
"""
from typing import Dict, Any
from myjournal.content.cultural_jobs import CulturalJobsAggregator
from myjournal.content.mock_content import get_mock_journal_content
from myjournal.config import Config

class CareersCraftsAgent:
    """Agente de carreiras técnicas, ourivesaria e salvaguarda do patrimônio cultural."""

    @classmethod
    def compile_section(cls) -> Dict[str, Any]:
        """Compila o caderno de ofícios e oportunidades dividido nos 3 blocos aprovados."""
        three_blocks = CulturalJobsAggregator.get_three_block_opportunities()
        flat_opps = CulturalJobsAggregator.get_all_opportunities_flat(limit=6)
        mock_fallback = get_mock_journal_content(Config.OWNER_NAME)["crafts_careers"]

        return {
            "title": "OFÍCIOS DE BANCADA, CONCURSOS & OPORTUNIDADES",
            "subtitle": "Concursos públicos, editais de salvaguarda de acervos e vagas técnicas em ateliês de alta ourivesaria.",
            "opportunities": flat_opps,
            "three_blocks": three_blocks,
            "curiosities": mock_fallback.get("curiosities", [])
        }
