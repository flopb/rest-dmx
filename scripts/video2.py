from lib.udmx import uDMX
import os
from subprocess import Popen
from lib.soundmanager import SoundManager

def play(**kwargs):
    dmx = kwargs.get("dmx")
    #sm = SoundManager()
    #sm.playFX("fx1")
    #sm.playFX("fx2")
    brightness = 0
    values = {"1": 0, "2": 0, "3": 0, "4": brightness, "5": brightness, "6": brightness, "7": brightness,
              "8": brightness}
    dmx.set_all_rgb(values)
    dmx.update()
    file_name = "./videos/jump_scare_2.mp4"
    os.system('killall omxplayer.bin')
    omxc = Popen(['omxplayer', '-b', file_name, '-l', '1', '--no-osd'])