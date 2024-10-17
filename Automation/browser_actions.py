import pyautogui
from Text_to_speech.Braian_voice_tts import speak

def zoom_in():
    pyautogui.hotkey('ctrl', '+')

def zoom_out():
    pyautogui.hotkey('ctrl', '-')

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def switch_to_previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')


def toggle_full_screen():
    pyautogui.hotkey('f11')


def perform_browser_actions(text):
    if "zoom in" in text or "zoom in karo" in text:
        speak("initiating command")
        zoom_in()
    elif "zoom out" in text or "zoom out karo" in text:
        speak("initiating command")
        zoom_out()
    elif "refresh page" in text or "page refresh karo" in text:
        speak("initiating command")
        refresh_page()
    elif "switch to next tab" in text or "next tab par jao" in text:
        speak("initiating command")
        switch_to_next_tab()
    elif "switch to previous tab" in text or "previous tab par jao" in text:
        speak("initiating command")
        switch_to_previous_tab()
    elif "go back" in text or "peeche jao" in text:
        speak("initiating command")
        go_back()
    elif "go forward" in text or "aage jao" in text:
        speak("initiating command")
        go_forward()
    elif "toggle full screen" in text or "full screen karo" in text:
        speak("initiating command")
        toggle_full_screen()
    else:
        pass