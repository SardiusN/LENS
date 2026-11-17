
import os
import tempfile
import streamlit as st
from faster_whisper import WhisperModel


@st.cache_resource
def load_whisper_model():
    """Load and cache the Whisper speech recognition model."""

    return WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )


def transcribe_audio(audio_file):
    """
    Convert recorded audio into text using Faster-Whisper.

    Args:
        audio_file: Audio file received from Streamlit.

    Returns:
        str: Transcribed text.
    """

    if audio_file is None:
        return ""

    temporary_path = None

    try:
        model = load_whisper_model()

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temporary_file:
            temporary_file.write(audio_file.getvalue())
            temporary_path = temporary_file.name

        segments, info = model.transcribe(
            temporary_path,
            beam_size=5
        )

        transcription = " ".join(
            segment.text.strip() for segment in segments
        )

        return transcription.strip()

    finally:
        if temporary_path and os.path.exists(temporary_path):
            os.remove(temporary_path)
