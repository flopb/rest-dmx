from lib.udmx import uDMX
import time
from time import sleep
import random
from lib.soundmanager import SoundManager
import os
from subprocess import Popen
import random
from pygame import mixer  # Load the required library

def color_row(dmx, fixtures, rows, duration=3, speed=0.2, rand=False):
    if type(fixtures) == str:
        fixtures = [fixtures]
    t_end = time.time() + duration
    switch = True
    newrow = random.choice(rows)
    prev_row = None
    while time.time() < t_end:
        if rand is not True:
            for row in rows:
                for fixture in fixtures:
                    dmx.setFixtureValues(fixture, row)
                dmx.update()
                sleep(speed)
        else:
            while prev_row == newrow:
                newrow = random.choice(rows)
            for fixture in fixtures:
                dmx.setFixtureValues(fixture, newrow)
            prev_row = newrow
            dmx.update()

            sleep(speed)

def color_switch(dmx, value1, value2, durration=10, speed=0.2):
    t_end = time.time() + durration
    switch = True
    while time.time() < t_end:
        switch = not switch
        if switch is True:
            values = value1
        else:
            values = value2
        dmx.setFixtureValues("rgb2", values)
        dmx.update()
        sleep(speed)

def stop(dmx):
    sleep(3)
    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    dmx.set_all_rgb(values)
    #dmx.update()
    mixer.music.stop()

def play(**kwargs):
    dmx = kwargs.get("dmx")
    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    dmx.set_all_rgb(values)
    dmx.update()

    ## Set filename of video
    file_name = "./sounds/Alice_Cooper_Feed_My Frankenstein.mp3"


    blue = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 255, "8": 0}
    red = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0}
    # color_switch(dmx=dmx,speed=0.5, durration=5, value1=blue, value2=red)

    white = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 0, "8": 255}
    green = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 255, "7": 0, "8": 0}

    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()

    while mixer.music.get_busy():
        #print(mixer.music.get_pos())
        if mixer.music.get_pos() >= 12000:
            values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
            dmx.set_all_rgb(values)
            dmx.update()
            stop(dmx)
            continue
        if mixer.music.get_pos() >= 10500:
            values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
            dmx.set_all_rgb(values)
            dmx.update()
            continue
        if mixer.music.get_pos() >= 10000:
            values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
            dmx.set_all_rgb(values)
            dmx.update()
            continue
        if mixer.music.get_pos() >= 8700:
            values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
            dmx.set_all_rgb(values)
            dmx.update()
            continue
        if mixer.music.get_pos() >= 8200:
            values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
            dmx.set_all_rgb(values)
            dmx.update()
            continue
        if mixer.music.get_pos() >= 7950:
            values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
            dmx.set_all_rgb(values)
            dmx.update()
            continue


        if mixer.music.get_pos() == 15000:
            values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
            dmx.set_all_rgb(values)
            dmx.update()
    #os.system('killall omxplayer.bin')
    # omxc = Popen(['omxplayer', '-b', file_name, '-l', '1', '--no-osd'])
    #omxc = Popen(['omxplayer', '-b', file_name, '--no-osd'])

    ## Make snapshot of current lightning settings to restore after script
    snapshot = dmx.get_snapshot()

    ## Set values which shall be set
    #values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 255, "8": 255}

    ## Set "rgb1" PAR to given values
    #dmx.setFixtureValues("rgb2", values)
    ## Set "rgb1" PAR to given values
    #dmx.setFixtureValues("rgb5", values)
    ## Send updated values to devices
    #dmx.update()
    #sleep(1)
    ## Set all rgb-pars to given values
    #values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
    #dmx.set_all_rgb(values)
    #dmx.update()

    blue = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 255, "8": 0}
    red = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0}
    #color_switch(dmx=dmx,speed=0.5, durration=5, value1=blue, value2=red)

    white = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 0, "8": 255}
    green = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 255, "7": 0, "8": 0}
    #color_switch(dmx=dmx, speed=0.2, durration=5, value1=white, value2=green)

    rows = [blue,red,green]
    #color_row(dmx, ["rgb2", "rgb3"], rows, duration=3, speed=0.01, rand=True)
    #color_row(dmx, "rgb2", rows, duration=3, speed=0.5, rand=True)
    #color_row(dmx, "rgb3", rows, duration=3, speed=0.5, rand=True)
    #color_row(dmx, ["rgb2", "rgb3"], rows, duration=30, speed=0.5, rand=True)
    #sleep(1)
    #values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 255, "6": 0, "7": 255, "8": 0}
    #dmx.set_all_rgb(values)
    #dmx.update()

    ## Just wait 3 seconds
    # sleep(3)

    # #brightness = 0
    # #while brightness < 250:
    #     values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": brightness, "8": 0}
    #     dmx.setFixtureValues("rgb2", values)
    #     dmx.update()
    #     brightness = brightness + 1
    #     sleep(0.01)
    #
    #
    # #brightness = 250
    # #while brightness > 0:
    #     values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": brightness, "6": 0, "7": brightness, "8": 0}
    #     dmx.setFixtureValues("rgb2", values)
    #     dmx.update()
    #     brightness = brightness - 1
    #     sleep(0.01)

# do whatever you do
# restore initial state at end of script with values saved at the beginning
# dmx.restore_snapshot(snapshot)
