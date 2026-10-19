"""Agente Especializado em Cultura Acadêmica, História, Indumentária e Gemologia.
Responsável pelas Páginas 7 (Op-Ed), 8 (História), 9 (Alta Costura) e 10 (Alta Joalheria).
Baseado estritamente em periódicos científicos revisados por pares e ensaios canônicos (SciELO, USP, ABEPEM, GIA, IPHAN).
"""
from typing import Dict, Any
from myjournal.content.academic_repo import AcademicRepository
from myjournal.content.cultural_jobs import CulturalJobsAggregator

class AcademicCultureAgent:
    """Agente de pesquisa acadêmica oficial e erudição histórica."""

    @classmethod
    def compile_sections(cls) -> Dict[str, Any]:
        """Compila os 4 cadernos acadêmicos do jornal com proveniência e DOI oficiais."""
        # 1. Página 7: Op-Ed (Ensaios Reais)
        oped_data = AcademicRepository.get_oped_columns()

        # 2. Página 8: História Geral & Salvaguarda (Anais do Museu Paulista / USP / SciELO)
        history_article = AcademicRepository.get_history_article()

        # 3. Página 9: Alta Costura & Conservação Têxtil (Revista Dobras / ABEPEM)
        fashion_article = AcademicRepository.get_fashion_history_article()

        # 4. Página 10: Alta Joalheria & Cristalografia (GIA Gems & Gemology)
        jewelry_article = AcademicRepository.get_jewelry_academic_article()

        # 5. Cursos de Excelência Reconhecidos (GIA, L'ÉCOLE, FAU-USP)
        courses = CulturalJobsAggregator.get_recent_courses()

        return {
            "oped": oped_data,
            "culture_history": {
                "history_article": history_article,
                "fashion_history_article": fashion_article,
                "jewelry_history_article": jewelry_article,
                "courses": courses
            }
        }
