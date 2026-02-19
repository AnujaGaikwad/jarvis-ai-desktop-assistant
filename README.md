🤖 JARVIS – AI Desktop Voice Assistant
📌 Project Overview

JARVIS is a multi-threaded, event-driven AI desktop voice assistant built using Python.
It combines rule-based automation with Google Gemini AI to provide intelligent, contextual, and personality-driven voice interactions.

The assistant runs in the background, listens for a wake word, processes commands, and performs real system-level tasks such as opening applications and controlling media.

🚀 Key Features

🎙 Wake-word activation ("Jarvis")

🧠 Gemini AI integration for intelligent responses

🗂 Short-term conversation memory

🎭 Personality modes (Normal / Study / Fun)

💻 Windows application launcher (VS Code, Word, PowerPoint, File Manager, Camera, WhatsApp, Copilot)

📸 Screenshot capture with auto-save

🔋 Battery status detection

🧵 Multi-threaded background listener

📜 Structured logging system

🔐 Secure API key management using .env

⚙ Modular architecture for easy scalability

🏗 System Architecture
1️⃣ Input Layer

Microphone input via speech_recognition

Wake-word detection

2️⃣ Control Layer

Background listener thread

Command routing logic

3️⃣ Decision Layer

Predefined rule-based commands

AI fallback system

4️⃣ Intelligence Layer

Gemini AI (ai_engine.py)

Context memory

Personality mode management

5️⃣ Output Layer

gTTS for speech synthesis

Pygame for audio playback

Offline fallback handling

📂 Project Structure
jarvis-ai-desktop-assistant/
│
├── core/
│   ├── ai_engine.py
│   ├── command_handler.py
│   ├── memory.py
│   ├── personality.py
│   └── voice.py
│
├── commands/
│   ├── media_commands.py
│   ├── system_commands.py
│   └── web_commands.py
│
├── data/
│   └── music_library.py
│
├── utils/
│   └── logger.py
│
├── config.py
├── main.py
├── requirements.txt
├── .env (not committed)
└── README.md

🛠 Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-url>
cd jarvis-ai-desktop-assistant

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add API Key

Create .env file:

GOOGLE_API_KEY=your_api_key_here

5️⃣ Run the Project
python main.py

🎯 Example Commands
Jarvis open google
Jarvis open vs code
Jarvis open word
Jarvis open camera
Jarvis plays believer
Jarvis take screenshot
Jarvis battery status
Jarvis study mode
Jarvis fun mode

🔒 Security

API key is stored in .env file (not committed to GitHub)

Dangerous system commands removed for safer demo

The logging system tracks system activity

📈 Engineering Highlights

Multi-threaded architecture

Modular separation of concerns

Centralized configuration system

Graceful error handling

Clean audio pipeline

Real-world Windows integration

🔮 Future Improvements

Offline LLM fallback

Real wake-word engine 

GUI dashboard

Smart home integration

Task scheduling

👩‍💻 Author

Anuja Ramesh Gaikwad
