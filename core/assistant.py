
from core.groq_client import get_groq_client
from core.prompts import SYSTEM_PROMPT
from config import MODEL_NAME, MAX_TOKENS


def generate_response(user_message, conversation_history=None):
    """Generate an AI response using the Groq API."""

    client = get_groq_client()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    if conversation_history:
        messages.extend(conversation_history)

    messages.append({
        "role": "user",
        "content": user_message
    })

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            max_tokens=MAX_TOKENS
        )

        return response.choices[0].message.content

    except Exception as error:
        raise RuntimeError(f"Unable to generate a response: {error}")
