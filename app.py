
import os
import streamlit as st

from core.assistant import generate_response
from utils.session import (
    initialize_session,
    add_message,
    get_conversation_history,
    clear_conversation
)
from voice.speech_to_text import transcribe_audio
from voice.text_to_speech import generate_speech


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="LENS | Think Beyond Answers",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

initialize_session()

# State used to reset the voice recorder after submission
if "voice_widget_version" not in st.session_state:
    st.session_state.voice_widget_version = 0

if "pending_user_input" not in st.session_state:
    st.session_state.pending_user_input = None


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

def load_css():
    css_path = os.path.join("assets", "styles.css")

    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as file:
            st.markdown(
                f"<style>{file.read()}</style>",
                unsafe_allow_html=True
            )


load_css()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.title("🔍 LENS")
    st.caption("Logical Exploration and Navigation System")

    st.divider()

    st.markdown("### Your thinking companion")
    st.write(
        "Explore questions, challenge assumptions, "
        "examine perspectives and develop reasoned conclusions."
    )

    st.divider()

    st.markdown("### Capabilities")
    st.markdown(
        """
        - Critical thinking and analysis
        - Question decomposition
        - Multiple perspectives
        - Counterargument evaluation
        - Conversational memory
        - Voice interaction
        """
    )

    st.divider()

    if st.button("🗑️ Clear conversation", use_container_width=True):
        clear_conversation()
        st.session_state.voice_transcription = None
        st.session_state.pending_user_input = None
        st.session_state.voice_widget_version += 1
        st.rerun()

    st.caption("LENS | AI Reasoning Assistant")


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-label">THINK BEYOND ANSWERS</div>
        <h1>Explore. Question. Understand.</h1>
        <p>
            A space to examine ideas, challenge assumptions,
            and arrive at reasoned conclusions.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# CONVERSATION DISPLAY
# --------------------------------------------------

for message in get_conversation_history():
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# VOICE INPUT
# --------------------------------------------------

st.markdown("### What would you like to explore?")
st.markdown("#### Speak your question")

audio_file = st.audio_input(
    "Record your question",
    key=f"voice_input_{st.session_state.voice_widget_version}"
)

if audio_file is not None:

    if st.button("Transcribe recording", key="transcribe_button"):

        with st.spinner("Understanding your speech..."):

            try:
                transcription = transcribe_audio(audio_file)

                if transcription:
                    st.session_state.voice_transcription = transcription
                else:
                    st.warning("No speech was detected.")

            except Exception as error:
                st.error(f"Voice recognition failed: {error}")


# Display transcription and submission button

if st.session_state.get("voice_transcription"):

    st.markdown("**Recognised speech:**")

    st.info(st.session_state.voice_transcription)

    if st.button("Send transcribed question", key="send_voice_button"):

        st.session_state.pending_user_input = (
            st.session_state.voice_transcription
        )

        st.session_state.voice_transcription = None

        # Give the next recording widget a fresh identity
        st.session_state.voice_widget_version += 1

        st.rerun()


# --------------------------------------------------
# TEXT INPUT
# --------------------------------------------------

st.markdown("#### Or type your question")

with st.form("text_question_form", clear_on_submit=True):

    text_input = st.text_input(
        "Your question",
        placeholder="Type your question here..."
    )

    text_submitted = st.form_submit_button("Send question")


# --------------------------------------------------
# AI RESPONSE GENERATION
# --------------------------------------------------

user_input = None

if st.session_state.pending_user_input:
    user_input = st.session_state.pending_user_input
    st.session_state.pending_user_input = None

elif text_submitted and text_input.strip():
    user_input = text_input.strip()


if user_input:

    add_message("user", user_input)

    with st.spinner("LENS is exploring your question..."):

        try:
            history = get_conversation_history()[:-1]

            response = generate_response(
                user_input,
                history
            )

            add_message("assistant", response)

            # Re-render the application with the updated conversation
            st.rerun()

        except Exception as error:
            st.error(f"Something went wrong: {error}")


# --------------------------------------------------
# TEXT-TO-SPEECH
# --------------------------------------------------

if get_conversation_history():

    last_message = get_conversation_history()[-1]

    if last_message["role"] == "assistant":

        if st.button("🔊 Read latest response aloud"):

            with st.spinner("Generating speech..."):

                audio_path = None

                try:
                    audio_path = generate_speech(
                        last_message["content"]
                    )

                    if audio_path:

                        with open(audio_path, "rb") as audio_file:
                            audio_bytes = audio_file.read()

                        st.audio(
                            audio_bytes,
                            format="audio/wav"
                        )

                except Exception as error:
                    st.error(f"Speech generation failed: {error}")

                finally:
                    if audio_path and os.path.exists(audio_path):
                        os.remove(audio_path)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div class="footer">
        LENS — Logical Exploration and Navigation System
        <br>
        <span>Think critically. Explore deeply. Understand better.</span>
    </div>
    """,
    unsafe_allow_html=True
)

