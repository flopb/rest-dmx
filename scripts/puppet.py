from lib.udmx import uDMX
import time
from time import sleep
import random
from lib.soundmanager import SoundManager
import os

def play(**kwargs):
    dmx = kwargs.get("dmx")

    #sm = SoundManager()
    #sm.playFX("fx1")
    #sm.playFX("fx2")

    #os.system('omxplayer -r videos/jump_scare_1.mp4')
    #os.system('pkill omxplayer')
    t_end = time.time() + 3
    while time.time() < t_end:

        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        W = random.randint(0, 255)
        Bright = random.randint(0, 255)
        fixture = "rgb1"
        values = {"1": 0, "2": 0, "3": 0, "4": Bright, "5": R, "6": G, "7": B, "8": W}
        dmx.setFixtureValues(fixture, values)

        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        W = random.randint(0, 255)
        Bright = random.randint(0, 255)

        fixture = "rgb2"
        values = {"1": 0, "2": 0, "3": 0, "4": Bright, "5": R, "6": G, "7": B, "8": W}
        dmx.setFixtureValues(fixture, values)

        dmx.update()

        sleep(0.3)

    values = {"1": 12, "2": 40, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0}
    fixture = "rgb1"
    dmx.setFixtureValues(fixture, values)
    values = {"1": 12, "2": 60, "3": 0, "4": 255, "5": 0, "6": 0, "7": 255, "8": 0}
    fixture = "rgb2"
    dmx.setFixtureValues(fixture, values)

    dmx.update()