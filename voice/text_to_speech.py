
import os
import tempfile
import pyttsx3
import re

def clean_text_for_speech(text):
    """Remove Markdown formatting before text-to-speech conversion."""

    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", " ", text)

    # Remove Markdown headings
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

    # Remove bold and italic formatting
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    text = re.sub(r"_(.*?)_", r"\1", text)

    # Remove horizontal separators
    text = re.sub(r"^\s*[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)

    # Remove Markdown table separators and formatting
    text = re.sub(r"\|", " ", text)
    text = re.sub(r"^\s*[-:\s]+\s*$", "", text, flags=re.MULTILINE)

    # Remove inline code markers
    text = text.replace("`", "")

    # Remove links, retaining their visible text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # Remove excessive whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()

def generate_speech(text):
    """
    Convert text into speech and save it as a temporary WAV file.

    Returns:
        str: Path to the generated audio file.
    """

    if not text or not text.strip():
        return None

    temporary_path = None
    engine = None

    try:
        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temporary_file:
            temporary_path = temporary_file.name

        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        engine.setProperty("volume", 0.9)

        cleaned_text = clean_text_for_speech(text)

        engine.save_to_file(cleaned_text, temporary_path)

        engine.runAndWait()

        return temporary_path

    except Exception:
        if temporary_path and os.path.exists(temporary_path):
            os.remove(temporary_path)
        raise

    finally:
        if engine is not None:
            engine.stop()
