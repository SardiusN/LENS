
import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "LENS"
APP_FULL_NAME = "Logical Exploration and Navigation System"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "openai/gpt-oss-120b"

MAX_TOKENS = 8192
TEMPERATURE = 0.6

WHISPER_MODEL_SIZE = "base"
