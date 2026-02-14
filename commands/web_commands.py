import webbrowser
from core.voice import speak

def open_google():
    speak("Opening Google.")
    webbrowser.open("https://google.com")

def open_youtube():
    speak("Opening YouTube.")
    webbrowser.open("https://youtube.com")
