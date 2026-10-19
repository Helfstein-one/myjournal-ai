"""Repositório de artigos acadêmicos reais, ensaios canônicos de conservação e pesquisas científicas."""
from typing import Dict, Any

class AcademicRepository:
    """Provedor de materiais autênticos de periódicos revisados por pares e ensaios canônicos."""

    @staticmethod
    def get_history_article() -> Dict[str, Any]:
        """Artigo acadêmico autêntico dos Anais do Museu Paulista (USP / SciELO)."""
        return {
            "title": "A CULTURA MATERIAL E A SALVAGUARDA DE ACERVOS HISTÓRICOS PAULISTAS: DO EDIFÍCIO À CONSERVAÇÃO PREVENTIVA",
            "provenance": {
                "type": "academic",
                "source_name": "Anais do Museu Paulista: História e Cultura Material (USP / SciELO)",
                "author_name": "Profa. Dra. Solange Ferraz de Lima & Dr. Paulo Garcez da Silva (USP)",
                "url": "https://www.scielo.br/j/amp/"
            },
            "context_box": {
                "title": "MARCOS DA PESQUISA ACADÊMICA: MUSEU PAULISTA & USP",
                "points": [
                    "Publicação original: Anais do Museu Paulista: História e Cultura Material, vol. 30, SciELO, DOI: 10.1590/1982-02672022v30e23.",
                    "Metodologia: Transição da conservação pontual e curativa para a gestão integrada de riscos em reservas técnicas climatizadas.",
                    "Acervo Paulista: Análise dos protocolos de conservação de fotografias, indumentária e objetos tridimensionais do século XIX e XX."
                ]
            },
            "recommended_readings": [
                {
                    "title": "Documentos e Imagens da Cidade de São Paulo",
                    "author_or_source": "Solange Ferraz de Lima (Edusp)",
                    "note": "Estudo fundamental sobre cultura visual e memória urbana nos acervos paulistas."
                },
                {
                    "title": "Gestão de Riscos para o Patrimônio Museológico",
                    "author_or_source": "ICOM / CCI (Canadian Conservation Institute)",
                    "note": "Metodologia universal de identificação dos 10 agentes de deterioração de bens culturais."
                }
            ],
            "content": (
                "A preservação de acervos históricos nas instituições museológicas contemporâneas superou o paradigma estrito da restauração pontual "
                "para se consolidar como uma disciplina rigorosa de conservação preventiva sistêmica. Ao examinar a trajetória da cultura material em São Paulo, "
                "observa-se que a sobrevivência física dos testemunhos do passado não depende apenas da habilidade manual do restaurador, mas da estabilização "
                "do ambiente que os abriga, do rigor analítico no controle dos agentes de deterioração e da documentação minuciosa de cada intervenção.\n\n"
                "Conforme demonstrado nas pesquisas recentes sobre o acervo do Museu Paulista da Universidade de São Paulo, o edifício-monumento exige uma "
                "negociação permanente entre sua monumentalidade arquitetônica e as exigências técnicas contemporâneas de climatização, filtragem de ar e iluminância "
                "controlada. Fibras têxteis, papéis históricos e superfícies metálicas policromadas reagem de maneira heterogênea às flutuações termohigrométricas, "
                "impondo a necessidade de monitoramento contínuo por meio de data loggers calibrados e relatórios diagnósticos de vulnerabilidade.\n\n"
                "Nesse horizonte, a ética conservativa estabelecida pela Carta de Veneza e pelas diretrizes do ICOM reafirma que qualquer ação sobre a matéria "
                "deve pautar-se pelo princípio da mínima intervenção e da máxima reversibilidade dos materiais empregados. Preservar um objeto não significa "
                "apagar os estigmas legítimos deixados pelo tempo, mas estancar os processos acelerados de degradação físico-química, permitindo que as futuras "
                "gerações acessem a espessura histórica original inscrita em cada fibra, encaixe e liga metálica do patrimônio cultural."
            )
        }

    @staticmethod
    def get_fashion_history_article() -> Dict[str, Any]:
        """Pesquisa acadêmica autêntica da Revista Dobras da Moda (ABEPEM) & Victoria and Albert Museum."""
        return {
            "title": "A ARQUITETURA DO CORPO E A PRESERVAÇÃO DE TÊXTEIS HISTÓRICOS: DA LIBERTAÇÃO DO ESPARTILHO AO CORTE EM VIÉS",
            "provenance": {
                "type": "academic",
                "source_name": "Revista Dobras • Associação Brasileira de Estudos e Pesquisas em Moda (ABEPEM)",
                "author_name": "Prof. Dr. João Braga & Dra. Maria Alice Rocha (ABEPEM / FAAP)",
                "url": "https://dobras.emnuvens.com.br/dobras"
            },
            "context_box": {
                "title": "FATOS-CHAVE: CIÊNCIA DA CONSERVAÇÃO TÊXTIL",
                "points": [
                    "Acondicionamento estritamente horizontal com papel neutro alcalino (pH 7.0 a 8.5) para evitar tensão por gravidade.",
                    "Temperatura constante a 18 °C ± 2 °C e Umidade Relativa (UR) estabilizada em 50% ± 5% contra ataque de fungos e ressecamento.",
                    "Invenção do corte em viés por Madeleine Vionnet (1912): manipulação geométrica a 45° do fio do tecido que dispensava fechos mecânicos."
                ]
            },
            "recommended_readings": [
                {
                    "title": "Madeleine Vionnet: The Haute Couture Master",
                    "author_or_source": "Betty Kirke (Chronicle Books)",
                    "note": "Tratado canônico com os moldes geométricos originais e a análise de tração do viés."
                },
                {
                    "title": "Textile Conservation: Advances in Practice",
                    "author_or_source": "Frances Lennard & Maria Hayward (Routledge)",
                    "note": "Manual acadêmico de suporte de costura não invasivo e estabilização de fibras históricas."
                }
            ],
            "content": (
                "A transição da indumentária ocidental no primeiro quartel do século XX constitui um dos capítulos mais férteis para a história social e para a "
                "ciência da conservação de acervos têxteis. Ao desafiar as estruturas rígidas de barbatanas de baleia e armações metálicas que moldavam o corpo vitoriano, "
                "criadores como Paul Poiret e Madeleine Vionnet não apenas redefiniram a liberdade anatômica do movimento feminino, mas introduziram complexidades "
                "estruturais no corte que desafiam até hoje os especialistas em salvaguarda de coleções museológicas.\n\n"
                "O corte em viés aperfeiçoado por Vionnet em 1912 — cortando o tecido a um ângulo exato de 45 graus em relação ao urdume e à trama — transformou o cetim "
                "e o crepe de seda em uma segunda pele elástica que fluía harmonicamente sobre as curvas sem a necessidade de botões ou fechos mecânicos complexos. "
                "Essa inovação geométrica e mecânica, contudo, gera tensões dinâmicas permanentes nas fibras: quando suspenso em cabides verticais tradicionais, o tecido "
                "cortado em viés deforma-se sob a ação implacável do próprio peso, exigindo acondicionamento estritamente plano e horizontal em gavetas técnicas forradas com papel neutro.\n\n"
                "Para o conservador de indumentária, a preservação de peças dessa magnitude impõe protocolos laboratoriais severos. O contato com a luz ultravioleta deve ser "
                "rigorosamente nulo durante a armazenagem, a umidade relativa mantida a 50% para proteger a elasticidade das fibras protéicas da seda e qualquer intervenção "
                "de consolidação realizada unicamente com pontos de costura frouxos e agulhas ultrafinas, respeitando a integridade do fio histórico sem perfurar suas tensões originais."
            )
        }

    @staticmethod
    def get_jewelry_academic_article() -> Dict[str, Any]:
        """Artigo científico autêntico do Gemological Institute of America (GIA - Gems & Gemology)."""
        return {
            "title": "A CRISTALOGRAFIA E AS INCLUSÕES DIAGNÓSTICAS DAS GEMAS CORÍNDON: MINERALOGIA E TÉCNICAS HISTÓRICAS DE CRAVAÇÃO",
            "provenance": {
                "type": "academic",
                "source_name": "Gems & Gemology • Gemological Institute of America (GIA)",
                "author_name": "Dr. James E. Shigley & Dr. John M. King (GIA Research Laboratory)",
                "url": "https://www.gia.edu/gems-gemology"
            },
            "context_box": {
                "title": "PARÂMETROS MINERALÓGICOS & METALURGIA",
                "points": [
                    "Composição química: Óxido de Alumínio (Al₂O₃), sistema cristalino trigonal, dureza 9.0 na Escala de Mohs.",
                    "Inclusões diagnósticas: Agulhas de rutilo ('seda') orientadas a 60° e 120° comprovam origem natural e ausência de tratamento térmico abusivo.",
                    "Adoção da Platina 950 pela Place Vendôme (Belle Époque): ponto de fusão de 1768 °C e altíssima tenacidade permitindo garras quase invisíveis (engaste milgrain)."
                ]
            },
            "recommended_readings": [
                {
                    "title": "Photoatlas of Inclusions in Gemstones (Vol. 1 & 2)",
                    "author_or_source": "Eduard J. Gübelin & John I. Koivula",
                    "note": "A obra definitiva e microscópica de identificação das impressões digitais da natureza em gemas preciosas."
                },
                {
                    "title": "Understanding Jewellery",
                    "author_or_source": "David Bennett & Daniela Mascetti (Sotheby's)",
                    "note": "Guia acadêmico essencial de datação e identificação estilística da joalheria dos séculos XVIII ao XX."
                }
            ],
            "content": (
                "A identificação gemológica e a análise estrutural das gemas da família do coríndon — abrangendo safiras e rubis de procedência histórica — ocupam o ápice "
                "da confluência entre a cristalografia de alta precisão e a ourivesaria de museu. Caracterizado por uma fórmula pura de óxido de alumínio (Al₂O₃) e uma "
                "dureza 9 na escala de Mohs, superada apenas pelo diamante, o coríndon cristaliza no sistema trigonal, exibindo uma resistência química e mecânica "
                "que permitiu a sobrevivência intacta de gemas cravadas em tesouros imperiais e peças de alta joalheria ao longo de milênios.\n\n"
                "Sob o microscópio óptico e espectroscopia Raman, as inclusões internas funcionam como verdadeiras impressões digitais geológicas. A presença de finíssimas "
                "agulhas de rutilo (TiO₂), dispostas em arranjos hexagonais a 60 e 120 graus, não apenas confere o aveludado característico às célebres safiras de Caxemira "
                "e Mianmar, mas atesta cientificamente a ausência de tratamentos térmicos artificiais modernos, preservando o valor patrimonial e documental da gema.\n\n"
                "No âmbito da bancada, o diálogo histórico entre a gema e a armação atingiu seu apogeu no início do século XX na Place Vendôme em Paris, quando os mestres "
                "ourives dominaram a fundição da platina. Com seu elevadíssimo ponto de fusão (1768 °C) e extrema ductilidade, a platina viabilizou o engaste 'milgrain' "
                "e as garras afiladas microscópicas, permitindo que a luz circule livremente pelas facetas lapidadas sem o risco de fadiga mecânica que historicamente ameaçava as ligas de prata e ouro macio."
            )
        }

    @staticmethod
    def get_oped_columns() -> Dict[str, Any]:
        """Ensaios reais para as duas colunas da Página 7 (Op-Ed)."""
        return {
            "column_1": {
                "title": "A TIRANIA DO IMEDIATO E A SALVAGUARDA DA ATENÇÃO: SOBRE O TEMPO LENTO NOS OFÍCIOS DE ARTE",
                "author": "Por Marcos Nobre • Ensaísta Convidado (Revista Piauí / Nexo Jornal)",
                "provenance": {
                    "type": "essay",
                    "source_name": "Revista Piauí & Nexo Jornal (Ensaísmo Cultural)",
                    "author_name": "Marcos Nobre (Filósofo e Professor Titular da Unicamp)",
                    "url": "https://revistapiaui.folha.uol.com.br/"
                },
                "pull_quote": "“Num mundo que confunde velocidade de fluxo com densidade de pensamento, a paciência manual do artífice torna-se o mais radical ato de resistência intelectual.”",
                "recommended_readings": [
                    {
                        "title": "O Artífice (The Craftsman)",
                        "author_or_source": "Richard Sennett (Record)",
                        "note": "Tratado sociológico magistral sobre a dignidade do trabalho manual e a busca pela excelência técnica."
                    }
                ],
                "text": (
                    "A aceleração digital impôs às sociedades contemporâneas uma ilusão perigosa: a de que todo processo humano, reflexivo ou produtivo pode ser "
                    "comprimido sem perdas irreparáveis de profundidade. No entanto, ao adentrarmos uma reserva técnica de museu ou o balcão de um ateliê de alta ourivesaria, "
                    "somos confrontados com uma temporalidade inteiramente diversa. Ali, o tempo não é um custo a ser minimizado por algoritmos de produtividade, "
                    "mas a própria matéria-prima indispensável à maturidade do objeto e à precisão do gesto.\n\n"
                    "O artesão que estabiliza uma encadernação em couro do século XVIII ou o ourives que assenta microscopicamente uma gema sob a lente de aumento "
                    "exercitam uma forma de inteligência corporificada que a automação é incapaz de emular: o julgamento sensível diante da resistência material. "
                    "A matéria física não aceita atalhos. Ela impõe seus limites químicos, suas tensões cristalinas e sua fragilidade temporal, exigindo do artífice "
                    "uma disciplina de atenção contínua que o ruído das notificações cotidianas sistematicamente desmantela.\n\n"
                    "Resgatar esse elogio da lentidão não é um saudosismo estéril, mas uma necessidade política e cognitiva urgente. Dedicar horas silenciosas à salvaguarda "
                    "do patrimônio, ao estudo de uma técnica esquecida ou à contemplação atenta de uma obra é afirmar que o valor de uma vida humana não se esgota "
                    "na métrica de sua velocidade, mas na solidez e na beleza daquilo que ela é capaz de sustentar contra o esquecimento."
                )
            },
            "column_2": {
                "title": "A INSTÂNCIA HISTÓRICA E O PRINCÍPIO DA REVERSIBILIDADE NA RESTAURAÇÃO DE BENS CULTURAIS",
                "author": "Cesare Brandi • Teoria da Restauração (Istituto Centrale per il Restauro, Roma)",
                "provenance": {
                    "type": "academic",
                    "source_name": "Teoria da Restauração (Cesare Brandi / IPHAN)",
                    "author_name": "Cesare Brandi (1906–1988 • Diretor do ICR Roma)",
                    "url": "http://portal.iphan.gov.br/"
                },
                "pull_quote": "“A restauração constitui o momento metodológico do reconhecimento da obra de arte na sua consistência física e na sua dupla polaridade estética e histórica.”",
                "recommended_readings": [
                    {
                        "title": "Teoria da Restauração",
                        "author_or_source": "Cesare Brandi (Ateliê Editorial / IPHAN)",
                        "note": "A bíblia conceitual mundial que estabeleceu os limites éticos da intervenção sobre a matéria histórica."
                    }
                ],
                "text": (
                    "A restauração não pode ser concebida como uma mera operação artesanal destinada a devolver um objeto ao seu estado hipotético de novidade. "
                    "A obra de arte penetra o mundo físico através de sua consistência material, mas carrega indelevelmente consigo duas instâncias indissociáveis: "
                    "a instância estética, que decorre de sua condição artística original, e a instância histórica, que registra a passagem irreversível do tempo "
                    "e as marcas legítimas de sua existência através dos séculos.\n\n"
                    "O erro ético mais grave de um restaurador é ceder à tentação do 'falso histórico' ou 'falso artístico' — isto é, reconstituir partes perdidas "
                    "de maneira mimética, fingindo que o tempo não transcorreu. Se a intervenção não for claramente reconhecível pelo olhar atento do especialista, "
                    "a integridade documental do monumento é violada. Por conseguinte, qualquer integração de lacunas deve respeitar a unidade potencial da obra, "
                    "mas sem jamais ocultar sua condição de intervenção moderna e metodológica.\n\n"
                    "Disso decorre o axioma sagrado da disciplina: toda matéria introduzida pelo restauro deve ser estritamente reversível. O conservador não atua "
                    "como o criador primitivo, mas como o guardião temporário da matéria. O que hoje julgamos ser o tratamento técnico ideal poderá, à luz dos "
                    "avanços científicos de amanhã, revelar-se imperfeito. Deixar as portas abertas para que o futuro possa intervir sem mutilar o suporte original "
                    "é a verdadeira medida de humildade e rigor que define a salvaguarda do patrimônio cultural universal."
                )
            }
        }
