import os
import time

def mute():
    os.system('playerctl -p spotify volume 0.0')

def unmute():
    os.system('playerctl -p spotify volume 1.0')

def getTitle():
    title = os.popen('playerctl -p spotify metadata title').read()
    title = title.replace('\n', '')
    return title

while True:
    if getTitle() == 'Advertisement':
        mute()
        time.sleep(1)
    else:
        unmute()
        time.sleep(1)
