import os
import socket
from dotenv import load_dotenv
from google import genai
from utils.logger import log_error
from config import AI_MODEL
from core.personality import get_mode
from core.memory import get_memory, add_to_memory


# Load environment variables
load_dotenv()

# Initialize Gemini client
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)


def is_online():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except:
        return False


def ask_ai(command):
    if not is_online():
        return "I am currently offline. Please check your internet connection."

    try:
        mode = get_mode()
        context = get_memory()

        full_prompt = f"""
You are Jarvis in {mode} mode.
Respond accordingly.

Conversation history:
{context}

User: {command}
"""

        response = client.models.generate_content(
            model=AI_MODEL,
            contents=full_prompt
        )

        reply = response.text.strip()

        add_to_memory("User", command)
        add_to_memory("Jarvis", reply)

        return reply

    except Exception as e:
        log_error(f"AI Error: {e}")
        return "Sorry, I am unable to respond right now."
