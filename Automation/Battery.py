# pip insatll psutil

import psutil
import time
from Text_to_speech.Braian_voice_tts import speak
import threading
from Alert import alert


def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percentage = int(battery.percent)
        if percentage == 100:
            t1 = threading.Thread(target=alert,args="100% charged")
            t2 = threading.Thread(target=speak,args=("100% charged. please unplug it"))
            t1.start()
            t2.start()
            t1.join()
            t2.join()


# for battery error code 22 23 24