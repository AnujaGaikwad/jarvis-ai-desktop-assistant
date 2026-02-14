import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import time
import pyttsx3
from config import WAKE_WORD

# Initialize recognizer
recognizer = sr.Recognizer()

# Initialize pygame mixer ONCE
pygame.mixer.init()

# Initialize offline engine once
engine = pyttsx3.init()


def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()


import uuid

def speak(text):
    try:
        filename = f"temp_{uuid.uuid4().hex}.mp3"

        tts = gTTS(text=text, lang="en")
        tts.save(filename)

        play_audio(filename)

        # Small delay before deletion (important on Windows)
        time.sleep(0.2)

        os.remove(filename)

    except Exception as e:
        print("TTS Error:", e)
        engine.say(text)
        engine.runAndWait()


def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

def play_startup():
    import os
    if os.path.exists("startup.mp3"):
        play_audio("startup.mp3")


def listen_for_wake_word():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            text = recognizer.recognize_google(audio)
            print("Heard:", text)

            text = text.lower().strip()

            if "jarvis" in text:
                command = text.replace("jarvis", "").strip()

                # Ignore if only wake word spoken
                if command == "":
                    return None

                return command

    except:
        return None



def listen_command():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print("Listening for confirmation...")
            return command

    except:
        return None
