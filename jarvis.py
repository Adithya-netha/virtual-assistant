import threading
from internet_check import is_Online
from Alert import alert
from DATA.dialouge_data import online_dlg
from Text_to_speech.Braian_voice_tts import speak
from co_brain import jarvis
import random

random_dilauge = random.choice(online_dlg)

def main():
    if is_Online():
        t1 = threading.Thread(target=speak,args=(random_dilauge,))
        t2 = threading.Thread(target=alert,args=(random_dilauge,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        jarvis()
    else:

        alert("Iam offline") 

main()
