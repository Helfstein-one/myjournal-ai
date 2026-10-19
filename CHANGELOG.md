# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue as diretrizes do [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), e adota o [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [2.2.0] - 2026-10-19

### 🏷️ Rebranding Editorial: MY Personal Journal
- **Atualização do Cabeçalho & Masthead Oficial:**
  - Padronização do nome do jornal para **`MY Personal Journal`** em todas as camadas de configuração, modelos e templates.
  - Atualização dos metadados globais em [config.py](file:///Users/mauriciohelfstein/Downloads/myjournal-ai/myjournal/config.py), `.env.example` e documentação [README.md](file:///Users/mauriciohelfstein/Downloads/myjournal-ai/README.md).
  - Regeneração integral da edição e atualização de todos os assets visuais e screenshots da capa e cadernos internos.

---

## [2.1.0] - 2026-10-19

### 🌐 Expansão de Fontes Oficiais & Imagens Reais (Brasil & Mundo)
- **Ingestão Direta de Fontes de Estado & Diplomáticas:**
  - Integração da **Agência Brasil (EBC)** e da **Agência Câmara** para monitoramento contínuo de atos de Estado, reformas e decretos.
  - Ingestão via API oficial do **IBGE (Instituto Brasileiro de Geografia e Estatística)** para indicadores econômicos, demográficos e sociais em tempo real.
  - Conexão oficial com a **ONU News (Português)** para cobertura multilateral, tratados e resoluções globais.
- **Novas Seções Editoriais Estilo NYT:**
  - **Página 4 (Brasil: Fatos de Estado):** Coluna lateral estilizada com filetes duplos clássicos e datelines em versalete (`BRASÍLIA • Agência Brasil`, `RIO DE JANEIRO • IBGE`).
  - **Página 5 (The World in Brief):** Coluna de despachos rápidos com síntese diplomática (`GENEBRA • ONU News`, `NOVA YORK • Reuters`).
  - **Página 10 (Painel Diplomático & Multilateral):** Seção aprofundada de acordos globais e resoluções da ONU.
- **Motor Fotográfico com Imagens Reais:**
  - `ImageCurator` atualizado para priorizar 100% fotografias autênticas de agências de notícias e do acervo documental de patrimônio histórico da Wikimedia Commons.
  - Tratamento gráfico jornalístico de alto contraste P&B aplicado tanto na edição impressa (PDF) quanto na edição web responsiva.
- **Auditoria Reforçada no Gatekeeper Editorial:**
  - Nova regra de conformidade que audita e valida a proveniência e integridade das pílulas de fatos oficiais antes da liberação da edição.

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
