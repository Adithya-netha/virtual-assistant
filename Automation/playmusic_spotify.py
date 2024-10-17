import webbrowser
import pyautogui as gui
import time
def  play_music_on_spotify(song_name):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(10)
    gui.hotkey('ctrl','shift','l')
    time.sleep(2)
    gui.write(song_name)
    time.sleep(3)
    gui.leftClick(700,460)


