from core.voice import listen_for_wake_word, listen_command, speak, play_startup
from core.command_handler import handle_command
import threading
import time
from utils.logger import log_info, log_error
running = True
listening_enabled = True

def pause_listener():
    global listening_enabled
    listening_enabled = False

def resume_listener():
    global listening_enabled
    listening_enabled = True

def background_listener():
    global running, listening_enabled

    while running:
        if not listening_enabled:
            time.sleep(0.2)
            continue

        command = listen_for_wake_word()

        if command:
            handle_command(command, pause_listener, resume_listener)


def main():
    global running

    play_startup()
    speak("Jarvis online.")

    listener_thread = threading.Thread(target=background_listener)
    listener_thread.start()

    while running:
        time.sleep(1)

    listener_thread.join()

if __name__ == "__main__":
    main()
