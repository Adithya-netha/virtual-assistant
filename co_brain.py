from Automation.Automation_brain import Auto_main_brain,clear_file
from Speectotext.speechtotext import listen
import threading
from DATA.dialouge_data import online_dlg
import random
from Automation.Battery import battery_alert

random_online_dlg = random.choice(online_dlg)

def check_inputs():
    output_text = ""
    while True:
        with open("input.txt","r") as file:
            input_text = file.read().lower()
            if input_text != output_text:
                output_text = input_text
                if output_text:
                    Auto_main_brain(output_text)
            else:
                pass

def jarvis():
    clear_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
                 