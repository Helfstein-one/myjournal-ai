import os
import subprocess
import sys
from pathlib import Path
from myjournal.config import Config

LAUNCH_AGENT_LABEL = "com.myjournal.weekly"
PLIST_PATH = Path.home() / "Library" / "LaunchAgents" / f"{LAUNCH_AGENT_LABEL}.plist"

class LaunchAgentScheduler:
    @staticmethod
    def get_plist_content(python_bin: str, project_dir: str, email: str = "mhgdidi@gmail.com") -> str:
        log_out = str(Path(project_dir) / "output" / "launchd_stdout.log")
        log_err = str(Path(project_dir) / "output" / "launchd_stderr.log")
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{LAUNCH_AGENT_LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_bin}</string>
        <string>-m</string>
        <string>myjournal.cli</string>
        <string>--email</string>
        <string>{email}</string>
        <string>--no-open</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{project_dir}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>7</integer> <!-- Domingo: 7 (ou 0 em alguns sistemas) -->
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>{log_out}</string>
    <key>StandardErrorPath</key>
    <string>{log_err}</string>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
"""

    @classmethod
    def install(cls, email: str = "mhgdidi@gmail.com") -> bool:
        if sys.platform != "darwin":
            print("[Erro] O LaunchAgent do macOS só pode ser instalado em sistemas Apple/macOS.")
            return False

        project_dir = str(Config.BASE_DIR)
        python_bin = str(Config.BASE_DIR / ".venv" / "bin" / "python3")
        if not os.path.exists(python_bin):
            python_bin = sys.executable

        PLIST_PATH.parent.mkdir(parents=True, exist_ok=True)
        content = cls.get_plist_content(python_bin, project_dir, email)
        PLIST_PATH.write_text(content, encoding="utf-8")

        # Descarrega se já existia e carrega novamente
        subprocess.run(["launchctl", "unload", str(PLIST_PATH)], capture_output=True)
        res = subprocess.run(["launchctl", "load", str(PLIST_PATH)], capture_output=True, text=True)

        if res.returncode == 0:
            print(f"✓ Agendamento configurado com sucesso!")
            print(f"📅 O MyJournal AI rodará automaticamente todo domingo às 07:00 da manhã.")
            print(f"📬 Destinatário configurado: {email}")
            print(f"📄 Arquivo LaunchAgent: {PLIST_PATH}")
            return True
        else:
            print(f"[Erro] Falha ao registrar launchd: {res.stderr}")
            return False

    @classmethod
    def uninstall(cls) -> bool:
        if PLIST_PATH.exists():
            subprocess.run(["launchctl", "unload", str(PLIST_PATH)], capture_output=True)
            PLIST_PATH.unlink()
            print("✓ Agendamento semanal removido do sistema.")
            return True
        print("[Aviso] Nenhum agendamento ativo encontrado.")
        return False
