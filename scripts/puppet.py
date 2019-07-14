from mylib.udmx import uDMX
import time
from time import sleep
import random
from mylib.soundmanager import SoundManager
import os

def play(**kwargs):
    dmx = kwargs.get("dmx")


    t_end = time.time() + 7
    sleeptime=0.075
    values = {"1": 255, "2": 255, "3": 255, "4": 255, "5": 0, "6": 0, "7": 0}
    fixture = "uv"
    dmx.setFixtureValues(fixture, values)
    fixture = "fog"
    values = {"1": 255}
    dmx.setFixtureValues(fixture, values)
    dmx.update()
    while time.time() < t_end:

        #R = random.randint(0, 255)
        #G = random.randint(0, 255)
        #B = random.randint(0, 255)
        #W = random.randint(0, 255)
        #Bright = random.randint(0, 255)
        if time.time() > (t_end - 6):
            fixture = "fog"
            values = {"1": 0}
            dmx.setFixtureValues(fixture, values)
            dmx.update()
        R=255
        G=0
        B=0
        W=0
        Bright=255
        fixture = "rgb4"
        values = {"1": 0, "2": 0, "3": 0, "4": Bright, "5": R, "6": G, "7": B, "8": W}
        dmx.setFixtureValues(fixture, values)

        dmx.update()

        sleep(sleeptime)

        R = 0
        G = 0
        B = 255
        W = 0
        Bright = 255
        fixture = "rgb4"
        values = {"1": 0, "2": 0, "3": 0, "4": Bright, "5": R, "6": G, "7": B, "8": W}
        dmx.setFixtureValues(fixture, values)
        dmx.update()
        sleep(sleeptime)

    fixture = "fog"
    values = {"1": 0}
    dmx.setFixtureValues(fixture, values)
    dmx.update()

    values = {"1": 0, "2": 40, "3": 0, "4": 255, "5": 100, "6": 0, "7": 0, "8": 0}
    fixture = "rgb4"
    dmx.setFixtureValues(fixture, values)
    values = {"1": 255, "2": 255, "3": 255, "4": 255, "5": 0, "6": 0, "7": 0}
    fixture = "uv"
    dmx.setFixtureValues(fixture, values)

    dmx.update()