
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def get_groq_client():
    """
    Initialize and return the Groq API client.
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "Groq API key not found. Please configure GROQ_API_KEY in your .env file."
        )

    return Groq(api_key=api_key)
