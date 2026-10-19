import os
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pathlib import Path
from typing import Optional
from myjournal.config import Config

class EmailSender:
    @staticmethod
    def send_via_smtp(to_email: str, subject: str, body_text: str, pdf_path: str,
                      smtp_host: str = "smtp.gmail.com", smtp_port: int = 587,
                      smtp_user: Optional[str] = None, smtp_pass: Optional[str] = None) -> bool:
        user = smtp_user or os.getenv("SMTP_USER") or os.getenv("GMAIL_USER")
        password = smtp_pass or os.getenv("SMTP_PASSWORD") or os.getenv("GMAIL_APP_PASSWORD")

        if not user or not password:
            print("[Aviso] Credenciais SMTP (SMTP_USER / SMTP_PASSWORD) não encontradas no .env.")
            return False

        msg = MIMEMultipart()
        msg["From"] = f"MyJournal AI <{user}>"
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body_text, "plain", "utf-8"))

        pdf_file = Path(pdf_path)
        if pdf_file.exists():
            with open(pdf_file, "rb") as f:
                attach = MIMEApplication(f.read(), _subtype="pdf")
                attach.add_header("Content-Disposition", "attachment", filename=pdf_file.name)
                msg.attach(attach)

        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(user, password)
            server.send_message(msg)

        print(f"✓ E-mail enviado com sucesso para {to_email} via SMTP!")
        return True

    @staticmethod
    def send_via_gmail_api(to_email: str, subject: str, body_text: str, pdf_path: str, credentials_path: str = None, token_path: str = None) -> bool:
        creds_p = credentials_path or Config.GOOGLE_CREDENTIALS_PATH
        token_p = token_path or Config.GOOGLE_TOKEN_PATH

        if not os.path.exists(token_p):
            print("[Aviso] Token do Google não encontrado para envio via Gmail API.")
            return False

        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build

            creds = Credentials.from_authorized_user_file(token_p)
            service = build("gmail", "v1", credentials=creds)

            msg = MIMEMultipart()
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body_text, "plain", "utf-8"))

            pdf_file = Path(pdf_path)
            if pdf_file.exists():
                with open(pdf_file, "rb") as f:
                    attach = MIMEApplication(f.read(), _subtype="pdf")
                    attach.add_header("Content-Disposition", "attachment", filename=pdf_file.name)
                    msg.attach(attach)

            raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
            service.users().messages().send(userId="me", body={"raw": raw}).execute()
            print(f"✓ E-mail enviado com sucesso para {to_email} via Gmail API!")
            return True
        except Exception as e:
            print(f"[Aviso] Erro no envio via Gmail API: {e}")
            return False

    @staticmethod
    def send_via_macos_mail(to_email: str, subject: str, body_text: str, pdf_path: str) -> bool:
        import subprocess
        import sys
        if sys.platform != "darwin":
            return False

        abs_pdf = str(Path(pdf_path).resolve())
        safe_subject = subject.replace('\\', '\\\\').replace('"', '\\"')
        safe_body = body_text.replace('\\', '\\\\').replace('"', '\\"')
        safe_email = to_email.replace('\\', '\\\\').replace('"', '\\"')

        # Script AppleScript para compor e enviar pelo Mail.app nativo do Mac
        apple_script = f'''
        tell application "Mail"
            set newMessage to make new outgoing message with properties {{subject:"{safe_subject}", content:"{safe_body}\n\n", visible:false}}
            tell newMessage
                make new to recipient at end of to recipients with properties {{address:"{safe_email}"}}
                make new attachment with properties {{file name:"{abs_pdf}" as POSIX file}} at after the last paragraph
                send
            end tell
        end tell
        '''
        try:
            res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"✓ E-mail enviado com sucesso para {to_email} via Apple Mail!")
                return True
            else:
                print(f"[Aviso] Apple Mail retornou erro: {res.stderr.strip()}")
                return False
        except Exception as e:
            print(f"[Aviso] Falha no Apple Mail: {e}")
            return False
