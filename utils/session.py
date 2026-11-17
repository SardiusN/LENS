
import streamlit as st


def initialize_session():
    """Initialize the application's session state."""

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "input_history" not in st.session_state:
        st.session_state.input_history = []


def add_message(role, content):
    """Add a message to the conversation history."""

    st.session_state.messages.append({
        "role": role,
        "content": content
    })


def get_conversation_history():
    """Return conversation history for the AI model."""

    return st.session_state.messages


def clear_conversation():
    """Clear the current conversation."""

    st.session_state.messages = []
    st.session_state.input_history = []
