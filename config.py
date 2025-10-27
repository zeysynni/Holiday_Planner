# config.py
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# === API Keys ===
SERPAPI_KEY = os.getenv("SERP_API_KEY")
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
PUSHOVER_USER = os.getenv("PUSHOVER_USER")

# === Constants ===
PUSHOVER_URL = "https://api.pushover.net/1/messages.json"
SANDBOX_DIR = "sandbox"
DEFAULT_CURRENCY = "EUR"
