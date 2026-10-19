import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from myjournal.config import Config
from myjournal.calendar.client import GoogleCalendarClient
from myjournal.content.news_fetcher import NewsFetcher
from myjournal.content.image_curator import ImageCurator
from myjournal.agents.agenda_agent import AgendaIntelligenceAgent
from myjournal.agents.editor_in_chief import EditorInChiefAgent
from myjournal.renderer.pdf_generator import PDFGenerator
from myjournal.renderer.interactive_web import InteractiveWebRenderer
from myjournal.delivery.mailer import EmailSender
from myjournal.automation.scheduler import LaunchAgentScheduler

def main():
    parser = argparse.ArgumentParser(description="MyJournal AI: Redação Multi-Agente & Jornal Pessoal NYT")
    parser.add_argument("--mock", action="store_true", help="Usa agenda simulada sem exigir credenciais Google")
    parser.add_argument("--provider", choices=["gemini", "openai"], default=None, help="Provedor de IA")
    parser.add_argument("--output", type=str, default=None, help="Caminho do arquivo PDF de saída")
    parser.add_argument("--email", type=str, default=None, help="E-mail de destino do PDF")
    parser.add_argument("--owner", type=str, default=None, help="Nome do leitor/proprietário da edição")
    parser.add_argument("--calendar-pessoal", type=str, default=None, help="URL .ics do calendário pessoal")
    parser.add_argument("--calendar-trabalho", type=str, default=None, help="URL .ics do calendário profissional")
    parser.add_argument("--open", action="store_true", default=True, help="Abre o PDF e a versão web automaticamente")
    parser.add_argument("--no-open", dest="open", action="store_false", help="Não abre automaticamente os arquivos")
    parser.add_argument("--install-schedule", action="store_true", help="Instala agendamento semanal automático no macOS (domingos às 07:00)")
    parser.add_argument("--uninstall-schedule", action="store_true", help="Remove agendamento semanal do macOS")

    args = parser.parse_args()

    if args.owner:
        Config.OWNER_NAME = args.owner
    if args.calendar_pessoal:
        import os
        os.environ["CALENDAR_URL_PESSOAL"] = args.calendar_pessoal
    if args.calendar_trabalho:
        import os
        os.environ["CALENDAR_URL_TRABALHO"] = args.calendar_trabalho

    # Gerenciamento de agendamento no sistema operacional
    if args.install_schedule:
        target_email = args.email or "mhgdidi@gmail.com"
        LaunchAgentScheduler.install(email=target_email)
        return

    if args.uninstall_schedule:
        LaunchAgentScheduler.uninstall()
        return

    today_str = datetime.now().strftime("%Y-%m-%d")
    output_pdf = args.output or str(Config.OUTPUT_DIR / f"journal_{today_str}.pdf")
    output_html = str(Config.OUTPUT_DIR / f"interactive_journal_{today_str}.html")

    print("=" * 68)
    print(" 📰  MYJOURNAL AI v2.0 — REDAÇÃO MULTI-AGENTE EDITORIAL")
    print(f" Data: {datetime.now().strftime('%d/%m/%Y')} | Edição Semanal Personalizada")
    print("=" * 68)

    # 1. Agente de Agenda & Sincronização
    print("\n[1/6] 📅 Agente de Agenda: Diagnosticando compromissos e gerando cards com IA...")
    cal_client = GoogleCalendarClient()
    events = cal_client.get_weekly_events(mock=args.mock)
    agenda_days = AgendaIntelligenceAgent.enrich_schedule(events, provider=args.provider)
    print(f"      ✓ {len(events)} compromissos organizados em {len(agenda_days)} dias com cards inteligentes")

    # 2. Agente de Notícias Globais
    print("\n[2/6] 🌐 Agente News Hunter: Coletando pautas geopolíticas ao vivo (RSS)...")
    raw_news = NewsFetcher.get_weekly_news()
    all_news = raw_news.get("politica", []) + raw_news.get("mundo", []) + raw_news.get("tecnologia", [])
    print(f"      ✓ {len(all_news)} matérias coletadas de fontes jornalísticas oficiais (BBC, G1, NYT)")

    # 3. Redação Multi-Agente & Editor-Chefe com Memória Anti-Repetição
    print("\n[3/6] ✍️  Editor-Chefe: Coordenando pautas inéditas (Moda, Joalheria, SP)...")
    editor = EditorInChiefAgent(provider=args.provider)
    journal_data, word_search, crossword_data = editor.compile_edition(events, all_news, raw_news=raw_news)
    print("      ✓ Curadoria multi-agente e memória histórica atualizadas")

    # 4. Palavras Cruzadas NYT & Caça-Palavras Algorítmico Inédito
    print("\n[4/6] 🧩 Arquiteto de Jogos: Construindo The NYT Crossword & Caça-Palavras...")
    print(f"      ✓ Palavras Cruzadas entrelaçadas com {crossword_data['total_words']} pistas (Horizontais & Verticais)")
    print(f"      ✓ Grade 15x15 de Caça-Palavras com {len(word_search['placed_words'])} palavras exclusivas")

    # 5. Agente Fotográfico & Iconografia Editorial (P&B Alto Contraste)
    print("\n[5/6] 📸 Agente Fotográfico & Iconografia: Coletando fotos reais e gravuras...")
    image_curator = ImageCurator()
    curated_images = image_curator.curate_images(journal_data, all_news)
    print("      ✓ Imagens editoriais curadas com tratamento P&B de alto contraste")

    # 6. Renderização Híbrida: PDF NYT + Web Interativa
    print("\n[6/6] 🖨️  Renderizando Edição Impressa (PDF) e Edição Interativa (Web)...")
    pdf_renderer = PDFGenerator()
    html_print = pdf_renderer.render_html(
        data=journal_data,
        events=events,
        word_search=word_search,
        news_items=all_news,
        crossword=crossword_data,
        images=curated_images,
        agenda_days=agenda_days
    )
    pdf_file = pdf_renderer.generate_pdf(html_print, output_pdf)

    web_renderer = InteractiveWebRenderer()
    pdf_filename = Path(pdf_file).name
    html_file = web_renderer.render_web_edition(
        data=journal_data,
        events=events,
        word_search=word_search,
        pdf_filename=pdf_filename,
        output_path=output_html,
        news_items=all_news,
        crossword=crossword_data,
        images=curated_images,
        agenda_days=agenda_days
    )

    print(f"\n🎉 Edição impressa e interativa geradas com sucesso!")
    print(f"📄 PDF Editorial Dominical (14 páginas): {pdf_file}")
    print(f"🌐 Versão Web Interativa (Jogos jogáveis): {html_file}")

    # Despacho por e-mail se solicitado
    if args.email:
        print(f"\n[E-mail] 📬 Despachando edição para {args.email}...")
        subject = f"📰 {Config.NEWSPAPER_TITLE} — {journal_data.get('metadata', {}).get('date_str', 'Edição Semanal')}"
        body = (
            f"Olá {Config.OWNER_NAME},\n\n"
            f"Sua nova edição semanal do {Config.NEWSPAPER_TITLE} acaba de ser impressa pela sua redação de IA.\n\n"
            f"Destaques da Edição:\n"
            f"• Capa: {journal_data.get('front_page', {}).get('lead_headline', '')}\n"
            f"• Cultura & Joalheria: {journal_data.get('culture_history', {}).get('jewelry_history_article', {}).get('title', '')}\n"
            f"• Ofícios & Oportunidades: Conservação de Acervos, Alta Joalheria e Fatos de Ateliê.\n"
            f"• Gastronomia & Lazer SP: Roteiros culturais, Palavras Cruzadas (NYT) e Caça-Palavras temático.\n\n"
            f"O PDF oficial de 14 páginas está em anexo.\n\n"
            f"Boa leitura e excelente semana!\n"
            f"— MyJournal AI Redação"
        )
        sent = EmailSender.send_via_gmail_api(args.email, subject, body, pdf_file)
        if not sent:
            sent = EmailSender.send_via_macos_mail(args.email, subject, body, pdf_file)
        if not sent:
            sent = EmailSender.send_via_smtp(args.email, subject, body, pdf_file)

    if args.open and sys.platform == "darwin":
        subprocess.run(["open", pdf_file])
        subprocess.run(["open", html_file])

if __name__ == "__main__":
    main()
