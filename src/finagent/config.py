# src/finagent/config.py
import os
from dotenv import load_dotenv

# Force .env to override any Windows environment variables
load_dotenv(override=True)

class Settings:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.polygon_api_key = os.getenv("POLYGON_API_KEY", "").strip()
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo").strip()
        self.temperature = float(os.getenv("TEMPERATURE", "0"))
        self.log_level = os.getenv("LOG_LEVEL", "INFO").strip()

def get_settings() -> Settings:
    s = Settings()
    if not s.openai_api_key:
        raise RuntimeError("Missing OPENAI_API_KEY in .env or environment.")
    if not s.polygon_api_key:
        raise RuntimeError("Missing POLYGON_API_KEY in .env or environment.")
    return s
