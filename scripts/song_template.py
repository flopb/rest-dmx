from time import sleep
from pygame import mixer  # Load the required library
from mylib import effects
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
    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    dmx.set_all_rgb(values)
    dmx.setFixtureValues("uv", values)
    dmx.update()
    return
    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 255, "6": 255, "7": 255, "8": 255}
    dmx.setFixtureValues("rgb1", values)
    #fx.fade_in(dmx, fixtures=["rgb1"], values=values, speed=15, limit=255),
    #fx.fade_out(dmx, fixtures=["rgb1"], values=values, speed=15, limit=0)



    script = {}
    script[7950] = [
        f(effects.fade_in, dmx, fixtures=["rgb1"], values=values, speed=15, limit=255),
        f(effects.fade_out, dmx, fixtures=["rgb1"], values=values, speed=15, limit=0)
    ]
    script[10500] = [
        f(effects.fade_in, dmx, fixtures=["rgb1"], values=values, speed=15, limit=255),
        f(effects.fade_out, dmx, fixtures=["rgb1"], values=values, speed=15, limit=0)
    ]
    script[12500] = [
        f(dmx.set_all_rgb, values={"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}),
        f(dmx.update),
        f(sleep, 1),
        f(dmx.setFixtureValues, fixture="rgb2",
          values={"1": 0, "2": 0, "3": 0, "4": 0, "5": 255, "6": 0, "7": 0, "8": 0}),
        f(dmx.update)
    ]


    blue = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 255, "8": 0}
    red = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0}
    # color_switch(dmx=dmx,speed=0.5, durration=5, value1=blue, value2=red)

    white = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 0, "8": 255}
    green = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 255, "7": 0, "8": 0}
    # fx.color_switch(dmx=dmx, speed=0.2, durration=5, value1=white, value2=green)

    rows = [blue, red, green]
    # fx.color_row(dmx, ["rgb1"], rows, duration=3, speed=0.01, rand=True)

    # color_row(dmx, "rgb2", rows, duration=3, speed=0.5, rand=True)
    # color_row(dmx, "rgb3", rows, duration=3, speed=0.5, rand=True)
    # color_row(dmx, ["rgb2", "rgb3"], rows, duration=30, speed=0.5, rand=True)

    ## Set filename of video
    file_name = "./sounds/Alice_Cooper_Feed_My_Frankenstein.mp3"

    blue = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 255, "8": 0}
    red = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0}
    # color_switch(dmx=dmx,speed=0.5, durration=5, value1=blue, value2=red)

    white = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 0, "8": 255}
    green = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 255, "7": 0, "8": 0}

    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()

    while mixer.music.get_busy():
        currenttime = mixer.music.get_pos()
        for key in script.keys():
            print(currenttime, ">=", key)
            if currenttime >= key and type(script[key]) == list:
                print("Play Script:", key)
                for func in script[key]:
                    func()
                    script[key] = "done"
    #     if mixer.music.get_pos() >= 12000:
    #         values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    #         dmx.set_all_rgb(values)
    #         dmx.update()
    #         continue
    #     if mixer.music.get_pos() >= 10500:
    #         values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
    #         dmx.set_all_rgb(values)
    #         dmx.update()
    #         continue
    #     if mixer.music.get_pos() >= 10000:
    #         values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    #         dmx.set_all_rgb(values)
    #         dmx.update()
    #         continue
    #     if mixer.music.get_pos() >= 8700:
    #         values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
    #         dmx.set_all_rgb(values)
    #         dmx.update()
    #         continue
    #     if mixer.music.get_pos() >= 8200:
    #         values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    #         dmx.set_all_rgb(values)
    #         dmx.update()
    #         continue
    #     if mixer.music.get_pos() >= 7950:
    #         values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
    #         dmx.set_all_rgb(values)
    #         dmx.update()
    #         continue
    #     if mixer.music.get_pos() == 15000:
    #         values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 255, "8": 0}
    #         dmx.set_all_rgb(values)
    #         dmx.update()
    # os.system('killall omxplayer.bin')
    # omxc = Popen(['omxplayer', '-b', file_name, '-l', '1', '--no-osd'])
    # omxc = Popen(['omxplayer', '-b', file_name, '--no-osd'])

    ## Make snapshot of current lightning settings to restore after script
    # snapshot = dmx.get_snapshot()

    ## Set values which shall be set
    # values = {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 0, "8": 0}

    ## Set "rgb1" PAR to given values
    # dmx.setFixtureValues("rgb1", values)
    ## Set "rgb1" PAR to given values
    # dmx.setFixtureValues("rgb5", values)
    ## Send updated values to devices
    # dmx.update()

    # color_row(dmx, "rgb2", rows, duration=3, speed=0.5, rand=True)
    # color_row(dmx, "rgb3", rows, duration=3, speed=0.5, rand=True)
    # color_row(dmx, ["rgb2", "rgb3"], rows, duration=30, speed=0.5, rand=True)
    # sleep(1)
    # values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 255, "6": 0, "7": 255, "8": 0}
    # dmx.set_all_rgb(values)
    # dmx.update()

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
