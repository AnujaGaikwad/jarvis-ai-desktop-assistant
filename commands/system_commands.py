import os
import pyautogui
import psutil
from core.voice import speak
import platform
from datetime import datetime
def get_system_info():
    system = platform.system()
    return f"You are running {system} operating system."


def open_camera():
    speak("Opening camera.")
    os.system("start microsoft.windows.camera:")


def open_file_manager():
    speak("Opening file manager.")
    os.startfile("explorer")


def open_vs_code():
    speak("Opening Visual Studio Code.")
    os.system("code")


def open_whatsapp():
    speak("Opening WhatsApp.")
    os.system("start whatsapp:")


def open_copilot():
    speak("Opening Copilot.")
    os.system("start ms-copilot:")


def open_word():
    speak("Opening Microsoft Word.")
    os.system("start winword")


def open_powerpoint():
    speak("Opening Microsoft PowerPoint.")
    os.system("start powerpnt")



def take_screenshot():
    try:
        # Get user's home directory
        home = os.path.expanduser("~")

        # Target folder
        folder_path = os.path.join(home, "OneDrive", "Pictures", "Screenshots")

        # Create folder if not exists
        os.makedirs(folder_path, exist_ok=True)

        # Unique file name with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(folder_path, f"screenshot_{timestamp}.png")

        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)

        speak("Screenshot saved successfully.")

        print("Saved at:", file_path)

    except Exception as e:
        print("Screenshot Error:", e)
        speak("Unable to take screenshot.")


def battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"Battery is at {percent} percent.")
    else:
        speak("Battery information not available.")
