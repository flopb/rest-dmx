from lib.udmx import uDMX
import time
from time import sleep
import random


def play(**kwargs):
    dmx = kwargs.get("dmx")

    t_end = time.time() + 10
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

        #sleep(0.1)