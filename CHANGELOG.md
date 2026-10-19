# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue as diretrizes do [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), e adota o [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [2.0.0] - 2026-10-19

### 🚀 Novas Funcionalidades & Arquitetura Editorial Multi-Agente
- **Expansão Editorial para 14 Páginas:** Diagramação refinada inspirada no *The New York Times*, cobrindo Capa, Estratégia, Agenda Semanal, Política Nacional, Mundo, Tech & IA, Op-Ed Cultural, Política Paulista, Economia Nacional, Geopolítica Global, Metrópole SP, Concursos & Ofícios e Caderno de Jogos.
- **Redação Multi-Agente Especializada:**
  - `EditorInChiefAgent`: Coordena o fluxo editorial, unifica o tom de voz e orquestra os agentes setoriais.
  - `AgendaIntelligenceAgent`: Diagnostica a rotina semanal a partir de calendários Google/ICS, detectando picos de sobrecarga e blocos livres para gerar a matéria de capa e cards analíticos diários.
  - `PoliticsWorldAgent` & `WorldGeopoliticsAgent`: Monitoramento geopolítico ao vivo e síntese de bastidores internacionais via feeds RSS confiáveis.
  - `NationalEconomyAgent` & `SpPoliticsAgent`: Análises de conjuntura macroeconômica, política paulistana e cenários eleitorais.
  - `TechAIAgent`: Curadoria de inteligência artificial, computação de ponta e impactos industriais.
  - `AcademicCultureAgent` & `CultureAgent`: Ensaios aprofundados sobre História Geral, História da Alta Joalheria e Alta-Costura.
  - `CareersCraftsAgent`: Mapeamento de ofícios clássicos, ateliês, conservação de acervos e concursos de alto nível.
  - `LifestyleSpAgent`: Gastronomia, passeios e roteiros paulistanos integrados a links diretos no Google Maps.
  - `PuzzleAgent`: Criação de passatempos eruditos a partir do vocabulário da própria edição.
- **Caderno de Jogos Interativo:**
  - **The NYT Crossword:** Algoritmo de palavras cruzadas com entrelaçamento de termos e pistas inteligentes (Horizontais e Verticais).
  - **Caça-Palavras 15x15:** Gerador matricial algorítmico com detecção visual e interatividade em tempo real na versão web.
- **Curadoria Fotográfica & Iconográfica (P&B Alto Contraste):**
  - Módulo `ImageCurator` com download de ilustrações históricas e fotos de agências com tratamento tipográfico clássico em preto e branco.
- **Memória Histórica Anti-Repetição (`.myjournal_memory.json`):**
  - Rastreamento perpétuo de tópicos, restaurantes, ensaios e palavras de jogos para evitar redundâncias entre edições sucessivas.
- **Despacho Automatizado Multi-Canal (`EmailSender`):**
  - Suporte a envio de edições com fallback em cascata: **Google Gmail API** -> **Apple macOS Mail (AppleScript)** -> **Servidor SMTP**.
- **Agendamento no Sistema Operacional (`LaunchAgentScheduler`):**
  - Configuração nativa de agendamento no macOS (`launchd`) para compilação e entrega todo domingo pontualmente às 07:00 da manhã.
- **Edição Web Interativa (`InteractiveWebRenderer`):**
  - Versão digital responsiva com barra de navegação sticky, visualizador de páginas e caça-palavras jogável direto no browser.

### ⚡ Melhorias & Refatorações
- Tipografia premium baseada nas fontes *Cinzel*, *Playfair Display*, *Lora* e *PT Sans*.
- Renderização de PDFs em padrão gráfico editorial de alta resolução via Playwright Chromium.
- Sistema de flags de linha de comando expandido (`--calendar-pessoal`, `--calendar-trabalho`, `--install-schedule`, `--uninstall-schedule`, `--provider`).

---

## [1.0.0] - 2026-10-16

### 📰 Lançamento Inicial
- Estrutura base do projeto e CLI inicial.
- Geração de jornal em 5 páginas com estilo The New York Times.
- Conector Google Calendar inicial e mocks para demonstração sem API.
- Coletor RSS de notícias básicas via Feedparser.
- Renderizador de PDF via Playwright e CSS de colunas jornalísticas.
