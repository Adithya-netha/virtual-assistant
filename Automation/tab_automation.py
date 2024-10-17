import pyautogui as gui
from Text_to_speech.Braian_voice_tts import speak

def open_new_tab():
    gui.hotkey('ctrl', 't')

def close_tab():
    gui.hotkey('ctrl', 'w')

def open_browser_menu():
    gui.hotkey('alt', 'f')

def zoom_in():
    gui.hotkey('ctrl', '+')

def zoom_out():
    gui.hotkey('ctrl', '-')

def refresh_page():
    gui.hotkey('ctrl', 'r')

def switch_to_next_tab():
    gui.hotkey('ctrl', 'tab')

def switch_to_previous_tab():
    gui.hotkey('ctrl', 'shift', 'tab')

def open_history():
    gui.hotkey('ctrl', 'h')

def open_bookmarks():
    gui.hotkey('ctrl', 'b')

def go_back():
    gui.hotkey('alt', 'left')

def go_forward():
    gui.hotkey('alt', 'right')

def open_dev_tools():
    gui.hotkey('ctrl', 'shift', 'i')

def toggle_full_screen():
    gui.hotkey('f11')

def open_private_window():
    gui.hotkey('ctrl', 'shift', 'n')

def close():
    gui.hotkey('alt','F4')


def perform_browser_action(text):
    if "new tab" in text or "new tab kholo" in text:
        speak("initiating command")
        open_new_tab()
    elif "close tab" in text or "tab band karo" in text:
        speak("initiating command")
        close_tab()
    elif "browser menu" in text or "browser menu kholo" in text:
        speak("initiating command")
        open_browser_menu()
    elif "history" in text or "history kholo" in text:
        speak("initiating command")
        open_history()
    elif "bookmarks" in text or "bookmarks kholo" in text:
        speak("initiating command")
        open_bookmarks()
    elif "dev tools" in text or "dev tools kholo" in text:
        speak("initiating command")
        open_dev_tools()
    elif "private window" in text or "incognito mode" in text:
        speak("initiating command")
        open_private_window()
    elif "close" in text:
      close()
    else:
        pass