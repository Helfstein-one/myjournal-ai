from datetime import datetime, timedelta
from typing import List, Dict

def get_mock_calendar_events() -> List[Dict[str, any]]:
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    
    events = [
        # Segunda-feira
        {
            "title": "Reunião de Alinhamento Estratégico & OKRs",
            "category": "Trabalho",
            "start": (monday + timedelta(days=0, hours=9, minutes=30)).isoformat(),
            "end": (monday + timedelta(days=0, hours=10, minutes=45)).isoformat(),
            "location": "Google Meet / Sala Principal",
            "description": "Revisão dos entregáveis do trimestre com liderança."
        },
        {
            "title": "Treino Funcional & Corrida",
            "category": "Pessoal",
            "start": (monday + timedelta(days=0, hours=18, minutes=30)).isoformat(),
            "end": (monday + timedelta(days=0, hours=19, minutes=30)).isoformat(),
            "location": "Parque Ibirapuera",
            "description": "Treino de condicionamento físico."
        },
        # Terça-feira
        {
            "title": "Design Review: Nova Arquitetura de Coleções",
            "category": "Trabalho",
            "start": (monday + timedelta(days=1, hours=14, minutes=0)).isoformat(),
            "end": (monday + timedelta(days=1, hours=15, minutes=30)).isoformat(),
            "location": "Escritório Jardins",
            "description": "Apresentação técnica de novos conceitos e protótipos."
        },
        {
            "title": "Leitura & Pesquisa em História da Arte",
            "category": "Pessoal",
            "start": (monday + timedelta(days=1, hours=20, minutes=0)).isoformat(),
            "end": (monday + timedelta(days=1, hours=21, minutes=30)).isoformat(),
            "location": "Biblioteca Pessoal",
            "description": "Capítulos sobre Alta Joalheria do século XX e Art Déco."
        },
        # Quarta-feira
        {
            "title": "Comitê Executivo de Produtos & Lançamentos",
            "category": "Trabalho",
            "start": (monday + timedelta(days=2, hours=10, minutes=0)).isoformat(),
            "end": (monday + timedelta(days=2, hours=11, minutes=30)).isoformat(),
            "location": "Sala de Conferências",
            "description": "Validação de orçamento e cronograma de novidades."
        },
        {
            "title": "Jantar no Bistrô Le Jazz",
            "category": "Pessoal",
            "start": (monday + timedelta(days=2, hours=20, minutes=30)).isoformat(),
            "end": (monday + timedelta(days=2, hours=22, minutes=30)).isoformat(),
            "location": "Pinheiros, São Paulo",
            "description": "Jantar informal com amigos."
        },
        # Quinta-feira
        {
            "title": "Workshop: Tendências Globais de Joalheria & Gemas",
            "category": "Trabalho",
            "start": (monday + timedelta(days=3, hours=15, minutes=0)).isoformat(),
            "end": (monday + timedelta(days=3, hours=17, minutes=0)).isoformat(),
            "location": "Auditório / Webinar",
            "description": "Panorama de lapidações históricas e sustentabilidade na cadeia."
        },
        # Sexta-feira
        {
            "title": "Encerramento Semanal de Sprints & Retrospectiva",
            "category": "Trabalho",
            "start": (monday + timedelta(days=4, hours=16, minutes=0)).isoformat(),
            "end": (monday + timedelta(days=4, hours=17, minutes=0)).isoformat(),
            "location": "Online",
            "description": "Alinhamento das metas atingidas e pendências da semana."
        },
        {
            "title": "Vernissage / Abertura de Exposição no MASP",
            "category": "Pessoal",
            "start": (monday + timedelta(days=4, hours=19, minutes=0)).isoformat(),
            "end": (monday + timedelta(days=4, hours=22, minutes=0)).isoformat(),
            "location": "Avenida Paulista, São Paulo",
            "description": "Visita noturna a retrospectiva artística e coquetel."
        },
        # Sábado
        {
            "title": "Café da Manhã & Feira de Antiguidades do Bixiga",
            "category": "Pessoal",
            "start": (monday + timedelta(days=5, hours=10, minutes=0)).isoformat(),
            "end": (monday + timedelta(days=5, hours=13, minutes=0)).isoformat(),
            "location": "Praça Dom Orione, Bela Vista",
            "description": "Garimpo de peças vintage e passeio a pé."
        },
        # Domingo
        {
            "title": "Almoço no Fasano & Planejamento da Próxima Semana",
            "category": "Pessoal",
            "start": (monday + timedelta(days=6, hours=13, minutes=0)).isoformat(),
            "end": (monday + timedelta(days=6, hours=15, minutes=30)).isoformat(),
            "location": "Jardins, São Paulo",
            "description": "Almoço em família e revisão de prioridades."
        }
    ]
    return events
