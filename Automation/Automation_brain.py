from  Automation.open_app import open_app
from Automation.open_wesite import openweb
import pyautogui as gui
import pywhatkit
from Text_to_speech.Braian_voice_tts import speak
from Automation.play_music_yt import play_music_on_yt
from  Automation.playmusic_spotify import play_music_on_spotify
from os import getcwd
import time
from Automation.tab_automation import perform_browser_action
from Automation.youtube_playback import perform_media_action
from Automation.browser_actions import perform_browser_actions
from Automation.youtube_playback import perform_media_action
def close():
    gui.hotkey('alt','f4')

def search(text):
   gui.press("/")
   time.sleep(0.2)
   gui.write(text)
   time.sleep(0.2)
   gui.press('enter')
   

def closing_brain(text):
   if "close" in text:
      perform_browser_action(text)

def opening_brain(text):
    if "website" in text or "open website" in text:
        text = text.replace("website", "").replace("open", "").replace("open website", "").strip()
        openweb(text)
    elif "open" in text:
        app_name = text.replace("open", "").strip()
      
        open_app(app_name)

def search_youtube(text):
   pywhatkit.search(text)

def shutdown():
   gui.hotkey('alt','F4')
   time.sleep(5)
   gui.hotkey('alt','F4')
   time.sleep(3)
   gui.sleep('enter')

   





def clear_file():
  with open(f"{getcwd()}\\input.txt","w") as file:
    file.truncate(0)
   
def Auto_main_brain(text):
    try:
      if text.startswith("open"):
        opening_brain(text)
      elif "close" in text:
         closing_brain(text)
      elif "shutdown" in text:
         shutdown()
      elif "play music" in text or "play music on youtube" in text:
        speak("which song do you want to play sir")
        clear_file()
        output_text = ""
        while True:
          with open("input.txt","r") as file:
            input_text = file.read().lower()
            if input_text != output_text:
              output_text = input_text
              if output_text:
                 play_music_on_yt(output_text)
              break 
      # elif "play some music" in text or "play music on spotify" in text:
      #   speak("which song do you want to play on spotify sir")
      #   clear_file()
      #   output_text = ""
      #   while True:
      #     with open("input.txt","r") as file:
      #       input_text = file.read().lower()
      #       if input_text != output_text:
      #         output_text = input_text
      #         if output_text:
      #            play_music_on_spotify(output_text)
      #         break 
      elif text.startswith("search"):
         text = text.replace("search","")
         text.strip()
         search(text)
      elif "search on youtube" in text:
         text.replace("search on youtube","")
         search_youtube(text)
      else:
        perform_media_action(text)
        perform_browser_actions(text)
        perform_media_action(text)

    except Exception as e:
       print(e)