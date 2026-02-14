from gtts import gTTS

text = """
Artificial intelligence initialized.
Systems synchronized.
Awaiting your command,Anu.
"""

tts = gTTS(text=text, lang="en")
tts.save("startup.mp3")

print("Startup sound generated successfully.")
