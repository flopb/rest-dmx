from time import sleep
from pygame import mixer  # Load the required library
from lib import effects
import functools

f = functools.partial


def stop(dmx):
    sleep(3)
    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    dmx.set_all_rgb(values)
    # dmx.update()
    mixer.music.stop()


def play(**kwargs):
    dmx = kwargs.get("dmx")
    fx = effects.FX(dmx)
    startpos = float(kwargs.get("pos"))
    duration = float(kwargs.get("duration"))
    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    dmx.set_all_rgb(values)
    dmx.update()

    ## Set filename of music-title
    file_name = "./sounds/Alice_Cooper_Feed_My_Frankenstein.ogg"

    ## Now the script
    script = {}

    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 255, "6": 255, "7": 255, "8": 255}
    script[12500] = [
        f(dmx.setFixtureValues, fixture="rgb1", values=values),
        f(fx.fade_in, fixtures=["rgb1"], speed=15, limit=255),
        f(fx.fade_out, fixtures=["rgb1"], speed=15, limit=0)
    ]

    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 255, "6": 0, "7": 0, "8": 0}
    script[10000] = [
        f(dmx.setFixtureValues, fixture="rgb1", values=values),
        f(fx.fade_in, fixtures=["rgb1"], speed=15, limit=255),
        f(fx.fade_out, fixtures=["rgb1"], speed=15, limit=0)
    ]

    values1 = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
    values2 = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 255, "6": 0, "7": 0, "8": 0}
    script[8000] = [
        f(dmx.set_all_rgb, values=values1),
        dmx.update,
        f(sleep, 3),
        f(dmx.setFixtureValues, fixture="rgb2", values=values2),
        dmx.update
    ]

    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 255, "7": 0, "8": 0}
    script[13400] = [
        f(dmx.setFixtureValues, fixture="rgb1", values=values),
        f(fx.fade_in, fixtures=["rgb1"], speed=15, limit=255),
        f(fx.fade_out,  fixtures=["rgb1"], speed=15, limit=0)
    ]

    mixer.init()
    mixer.music.load(file_name)
    #mixer.music.set_pos(5)
    mixer.music.play(0, startpos/1000)

    while mixer.music.get_busy():
        currenttime = mixer.music.get_pos() + startpos
        if duration is not None and currenttime > startpos + duration:
            mixer.music.stop()
        for key in script.keys():
            if currenttime >= key and type(script[key]) == list:
                print("Play Script:", key)
                for func in script[key]:
                    func()
                    script[key] = "done"
