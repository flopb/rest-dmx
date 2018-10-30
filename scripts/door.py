from lib.udmx import uDMX
import time
from time import sleep
import random
from lib.soundmanager import SoundManager
import os
import requests

def play(**kwargs):
    t_end = time.time() + 30
    while time.time() < t_end:
        ############Set hue in entry area to blue
        url = "http://192.168.178.46/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/lights/14/state"
        brightness = 255

        payload = "{\"on\":true, \"on\":true, \"bri\":"+str(brightness)+"}"
        headers = {}
        response = requests.request("PUT", url, data=payload, headers=headers)
        ############################################

        sleeptime = 1
        ############Set hue in entry area to blue
        url = "http://192.168.178.46/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/lights/14/state"
        brightness = 0

        payload = "{\"on\":true, \"on\":true, \"bri\":" + str(brightness) + "}"
        headers = {}
        response = requests.request("PUT", url, data=payload, headers=headers)
        ############################################

        # Time between flashes
        sleeptime = 1.4
        sleep(sleeptime)

