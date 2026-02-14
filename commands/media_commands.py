import pywhatkit
from core.voice import speak

def play_music(command):
    song = command.replace("play", "").strip()

    if not song:
        speak("Please tell me what to play.")
        return

    speak(f"Playing {song}")

    try:
        pywhatkit.playonyt(song)
    except Exception as e:
        print("Playback Error:", e)
        speak("Unable to play the video right now.")
