from datetime import datetime
from typing import Dict, Any

def get_mock_journal_content(owner_name: str = "Mauricio") -> Dict[str, Any]:
    today = datetime.now()
    week_str = f"Semana de {today.strftime('%d de %B de %Y')}"
    
    from myjournal.config import Config
    return {
        "metadata": {
            "title": Config.NEWSPAPER_TITLE,
            "subtitle": "Edição Semanal Dedicada ao Conhecimento, Cultura e Planejamento",
            "date_str": today.strftime("%A, %d de %B de %Y").capitalize(),
            "volume": "VOL. CLXXV... No. 60.420",
            "edition": "EDIÇÃO PAULISTANA",
            "weather": "São Paulo: 22°C, Parcialmente Nublado | Vento: 12 km/h SE",
            "quote": "“A elegância não consiste em pôr um vestido novo, mas na proporção entre o tempo, o espaço e a intenção.” — Coco Chanel"
        },
        "front_page": {
            "lead_headline": f"O EQUILÍBRIO METROPOLITANO: A SEMANA DE {owner_name.upper()}",
            "lead_subdeck": "Entre alinhamentos executivos de design, imersões históricas e a pulsação urbana dos Jardins, os próximos sete dias exigem disciplina e discernimento.",
            "lead_article": (
                f"Ao adentrar mais uma semana de outono em São Paulo, a rotina de {owner_name} desenha-se "
                "sob o signo da precisão. As jornadas corporativas — ancoradas no refinamento de novas arquiteturas de produto "
                "e no comitê estratégico — dialogam diretamente com intervalos dedicados ao cultivo estético e ao bem-estar pessoal.\n\n"
                "A cadência dos dias revela uma distribuição harmoniosa: as manhãs de rigor e tomada de decisão corporativa "
                "encontram contraponto nas noites de pesquisa bibliográfica e nos jantares intimistas no eixo Pinheiros-Jardins. "
                "Mais do que uma simples sucessão de compromissos cronológicos, a semana convida a um estado de atenção plena: "
                "a arte de conciliar a densidade do trabalho técnico com o deleite intelectual da história e das artes."
            ),
            "itinerary_summary": (
                "Cinco blocos estratégicos corporativos concentrados na primeira metade da semana; "
                "três sessões de condicionamento e pesquisa pessoal; e um fim de semana orientado à alta gastronomia e artes visuais."
            )
        },
        "politics_world": {
            "headline": "A RECONFIGURAÇÃO DA ORDEM GEOPOLÍTICA E OS RUMOS INSTITUCIONAIS",
            "subdeck": "Análise sobre as tensões diplomáticas multilaterais e os reflexos econômicos no mercado emergente.",
            "main_article": (
                "O cenário internacional atravessa um dos períodos de maior complexidade conceitual das últimas décadas. "
                "O enfraquecimento de alianças tradicionais e a ascensão de novas matrizes energéticas impõem aos líderes "
                "globais um exercício contínuo de pragmatismo. Nos corredores de Genebra e Washington, diplomatas debatem "
                "a transição das cadeias globais de suprimento para polos de proximidade geográfica — o chamado 'nearshoring'.\n\n"
                "No plano doméstico, o debate sobre sustentabilidade fiscal e incentivo à inovação de ponta ganha contornos "
                "decisivos no Congresso. Especialistas apontam que a estabilidade de médio prazo dependerá não apenas de ajustes "
                "contábeis, mas da capacidade do país de consolidar marcos regulatórios transparentes para atração de capitais privados "
                "em setores de alta tecnologia e manufatura avançada."
            ),
            "provenance": {
                "type": "news",
                "source_name": "BBC News Brasil • Geopolítica",
                "author_name": "Correspondência Internacional",
                "url": "https://www.bbc.com/portuguese"
            },
            "context_box": {
                "title": "PARA ENTENDER MELHOR: CENÁRIO INSTITUCIONAL",
                "points": [
                    "Reconfiguração acelerada das rotas industriais estratégicas em direção a polos ocidentais.",
                    "Negociações orçamentárias prioritárias com foco em transição climática e equilíbrio fiscal.",
                    "Projeção de volatilidade nos mercados cambiais diante de reuniões de bancos centrais."
                ]
            },
            "recommended_readings": [
                {"title": "Ordem Mundial e Geopolítica Contemporânea", "author_or_source": "Henry Kissinger", "note": "Clássico sobre o equilíbrio de poder entre potências."},
                {"title": "Relatório Econômico Global 2026", "author_or_source": "FMI / Banco Mundial", "note": "Diagnóstico estrutural das cadeias produtivas."}
            ],
            "briefs": [
                {
                    "title": "Diplomacia & Comércio Exterior",
                    "text": "Negociações bilaterais de acordos tarifários sinalizam avanço para produtos de alto valor agregado na América Latina."
                },
                {
                    "title": "Transição Energética",
                    "text": "Cúpula internacional reafirma investimentos recordes em matrizes renováveis e descarbonização industrial."
                },
                {
                    "title": "Mercados & Juros",
                    "text": "Bancos centrais adotam cautela diante da resiliência dos índices de inflação em economias desenvolvidas."
                }
            ]
        },
        "tech_ai": {
            "headline": "A FRONTEIRA DOS SISTEMAS AUTÔNOMOS: ENGENHARIA DE DADOS E RACIOCÍNIO AGÊNTICO",
            "byline": f"Por {owner_name} & Redação de Tecnologia",
            "provenance": {
                "type": "ai_editorial",
                "source_name": "Redação MyJournal AI",
                "author_name": "Gemini 3.8 Flash • Curadoria Editorial",
                "url": ""
            },
            "context_box": {
                "title": "PARA ENTENDER MELHOR: SISTEMAS AGÊNTICOS",
                "points": [
                    "Evolução de modelos passivos de chat para orquestração de ferramentas e chamadas de API em tempo real.",
                    "Redução de alucinação mediante verificação e recuperação semântica sobre bases documentais fechadas.",
                    "Importância da governança de dados e auditoria em ambientes corporativos críticos."
                ]
            },
            "recommended_readings": [
                {"title": "Designing Data-Intensive Applications", "author_or_source": "Martin Kleppmann", "note": "Fundamentos de arquitetura de dados confiáveis e escaláveis."},
                {"title": "ReAct: Synergizing Reasoning and Acting in Language Models", "author_or_source": "Google Research & Princeton", "note": "Artigo pioneiro sobre raciocínio agêntico."}
            ],
            "article": (
                "A maturidade da inteligência artificial generativa deslocou o foco dos modelos fundacionais genéricos para as arquiteturas "
                "agênticas e a curadoria de dados de alta precisão. Empresas líderes compreendem que a soberania algorítmica não reside apenas "
                "na capacidade computacional bruta, mas na orquestração semântica de fluxos distribuídos.\n\n"
                "Ao integrar motores de inferência local com ferramentas corporativas em tempo real, os novos sistemas abandonam o papel passivo "
                "de 'chatbots' e assumem a governança ativa de processos: da auditoria de pipelines ao planejamento estratégico. A fronteira técnica "
                "atual exige dos engenheiros de dados uma síntese rigorosa entre modelagem matemática, arquitetura de latência ultrabaixa e discernimento ético."
            )
        },
        "oped": {
            "column_1": {
                "title": "O Elogio da Lentidão Consciente no Ritmo Metropolitano",
                "author": f"Por {owner_name}",
                "provenance": {
                    "type": "author_column",
                    "source_name": "MY Journal",
                    "author_name": f"{owner_name}",
                    "url": ""
                },
                "pull_quote": "“A velocidade é a forma de êxtase que a revolução técnica ofereceu ao homem moderno, mas o discernimento exige pausas deliberadas.”",
                "recommended_readings": [
                    {"title": "A Sociedade do Cansaço", "author_or_source": "Byung-Chul Han", "note": "Ensaio incisivo sobre hiperatividade, produtividade e a arte da pausa contemplativa."}
                ],
                "text": (
                    "Em uma megalópole caracterizada pela vertigem de compromissos simultâneos, a disciplina do tempo torna-se o mais raro dos luxos. "
                    "Dedicar manhãs ao rigor do ofício e noites ao cultivo intelectual não representa uma fuga do real, "
                    "mas a afirmação consciente de que o intelecto prospera nos contrastes deliberados. A mente que não reserva clareiras de contemplação "
                    "acaba por capitular diante do ruído contínuo."
                )
            },
            "column_2": {
                "title": "A Permanência da Forma: Da Alta Costura à Lapidação",
                "author": "Do Conselho Editorial",
                "provenance": {
                    "type": "ai_editorial",
                    "source_name": "Conselho Editorial",
                    "author_name": "Redação MyJournal AI • Gemini 3.8 Flash",
                    "url": ""
                },
                "pull_quote": "“A verdadeira elegância transcende as estações: ela reside na exatidão da proporção e no respeito à nobreza da matéria.”",
                "recommended_readings": [
                    {"title": "Teoria do Restauro", "author_or_source": "Cesare Brandi", "note": "A bíblia conceitual sobre a salvaguarda e mínima intervenção na matéria histórica."}
                ],
                "text": (
                    "Observar um diamante antigo lapidado em Golconda ou o corte desestruturado de uma casaca de alta costura é contemplar a vitória "
                    "do artífice sobre o efêmero. O século XXI, ávido por descartabilidade, redescobre nos ateliês históricos a lição fundamental: "
                    "nada daquilo que é executado com mestria e paciência sucumbe ao julgamento das décadas."
                )
            }
        },
        "sp_politics": {
            "headline": "GESTÃO PÚBLICA PAULISTA: INVESTIMENTOS ESTRUTURAIS, ORÇAMENTO E ARTICULAÇÃO NA ALESP",
            "byline": "Por Correspondente de Política Estadual & Alesp",
            "provenance": {
                "type": "news",
                "source_name": "Assembleia Legislativa do Estado de SP & Governo de SP",
                "author_name": "Agência de Notícias da Alesp",
                "url": "https://www.al.sp.gov.br/noticias/"
            },
            "context_box": {
                "title": "PANORAMA DO PODER EM SÃO PAULO",
                "points": [
                    "Tramitação de projetos prioritários de infraestrutura e concessões públicas na Alesp.",
                    "Articulação entre o Palácio dos Bandeirantes e a Prefeitura de SP em mobilidade e segurança.",
                    "Planejamento orçamentário e metas de responsabilidade fiscal do Estado de São Paulo."
                ]
            },
            "recommended_readings": [
                {"title": "História Política do Estado de São Paulo", "author_or_source": "Boris Fausto", "note": "Fundamentos da administração e da formação institucional paulista."},
                {"title": "Políticas Públicas e Gestão Metropolitana", "author_or_source": "Fundação Seade / Edusp", "note": "Diagnóstico socioeconômico e infraestrutura de São Paulo."}
            ],
            "article": (
                "A agenda do Executivo estadual e as deliberações no plenário da Assembleia Legislativa do Estado de São Paulo (Alesp) convergem em torno "
                "do planejamento orçamentário e da ampliação de concessões em infraestrutura e mobilidade urbana na Região Metropolitana.\n\n"
                "Projetos prioritários de modernização das linhas metroferroviárias da CPTM e do Metrô, além de parcerias público-privadas voltadas à extensão "
                "de corredores rodoviários, dominam os debates entre as lideranças partidárias e as comissões temáticas de finanças e transportes.\n\n"
                "No âmbito municipal paulistano, a coordenação com a Prefeitura de São Paulo intensifica intervenções em zeladoria urbana, contenção de encostas "
                "e revitalização do Centro Histórico, buscando equilibrar investimentos sociais com a responsabilidade fiscal do município."
            )
        },
        "national_economy": {
            "headline": "MACROECONOMIA BRASILEIRA: POLÍTICA MONETÁRIA, METAS DE INFLAÇÃO E ATIVIDADE PRODUTIVA",
            "byline": "Por Redação de Economia e Finanças",
            "provenance": {
                "type": "news",
                "source_name": "Agência Brasil / EBC (Economia e Negócios)",
                "author_name": "Redação de Indicadores Macroeconômicos em Brasília",
                "url": "https://agenciabrasil.ebc.com.br/economia"
            },
            "context_box": {
                "title": "INDICADORES MACROECONÔMICOS & CENÁRIO",
                "points": [
                    "Decisões do Banco Central sobre a taxa básica Selic e convergência da inflação oficial (IPCA).",
                    "Desempenho da massa salarial real e do emprego formal monitorados pelo IBGE e Caged.",
                    "Avanço da regulamentação tributária e seus impactos sobre competitividade industrial."
                ]
            },
            "recommended_readings": [
                {"title": "Economia Brasileira Contemporânea", "author_or_source": "Fabio Giambiagi et al.", "note": "Análise aprofundada dos ciclos econômicos e planos de estabilização."},
                {"title": "Princípios de Economia Monetária", "author_or_source": "Mishkin", "note": "Mecanismos de transmissão da política monetária e inflação."}
            ],
            "article": (
                "O Comitê de Política Monetária (Copom) do Banco Central e as projeções do Boletim Focus sinalizam a condução cautelosa das taxas de juros, "
                "buscando consolidar o processo de desinflação dos serviços e ancorar as expectativas para o horizonte relevante de política monetária.\n\n"
                "A resiliência do mercado de trabalho formal, acompanhada por índices consistentes de geração de empregos com carteira assinada pelo Caged "
                "e pela taxa de desocupação medida pela Pnad Contínua do IBGE, impulsiona a massa salarial real e sustenta o consumo das famílias.\n\n"
                "No plano produtivo, os setores do agronegócio exportador e da indústria de transformação ajustam seus estoques diante dos custos de financiamento, "
                "enquanto a regulamentação da reforma tributária sobre o consumo promete simplificar os regimes fiscais e elevar a produtividade agregada."
            )
        },
        "world_geopolitics": {
            "headline": "A RECONFIGURAÇÃO DA ORDEM GLOBAL: MULTIPOLARIDADE, ALIANÇAS E SEGURANÇA INTERNACIONAL",
            "byline": "Por Correspondência Internacional",
            "provenance": {
                "type": "news",
                "source_name": "BBC News Internacional • Análise Geopolítica",
                "author_name": "Redação de Relações Internacionais & Diplomacia",
                "url": "https://www.bbc.com/portuguese/topics/c7zp57yyz21t"
            },
            "context_box": {
                "title": "RADAR ESTRATÉGICO INTERNACIONAL",
                "points": [
                    "Realinhamento geopolítico e fortalecimento de alianças multilaterais de defesa.",
                    "Segurança das rotas comerciais globais e soberania tecnológica de semicondutores.",
                    "Diplomacia climática e transição energética como vetores de cooperação internacional."
                ]
            },
            "recommended_readings": [
                {"title": "A Ordem Mundial", "author_or_source": "Henry Kissinger", "note": "Reflexão sobre os equilíbrios históricos de poder e a estabilidade das civilizações."},
                {"title": "O Choque de Civilizações", "author_or_source": "Samuel P. Huntington", "note": "Análise das fraturas culturais e dos novos blocos geopolíticos globais."}
            ],
            "article": (
                "A dinâmica do sistema internacional atravessa um período de intensas transformações estruturais, caracterizado pela transição de uma ordem "
                "hegemônica para um arranjo multipolar fragmentado, onde alianças regionais e blocos econômicos redefinem os eixos de poder.\n\n"
                "As disputas estratégicas em torno de rotas comerciais, cadeias de suprimentos de minerais críticos e semicondutores sofisticados colocam "
                "as superpotências em permanente tensão, redefinindo as doutrinas de defesa mútua na Otan e ampliando o peso de articulações no Sul Global.\n\n"
                "Nas mesas de negociação multilateral da ONU e das cúpulas de segurança, os esforços diplomáticos concentram-se na contenção de escaladas armadas "
                "e na preservação de acordos de não proliferação nuclear, em um ambiente de desconfiança mútua sem precedentes desde a Guerra Fria."
            )
        },
        "culture_history": {
            "history_article": {
                "title": "A Geometria do Século: O Legado do Art Déco na Arquitetura Moderna",
                "provenance": {
                    "type": "ai_editorial",
                    "source_name": "Caderno de História & Civilizações",
                    "author_name": "Redação MyJournal AI • Gemini 3.8 Flash",
                    "url": ""
                },
                "context_box": {
                    "title": "FATOS-CHAVE: LINHAS DO TEMPO",
                    "points": [
                        "1925: Exposição Internacional de Artes Decorativas de Paris consolida o vocabulário formal do estilo.",
                        "Uso vanguardista de novos materiais industriais: cromo, baquelite, concreto armado e vidros prismáticos.",
                        "São Paulo: Edifício Martinelli, Banespa e Viaduto do Chá incorporam elementos ornamentais geométricos."
                    ]
                },
                "recommended_readings": [
                    {"title": "Art Deco: The Golden Age of Graphic Art", "author_or_source": "Alastair Duncan", "note": "Estudo aprofundado das matrizes estéticas dos anos 1920."}
                ],
                "content": (
                    "Nascido entre os escombros da Primeira Guerra e consagrado na célebre Exposição Internacional de Artes Decorativas de Paris em 1925, "
                    "o Art Déco não foi apenas um movimento estético, mas a expressão máxima da velocidade, da industrialização e do otimismo moderno. "
                    "Caracterizado por linhas puras, simetria geométrica, zigurates e o uso suntuoso de materiais como cromo, laca e ébano, o estilo "
                    "revolucionou a paisagem urbana de Nova York a São Paulo, deixando marcas indeléveis em edifícios icônicos que até hoje desafiam a passagem do tempo."
                )
            },
            "fashion_history_article": {
                "title": "A Revolução do Alfaiate: Como Paul Poiret e Vionnet Libertaram a Silhueta Feminina",
                "provenance": {
                    "type": "ai_editorial",
                    "source_name": "Caderno de Alta Costura",
                    "author_name": "Redação MyJournal AI • Gemini 3.8 Flash",
                    "url": ""
                },
                "context_box": {
                    "title": "FATOS-CHAVE: REVOLUÇÃO DO CORTE",
                    "points": [
                        "Abandono do espartilho rígido em favor do drapeado grego e da fluidez oriental.",
                        "Invenção do 'corte em viés' por Madeleine Vionnet em 1912, dispensando fechos mecânicos.",
                        "Conservação têxtil: desafios modernos de armazenamento com temperatura e umidade controladas a 18 °C e 50% UR."
                    ]
                },
                "recommended_readings": [
                    {"title": "Vionnet: The Haute Couture Master", "author_or_source": "Betty Kirke", "note": "Tratado com diagramas originais de corte e modelagem em viés."}
                ],
                "content": (
                    "Antes mesmo da consagração modernista de Chanel, o início do século XX testemunhou a ruptura definitiva com o espartilho rígido. "
                    "Paul Poiret introduziu drapeados fluidos inspirados no orientalismo, enquanto Madeleine Vionnet refinou o lendário 'corte em viés', "
                    "permitindo que o tecido desenhasse a anatomia sem restringir o movimento. Essa transformação não foi mero capricho de ateliê, "
                    "mas o reflexo direto da emancipação feminina e da entrada das mulheres no espaço público urbano."
                )
            },
            "jewelry_history_article": {
                "title": "O Mistério das Lapidações Antigas: Da Mina de Golconda às Platinas Eduardianas",
                "provenance": {
                    "type": "ai_editorial",
                    "source_name": "Caderno de Alta Joalheria",
                    "author_name": "Redação MyJournal AI • Gemini 3.8 Flash",
                    "url": ""
                },
                "context_box": {
                    "title": "FATOS-CHAVE: MINERALOGIA & LIGAS",
                    "points": [
                        "Minas de Golconda (Índia): fonte dos diamantes mais puros e límpidos (tipo IIa) da história.",
                        "Old Mine Cut: corte característico com cúpula alta, mesa pequena e facetas amplas que cintilavam à luz de velas.",
                        "Platina na Era Eduardiana: permitiu engastes 'mille-grains' ultrafinos com resistência estrutural inigualável."
                    ]
                },
                "recommended_readings": [
                    {"title": "Understanding Jewellery", "author_or_source": "David Bennett & Daniela Mascetti", "note": "Guia definitivo de identificação de joias dos séculos XIX e XX."}
                ],
                "content": (
                    "Na alta joalheria, a evolução das ferramentas mecânicas redefiniu a relação humana com a luz. Os lendários diamantes de Golconda, "
                    "lapidados originalmente em Old Mine Cut, valorizavam a profundidade e o brilho sob a luz de velas. Com a virada para a Era Eduardiana "
                    "e a incorporação da platina — metal de extrema tenacidade que permitia engastes quase invisíveis —, os mestres joalheiros da Place Vendôme "
                    "puderam erguer rendas metálicas onde as gemas pareciam levitar no colo da aristocracia."
                )
            },
            "courses": [
                {
                    "title": "História da Alta Joalheria & Gemologia Aplicada",
                    "institution": "L'ÉCOLE, School of Jewelry Arts (Paris / Online)",
                    "description": "Estudo aprofundado sobre a evolução das grandes casas de joalheria europeias e identificação de técnicas históricas de engaste."
                },
                {
                    "title": "História Social da Moda & Indumentária",
                    "institution": "Coursera & Institut Français de la Mode",
                    "description": "A moda como documento histórico e espelho das transformações econômicas do século XIX ao contemporâneo."
                },
                {
                    "title": "Arquitetura e Patrimônio Histórico Paulista",
                    "institution": "FAU-USP / Extensão Universitária",
                    "description": "Análise dos ciclos do café, modernismo e preservação do acervo arquitetônico da capital paulista."
                }
            ]
        },
        "lifestyle_sp": {
            "section_title": "METRÓPOLE & ESTILO: O GUIA PAULISTANO EXPANDIDO",
            "section_intro": "Uma seleção curada de 6 experiências gastronômicas de alta precisão e 4 roteiros culturais e arquitetônicos pela capital.",
            "gastronomy": [
                {
                    "name": "Coffee Lab & Torrefação",
                    "neighborhood": "Vila Madalena",
                    "type": "Cafés Especiais & Bancada",
                    "highlight": "Laboratório pioneiro de cafés especiais com métodos rituais de extração e grãos microlote.",
                    "dish": "Ritual de degustação comparativa & Bolo de polenta com alecrim",
                    "hours": "Terça a Domingo, 9h às 18h",
                    "ambience": "Balcão sensorial e mesas ao ar livre."
                },
                {
                    "name": "Bistrô Charlô & Bar",
                    "neighborhood": "Jardins",
                    "type": "Cozinha Clássica Franco-Brasileira",
                    "highlight": "Clássico atemporal da culinária franco-brasileira. Salão refinado com serviço de excelência.",
                    "dish": "Pato confitado com batatas sarladaises e redução de vinho",
                    "hours": "Almoço e Jantar, 12h às 23h",
                    "ambience": "Salão intimista com serviço à francesa de padrão histórico."
                },
                {
                    "name": "Fasano Gastronomia",
                    "neighborhood": "Jardins",
                    "type": "Alta Gastronomia Italiana",
                    "highlight": "O ápice da elegância e precisão técnica em massas e risotos clássicos na cidade.",
                    "dish": "Tortelli de vitelo com molho de cogumelos porcini frescos",
                    "hours": "Jantar, 19h30 à meia-noite",
                    "ambience": "Iluminação amena, piano suave e serviço de luva branca."
                },
                {
                    "name": "Boca de Ouro Bar",
                    "neighborhood": "Pinheiros",
                    "type": "Coquetelaria Autoral & Balcão",
                    "highlight": "Balcão em curva de madeira escura com coquetelaria precisa e sem afetações.",
                    "dish": "Macunaíma (cachaça, Fernet e limão) & Bolovo perfeito",
                    "hours": "Segunda a Sábado, 18h à 1h",
                    "ambience": "Iluminação baixa e vinis no som."
                },
                {
                    "name": "Fabrique Pão e Café",
                    "neighborhood": "Higienópolis",
                    "type": "Fermentação Natural & Brunch",
                    "highlight": "Pães rústicos de crosta estaladiça elaborados com farinhas francesas e fermentação de 36 horas.",
                    "dish": "Croissant folhado amanteigado & Toast de figo com queijo de cabra",
                    "hours": "Diariamente, 7h às 20h",
                    "ambience": "Tijolos ingleses, aroma de fornada quente e café fresco."
                },
                {
                    "name": "Cantina Roperto & Empório",
                    "neighborhood": "Bixiga",
                    "type": "Tradição Centenária da Imigração",
                    "highlight": "Fundada em 1942, conserva os segredos das massas artesanais da Calábria no coração do Bixiga.",
                    "dish": "Fusilli artesanal ao molho de calabresa curada",
                    "hours": "Almoço de domingo, 11h30 às 17h",
                    "ambience": "Garrafões de vinho no teto e hospitalidade calorosa."
                }
            ],
            "walks": [
                {
                    "title": "Museu da Imigração & Acervo Histórico",
                    "institution": "Mooca",
                    "itinerary": "Visita ao conjunto edificado da antiga Hospedaria do Brás, jardins históricos e salas de salvaguarda documental.",
                    "tip": "Caminhe pelo jardim das figueiras centenárias e consulte o acervo digital de matrículas dos ateliês e ofícios históricos.",
                    "hours": "Terça a Domingo, 9h às 18h"
                },
                {
                    "title": "Circuito Art Déco e Modernismo no Centro Histórico",
                    "institution": "Centro Histórico",
                    "itinerary": "Edifício Altino Arantes (Farol Santander), Edifício Martinelli e Mosteiro de São Bento.",
                    "tip": "Faça a caminhada no início da manhã de sábado, observando os relevos ornamentais em bronze e granito dos pórticos dos anos 1930.",
                    "hours": "Sábado matutino"
                },
                {
                    "title": "Tarde Cultural entre a Pinacoteca e o Jardim da Luz",
                    "institution": "Luz",
                    "itinerary": "Pinacoteca de São Paulo, Pina Contemporânea e Café do Parque.",
                    "tip": "Aprecie o contraste arquitetônico entre os tijolos aparentes de Ramos de Azevedo e o projeto arrojado de Paulo Mendes da Rocha.",
                    "hours": "Quarta a Segunda, 10h às 18h"
                },
                {
                    "title": "Caminhada sob as Marquises do Parque Ibirapuera",
                    "institution": "Ibirapuera",
                    "itinerary": "Circuito que conecta a Marquise de Niemeyer, Museu Afro Brasil e o Pavilhão da Bienal.",
                    "tip": "Melhor horário no fim da tarde para acompanhar a luz poente sobre as curvas do concreto armado modernista.",
                    "hours": "Aberto diariamente das 5h às 23h"
                }
            ]
        },
        "crafts_careers": {
            "section_title": "OFÍCIOS DE BANCADA, RESTAURO & OPORTUNIDADES",
            "section_subdeck": "Panorama de ateliês de restauração de acervos, alta ourivesaria, gemologia e oportunidades profissionais selecionadas.",
            "opportunities": [
                {
                    "role": "Conservador-Restaurador de Bens Móveis e Metais",
                    "institution": "Laboratório de Preservação & Museus de Arte",
                    "scope": "Trabalho técnico em conservação preventiva e curativa de ligas históricas, prataria e acervos sacros.",
                    "requirements": "Formação em Conservação e Restauro, química de materiais e técnicas de estabilização.",
                    "link": "https://www.google.com/search?q=vagas+conservador+restaurador+bens+moveis+metais+sao+paulo",
                    "link_label": "Ver Vagas & Editais de Restauro →"
                },
                {
                    "role": "Ourives de Bancada & Montador de Alta Joalheria",
                    "institution": "Ateliês de Alta Ourivesaria & Alta Joalheria",
                    "scope": "Confecção manual de estruturas em ouro 18k e platina, solda de alta precisão e acabamentos de luxo.",
                    "requirements": "Experiência sólida em bancada, limagem, calibração milimétrica e leitura de croquis técnicos.",
                    "link": "https://www.linkedin.com/jobs/search/?keywords=ourives%20bancada",
                    "link_label": "Buscar Vagas de Ourivesaria no LinkedIn →"
                },
                {
                    "role": "Cravador de Pedras Preciosas & Perito Gemólogo",
                    "institution": "Casas de Alta Gemologia & Joalherias Finas",
                    "scope": "Cravação refinada (pavê, grifas, trilho) em esmeraldas, rubis e diamantes com microscópio ótico.",
                    "requirements": "Domínio de buril pneumático, conhecimento gemológico de dureza e clivagem.",
                    "link": "https://www.linkedin.com/jobs/search/?keywords=gemologia%20cravador",
                    "link_label": "Consultar Vagas de Cravador & Gemologia →"
                }
            ],
            "curiosities": [
                {
                    "title": "Ouro Púrpura & Ligas Raras",
                    "text": "A combinação intermetálica de ouro puro (79%) com alumínio (21%) cria o ouro púrpura (AuAl2). Por ser quebradiço para forja tradicional de anéis, é lapidado como uma gema preciosa metálica em peças exclusivas de alta joalheria."
                },
                {
                    "title": "O Ácido Tartárico e o Restauro Histórico",
                    "text": "No restauro de bronzes e pratarias antigas, o uso de ácido tartárico natural derivado de borras de vinho é um dos métodos mais gentis e eficazes para remover sulfetos sem agredir a pátina original do metal."
                },
                {
                    "title": "O Segredo Policromático de Fabergé",
                    "text": "Peter Carl Fabergé conseguia até sete tonalidades distintas de ouro em um único ovo imperial manipulando proporções exatas de cobre (vermelho), prata (verde), ferro (cinza) e níquel (branco), técnica que exigia controle térmico artesanal sem pirômetros eletrônicos."
                },
                {
                    "title": "Pleocroísmo: As Gemas Camaleônicas",
                    "text": "A alexandrita e a tanzanita absorvem a luz de maneira tão desigual através de seus eixos cristalográficos que exibem cores completamente distintas: verde esmeralda à luz solar e vermelho rubi sob luz incandescente."
                }
            ]
        },
        "crossword": {
            "title": "THE NEW YORK TIMES CROSSWORD • EDIÇÃO DOMINICAL",
            "instructions": "Preencha a grade entrelaçada utilizando as pistas culturais, históricas e pessoais da presente edição.",
            "clues": [
                {"word": "VENDOME", "clue": "Célebre praça parisiense epicentro da alta joalheria mundial"},
                {"word": "ARTDECO", "clue": "Estilo geométrico dos anos 1920 que uniu luxo e modernidade"},
                {"word": "PLATINA", "clue": "Metal nobre e denso indispensável aos engastes da Belle Époque"},
                {"word": "PIANO", "clue": "Instrumento harmônico de teclas estudado na rotina semanal"},
                {"word": "ORACLE", "clue": "Gigante tecnológica anfitriã do encontro de inteligência artificial"},
                {"word": "ALFAIATE", "clue": "Mestre artífice da estrutura do corte de trajes"}
            ]
        },
        "games_diversions": {
            "title": "DIVERSÕES DA MENTE: CAÇA-PALAVRAS DA SEMANA",
            "instructions": "Encontre as palavras temáticas escondidas na grade. Elas refletem seus compromissos, as reflexões históricas e as artes da presente edição.",
            "words_to_find": [
                "JOALHERIA", "PLATINA", "ARTDECO", "ALFAIATARIA",
                "ESTRATEGIA", "PINHEIROS", "IBIRAPUERA", "VIONNET",
                "GOLCONDA", "EDITORIAL", "PRECISAO", "HISTORIA"
            ]
        }
    }
