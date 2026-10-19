import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class Config:
    BASE_DIR = BASE_DIR
    AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini").lower()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

    NEWSPAPER_TITLE = os.getenv("NEWSPAPER_TITLE", "THE PERSONAL DISPATCH")
    NEWSPAPER_SUBTITLE = os.getenv("NEWSPAPER_SUBTITLE", "Edição Semanal Dedicada ao Conhecimento, Cultura e Planejamento")
    OWNER_NAME = os.getenv("OWNER_NAME", "Mauricio")
    CITY = os.getenv("CITY", "São Paulo")

    GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH", str(BASE_DIR / "credentials.json"))
    GOOGLE_TOKEN_PATH = os.getenv("GOOGLE_TOKEN_PATH", str(BASE_DIR / "token.json"))

    OUTPUT_DIR = BASE_DIR / "output"
    OUTPUT_DIR.mkdir(exist_ok=True)
