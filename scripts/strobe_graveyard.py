from mylib.udmx import uDMX
import time
from time import sleep
import random
from mylib.soundmanager import SoundManager
import os

def play(**kwargs):
    dmx = kwargs.get("dmx")

    sm = SoundManager()
    #sm.playFX("fx1")
    #sm.playFX("fx2")

    #os.system('omxplayer -r videos/jump_scare_1.mp4')
    #os.system('pkill omxplayer')

    snapshot = dmx.get_snapshot()
    sleeptime=0.05
    t_end = time.time() + 10
    while time.time() < t_end:
        brightness = random.randint(0, 255)
        values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 255, "8": brightness}
        dmx.setFixtureValues("rgb1", values)
        dmx.setFixtureValues("rgb5", values)
        dmx.update()
        # Time the flash
        #sleeptime = random.randint(1, 2) / random.randint(80, 120)
        sleep(sleeptime)

        values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0}
        dmx.setFixtureValues("rgb1", values)
        dmx.setFixtureValues("rgb5", values)
        dmx.update()
        # Time the flash
        # sleeptime = random.randint(1, 2) / random.randint(80, 120)
        sleep(sleeptime)

        brightness = 0
        values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": brightness, "7": brightness,
                  "8": brightness}
        dmx.setFixtureValues("rgb1", values)
        dmx.setFixtureValues("rgb5", values)
        dmx.update()

        # Time between flashes
        #sleeptime = random.randint(0, 20) / random.randint(50, 80)
        sleep(sleeptime)

    brightness = random.randint(0, 255)
    values = {"1": 0, "2": 0, "3": 0, "4": brightness, "5": brightness, "6": brightness, "7": brightness,
              "8": brightness}
    dmx.set_all_rgb(values)
    dmx.update()

    dmx.restore_snapshot(snapshot)