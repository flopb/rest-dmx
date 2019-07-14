from mylib.helpers import runScript
from time import sleep
from mylib import effects
import functools

f = functools.partial

def play(**kwargs):
    dmx = kwargs.get("dmx")
    fx = effects.FX(dmx)
    script = {}
    startpos = float(kwargs.get("pos"))
    duration = float(kwargs.get("duration")) if kwargs.get("duration") is not None else None

    ## Create initial mood
    fx.blackout()

    ## Set filename of music-title
    file_name = "./sounds/Alice_Cooper_Feed_My_Frankenstein.mp3"

    ## Here comes the script
    script[0] = [f(fx.fog, intensity=255, duration=1.0)]  # manual
    script[7975] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[8601] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[10425] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[11371] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[12177] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.05, laps=1, reverse=False)]  # 2
    script[12891] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[13404] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[14001] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[14623] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[15162] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[15764] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[16331] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[16930] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[17509] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[18111] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[18682] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[19280] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[19850] = [f(fx.blackout)]  # 1
    script[19852] = [f(fx.random, color_brgbw=[255, 255, 255, 255, 255], splittime=0.02, laps=6, reverse=False)]  # 2
    script[22248] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[22887] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[23446] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[24031] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[24576] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[25203] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[25766] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[26357] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[26980] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[27543] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[28126] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[28754] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[29300] = [f(fx.random, color_brgbw=[255, 255, 255, 255, 255], splittime=0.02, laps=2, reverse=False)]  # 2
    script[29922] = [f(fx.set_all_rgb, values=fx.all(), update=True, autoOff=0.2)]  # space
    script[30253] = [f(fx.set_all_rgb, values=fx.blue(), update=True, autoOff=0.1)]  # space
    script[30450] = [f(fx.set_all_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[30650] = [f(fx.set_all_rgb, values=fx.all(), update=True, autoOff=0.1)]  # space
    script[30891] = [f(fx.set_all_rgb, values=fx.blue(), update=True, autoOff=0.2)]  # space
    script[31091] = [f(fx.set_all_rgb, values=fx.red(), update=True, autoOff=False)]  # space

    #script[31291] = [f(fx.set_all_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    #script[29273] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.02, laps=1, reverse=False)]  # 2


    script[31200] = [f(fx.fade_out, speed=9)]  # space
    script[31700] = [f(fx.fog, intensity=255, duration=0.5)]  # manual
    script[32294] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[33451] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[34652] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[35824] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[37021] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[38179] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[39383] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[40542] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[41727] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[42917] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[44109] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[45256] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[46461] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[47630] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[48828] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[49990] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[51215] = [f(fx.set_all_rgb, values=fx.green(), update=True)]  # space
    script[52364] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[53573] = [f(fx.set_all_rgb, values=fx.red(), update=True)]  # space
    script[54713] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[54950] = [f(fx.set_all_rgb, values=fx.all(), update=True, autoOff=0.1)]  # space
    script[55150] = [f(fx.set_all_rgb, values=fx.blue(), update=True, autoOff=0.1)]  # space
    script[55400] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=12, reverse=False)]
    script[56445] = [f(fx.blackout)]  # 1
    script[56450] = [f(fx.set_all_rgb, values=fx.blue(), update=True)]  # space
    script[56500] = [f(fx.fade_out, speed=15)]  # space
    script[56550] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=12, reverse=True)]
    #script[56439] = [f(fx.racer, color_brgbw=[255, 255, 0, 0, 0], splittime=0.01, laps=8, reverse=True)]


    ## Start the script now
    runScript(file_name=file_name,startpos=startpos,script=script,duration=duration)

