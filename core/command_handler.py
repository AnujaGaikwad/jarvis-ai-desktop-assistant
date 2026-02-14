from core.voice import speak, listen_command
from core.ai_engine import ask_ai
from commands.web_commands import open_google, open_youtube
from commands.media_commands import play_music
from commands.system_commands import get_system_info
from commands.system_commands import  take_screenshot, battery_status
from core.personality import set_mode
import time
from commands.system_commands import (
    open_camera,
    open_file_manager,
    open_vs_code,
    open_whatsapp,
    open_copilot,
    open_word,
    open_powerpoint
)


def handle_command(command, pause_listener=None, resume_listener=None):
    command = command.lower()

    if "open google" in command:
        open_google()

    elif "open youtube" in command:
        open_youtube()

    elif command.startswith("play"):
        play_music(command)

    elif "system info" in command:
        info = get_system_info()
        speak(info)


    elif "screenshot" in command:
        take_screenshot()

    elif "battery status" in command:
        battery_status()

    elif "study mode" in command:
        set_mode("study")
        speak("Study mode activated.")

    elif "fun mode" in command:
        set_mode("fun")
        speak("Fun mode activated.")
    elif "open camera" in command:
        open_camera()

    elif "open file manager" in command or "open files" in command:
        open_file_manager()

    elif "open vs code" in command or "open code" in command:
        open_vs_code()

    elif "open whatsapp" in command:
        open_whatsapp()

    elif "open copilot" in command:
        open_copilot()

    elif "open word" in command:
        open_word()

    elif "open powerpoint" in command or "open ppt" in command:
        open_powerpoint()

    else:
        reply = ask_ai(command)
        speak(reply)
