from mylib.helpers import runScript
from time import sleep
from mylib import effects
from mylib.pwmdriver import Servo
import functools

f = functools.partial

def play(**kwargs):
    dmx = kwargs.get("dmx")
    #servo = Servo()
    #servo.set("paule", "open")
    fx = effects.FX(dmx)
    script = {}
    startpos = float(kwargs.get("pos"))
    duration = float(kwargs.get("duration")) if kwargs.get("duration") is not None else None
    fx.uv_off()
    fx.mh_set_start("gobo", rotation=175, tilt=255)
    fx.mh_set_gobo("gobo", "spot")
    fx.mh_set_color("gobo", "darkblue")
    ## Create initial mood
    fx.blackout()

    ## Set filename of music-title
    file_name = "./sounds/Pirates_of_the_Caribbean.mp3"

    ## Here comes the script
    script[1945] = [f(fx.fade_in, color=fx.green_blue(), fixtures="rgb5", stepping=6, step_delay=0.05, end_brightness=255)]  # space
    script[2145] = [f(fx.fade_out, speed=6)]
    script[6168] = [f(fx.fade_in, color=fx.green_blue(), fixtures="rgb4", stepping=6, step_delay=0.05, end_brightness=255)]  # space
    script[8168] = [f(fx.fade_out, speed=6)]
    script[11173] = [f(fx.fade_in, color=fx.green_blue(), fixtures="rgb6", stepping=6, step_delay=0.05, end_brightness=255)]  # space
    script[13173] = [f(fx.fade_out, speed=6)]
    script[16419] = [f(fx.fade_in, color=fx.green_blue(), fixtures=["rgb7","rgb8"], stepping=1, step_delay=0.05, end_brightness=15)]  # space
    script[19545] = [f(fx.blackout)]
    script[19546] = [f(fx.set_rgb, fixtures=["rgb1"], values=fx.green_blue(), update=True, autoOff=False)]  # space
    script[21246] = [f(fx.set_rgb, fixtures=["rgb3"], values=fx.green_blue(), update=True, autoOff=False)]
    script[23036] = [f(fx.set_rgb, fixtures=["rgb2"], values=fx.green_blue(), update=True, autoOff=False)]
    script[24855] = [f(fx.blackout)]
    script[24856] = [f(fx.uv_on)]  # space
    script[24857] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[24857+150] = [f(fx.fade_out, speed=6)]
    script[26536] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[26536+150] = [f(fx.fade_out, speed=6)]
    script[28536] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[28536 + 150] = [f(fx.fade_out, speed=6)]
    script[30132] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[30132+150] = [f(fx.fade_out, speed=6)]
    script[31980] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[31980 + 150] = [f(fx.fade_out, speed=6)]
    script[33638] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[33638 + 150] = [f(fx.fade_out, speed=6)]
    script[35422] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[35422 + 150] = [f(fx.fade_out, speed=6)]

    #script[37222] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[37222] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[37222 + 50] = [f(fx.blackout)]

    #script[37321] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # c
    script[37321] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[37321 + 50] = [f(fx.blackout)]

    #script[37532] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[37532] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[37532 + 50] = [f(fx.blackout)]

    #script[38160] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[38160] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[38160 + 50] = [f(fx.blackout)]

    #script[38354] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[38354] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[38354 + 50] = [f(fx.blackout)]

    #script[38502] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[38502] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[38502 + 50] = [f(fx.blackout)]

    #script[39018] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[39018] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39018 + 50] = [f(fx.blackout)]

    #script[39238] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[39238] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39238 + 50] = [f(fx.blackout)]

    #script[39388] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[39388] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39388 + 50] = [f(fx.blackout)]

    #script[39889] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[39889] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39889 + 50] = [f(fx.blackout)]

    #script[40201] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[40201] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[40201 + 50] = [f(fx.blackout)]

    #script[36381] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    #script[36381 + 50] = [f(fx.blackout)]
    #script[37317] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    #script[37317 + 50] = [f(fx.blackout)]
    #script[38220] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    #script[38220 + 50] = [f(fx.blackout)]
    #script[39072] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    #script[39072 + 50] = [f(fx.blackout)]

    ## Start the script now
    runScript(file_name=file_name,startpos=startpos,script=script,duration=duration)

