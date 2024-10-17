import os
from os import getcwd
from winotify import Notification, audio


def alert(text):
    icon_path = r"C:\Users\Adhithya\Desktop\JARVIS\jarvis_logo.ico"

    toast  =Notification(
    app_id="⚡J.A.R.V.I.S",
    title = text,
    msg="",
    duration="short",
    icon=icon_path
 
    )

    toast.set_audio(audio.Default,loop=False)

    toast.add_actions(label="click me",launch="https://www.google.com")
    toast.add_actions(label="dismiss",launch="https://www.gooogle.com")

    toast.show()
