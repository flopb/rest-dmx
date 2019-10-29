from functools import partial
from typing import Dict, List, Union

from mylib.helpers import runScript
from time import sleep
from mylib import effects
from mylib.pwmdriver import Servo
import functools


def play(**kwargs):
    ## Default settings, always usable
    dmx = kwargs.get("dmx")
    f = functools.partial
    fx = effects.FX(dmx)
    script = {}
    startpos = float(kwargs.get("pos"))
    duration = float(kwargs.get("duration")) if kwargs.get("duration") is not None else None
    s = Servo()
    ## System initial settings, change according to song
    ## Create initial mood

    fx.uv_off()
    fx.mh_set_start("gobo", rotation=0, tilt=0)
    fx.mh_set_gobo("gobo", "spot")
    fx.mh_set_color("gobo", "darkblue")
    fx.blackout()

    ## Set filename of music-title
    file_name = "./sounds/LMFAO_party_rock_anthem.mp3"

    ## Here comes the script
    #Singer
    silent = [350, 500]
    medium = [300, 450]
    loud = [150, 350]
    script["a30498"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a33700"] = [f(s.stop, who=["paulinchen"])]  # z

    script["a34103"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a37429"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a38036"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a41166"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a41537"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a44512"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a45397"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a48351"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a48831"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a52167"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a52712"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a55951"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a56246"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a57961"] = [f(s.stop, who=["paulinchen"])]  # z

    script["a18488"] = [f(s.speak, who=["paolo"], minmax=loud)]  # s
    script["a19366"] = [f(s.stop, who=["paolo"])]  # z
    script["a22372"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a22887"] = [f(s.stop, who=["paolo"])]  # z
    script["a26084"] = [f(s.speak, who=["paolo"], minmax=loud)]  # s
    script["a26566"] = [f(s.stop, who=["paolo"])]  # z
    script["a29284"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a29566"] = [f(s.stop, who=["paolo"])]  # z

    script["a74714"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a75992"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a76115"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a77741"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a77889"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a81414"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a81731"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a83424"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a83809"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a87052"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a87204"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a88939"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a89101"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a103817"] = [f(s.stop, who=["paolo"])]  # z
    script["a104443"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a107514"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a107990"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a111095"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a111657"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a114874"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a115323"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a118454"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a119008"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a122282"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a122687"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a125806"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a126515"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a129698"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a130143"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a131732"] = [f(s.stop, who=["paulinchen"])]  # z

    script["a132914"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a133538"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a135219"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a136872"] = [f(s.stop, who=["paolo"])]  # z

    script["a150053"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a151411"] = [f(s.stop, who=["paolo"])]  # z

    script["a152278"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a153199"] = [f(s.stop, who=["paolo"])]  # z
    script["a153502"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a155287"] = [f(s.stop, who=["paolo"])]  # z
    script["a155582"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a157839"] = [f(s.stop, who=["paolo"])]  # z
    script["a158325"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a159238"] = [f(s.stop, who=["paolo"])]  # z
    script["a159467"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a164102"] = [f(s.stop, who=["paolo"])]  # z
    script["a164252"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a165942"] = [f(s.stop, who=["paolo"])]  # z
    script["a166175"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a166810"] = [f(s.stop, who=["paolo"])]  # z

    script["a166717"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a167168"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a167558"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a168190"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a168434"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a170023"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a170181"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a170926"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a171151"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a171955"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a172127"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a173709"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a173917"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a174538"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a174824"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a175638"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a175831"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a177387"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a177641"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a179260"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a179466"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a181223"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a181376"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a196444"] = [f(s.stop, who=["paulinchen"])]  # z

    script["a196637"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a199830"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a200316"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a203580"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a203974"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a207186"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a207576"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a211194"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a213109"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a214266"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a216398"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a218279"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a220125"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a221909"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a223857"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a225392"] = [f(s.stop, who=["paulinchen"])]  # z

    script["a226622"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a227184"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a227556"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a229605"] = [f(s.stop, who=["paulinchen"])]  # z

    script["a232159"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a233078"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a235641"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a236675"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a239422"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a240399"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a246977"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a247326"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a250530"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a250982"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a254620"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a254875"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a257963"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a258982"] = [f(s.stop, who=["paulinchen"])]  # z

    script[580] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[1069] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[1475] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[1882] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[2319] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[2775] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[3236] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[3704] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[4159] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[4590] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[5056] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[5517] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[5992] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[6477] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[6936] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[7380] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[7835] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[8309] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[8793] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[9231] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[9693] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[10159] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[10655] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[11080] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[11542] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[12033] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[12499] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[12949] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[13397] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[13860] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[14307] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[14762] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten
    script[15252] = [f(fx.set_floor_rgb, values=fx.white_green(), update=True, autoOff=0.1)]  # nach-unten

    script[2361] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=0.1)]  # space
    script[4103] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=0.1)]  # space
    script[5992] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=0.1)]  # space
    script[7865] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=0.1)]  # space
    script[9755] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=0.1)]  # space
    script[11572] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=0.1)]  # space
    script[13420] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=0.1)]  # space
    script[15292] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=0.1)]  # space

    script[8354] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[8943] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[9186] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[9324] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[10502] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[10819] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[10977] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[11158] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[12354] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[12664] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[12837] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[12984] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[14188] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[14523] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[14700] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[14885] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(80), update=True, autoOff=0.1)]  # l
    script[15331] = [f(fx.set_all_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # nach-oben
    script[15431] = [f(fx.fade_out, speed=20)]

    script[18948] = [f(fx.set_floor_rgb, values=fx.orange(70), update=True, autoOff=False)]  # nach-unten
    script[18948 + 400] = [f(fx.off, fixtures=["rgb7", "rgb8"])]  # nach-unten
    script[22413] = [f(fx.set_floor_rgb, values=fx.orange(70), update=True, autoOff=False)]  # nach-unten
    script[22413 + 400] = [f(fx.off, fixtures=["rgb7", "rgb8"])]  # nach-unten
    script[25967] = [f(fx.set_floor_rgb, values=fx.orange(70), update=True, autoOff=False)]  # nach-unten
    script[25967 + 400] = [f(fx.off, fixtures=["rgb7", "rgb8"])]  # nach-unten
    script[30013] = [f(fx.set_floor_rgb, values=fx.orange(70), update=True, autoOff=False)]  # nach-unten
    script[59568] = [f(fx.off, fixtures=["rgb7", "rgb8"])]

    script[12000] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255),
                     f(fx.mh_set_gobo, fixture="gobo", name="jspiral")]  # space
    script[13521] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=220, update=True)]
    script[13544] = [f(fx.mh_strobe, fixture="gobo", color="darkblue", speed=40)]
    script[14544] = [f(fx.mh_strobe, fixture="gobo", color="darkblue", speed=50)]
    script[15544] = [f(fx.mh_strobe, fixture="gobo", color="darkblue", speed=60)]
    script[16544] = [f(fx.mh_strobe, fixture="gobo", color="darkblue", speed=70)]
    script[17544] = [f(fx.mh_strobe, fixture="gobo", color="darkblue", speed=80)]
    script[18744] = [f(fx.mh_strobe_off, fixture="gobo"),
                     f(fx.mh_set_gobo, fixture="gobo", name="spiral")]

    script[15366] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[15703] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[16008] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[16409] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[16828] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[17142] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[17522] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[17856] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[18290] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[18684] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[18977] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[19383] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[19721] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[20122] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[20517] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[20802] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[21205] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[21517] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[21968] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[22418] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[22704] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[23060] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[23403] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[23826] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[24245] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[24517] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[24902] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[25211] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[25652] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[26075] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[26334] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[26711] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[27047] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[27568] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[27922] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[28227] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[28573] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[28905] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[29359] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[29755] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[30031] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[30436] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[30744] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[31240] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[31625] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[31868] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[32281] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[32618] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[33035] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[33422] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[33708] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[34090] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[34471] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[34927] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[35294] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[35591] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[35984] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[36279] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[36734] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[37179] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[37432] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[37834] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[38173] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[38620] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[39010] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[39272] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[39681] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[40026] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[40522] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[40836] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[41150] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[41533] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[41817] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[42334] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[42692] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[42951] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[43324] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[43655] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[44180] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[44521] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[44758] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[45147] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[45594] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[46020] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[46447] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[46739] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[47110] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[47359] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[47888] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[48231] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[48501] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[48917] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[49229] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[49715] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[50126] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[50401] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[50765] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[51152] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[51612] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[51918] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[52231] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[52566] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[52938] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[53431] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[53800] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[54059] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[54461] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[54789] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[55230] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[55649] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[55903] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # b
    script[56306] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(), update=True, autoOff=0.1)]  # c
    script[56642] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(), update=True, autoOff=0.1)]  # v
    script[57103] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.white(), update=True, autoOff=0.1)]  # c

    #clap
    script[44978] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[45336] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[45790] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[46230] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[46695] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[47154] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[47609] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[48083] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[48525] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[48978] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[49454] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[49928] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[50362] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[50829] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[51278] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[51741] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[52197] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[52651] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[53114] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[53572] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[54046] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[54494] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[54957] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[55406] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[55864] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[56320] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[56792] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[57262] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space

    script[30061] = [f(fx.set_front_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # nach-oben
    script[30161] = [f(fx.fade_out, fixtures=["rgb4","rgb5","rgb6"], speed=20)]
    script[44855] = [f(fx.set_front_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # nach-oben
    script[44955] = [f(fx.fade_out, fixtures=["rgb4","rgb5","rgb6"], speed=20)]


    color_rotate_off_delay = 1100
    script[27492] = [f(fx.mh_set_start, fixture="gobo1", rotation=8, tilt=100),
                     f(fx.mh_set_start, fixture="gobo2", rotation=255, tilt=155),
                     f(fx.mh_set_color, fixture="gobo", name="purple"),
                     f(fx.mh_set_gobo, fixture="gobo", name="spot")]   # n

    script[30492] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[30492 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[34177] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[34177 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[38117] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[38117 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[41552] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[41552 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[45232] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[45232 + color_rotate_off_delay - 200] = [f(fx.mh_color_rotate_off, fixture="gobo"),
                                              f(fx.mh_set_color, fixture="gobo", name="red")]  # n

    script[48994] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[48994 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[52815] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[52815 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[56356] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[56356 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[18508] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[22549] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[26116] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[29288] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.4)]  # space

    script[59603] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=165, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=100, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="orange", speed=70),
                     f(fx.mh_set_gobo, fixture="gobo", name="puzzle")]  # n
    script[63322] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=155, speed=165, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=100, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="violet", speed=70)]  # n
    script[66972] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=165, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=100, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="green", speed=70)]  # n
    script[70702] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=155, speed=165, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=100, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # n


    script[72555] = [f(fx.set_front_rgb, values=fx.white_blue(), update=True, autoOff=0.2)]  # space
    script[72906] = [f(fx.set_front_rgb, values=fx.white_blue(), update=True, autoOff=0.2)]  # space
    script[73256] = [f(fx.set_front_rgb, values=fx.white_blue(), update=True, autoOff=0.2)]  # space
    script[73658] = [f(fx.set_front_rgb, values=fx.white_blue(), update=True, autoOff=0.2)]  # space
    script[74077] = [f(fx.set_front_rgb, values=fx.white_blue(), update=True, autoOff=False),
                     f(fx.mh_off),
                     f(fx.fade_out, speed=20)]  # space

    brightness = 100
    script[74614] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1),
                     f(fx.set_floor_rgb, values=fx.orange(70), update=True, autoOff=False)]  # v
    script[74819] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[75325] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[75577] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[75694] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[76266] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[76476] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[76597] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[76738] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[76954] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[77175] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[77411] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[77621] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[78084] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[78364] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[78564] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[79001] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[79372] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[79949] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[80086] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[80288] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[80444] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[80639] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[80790] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[80991] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[81283] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c

    script[81720] = [f(fx.set_rgb, fixtures=["rgb3"], values=fx.white_blue(brightness), update=True, autoOff=0.3)]  # c
    script[82030] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[82237] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[82676] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[82933] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[83145] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[83578] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[83885] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[84099] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[84363] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[84580] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[84743] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[84955] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[85492] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[85699] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[85899] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[86123] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[86356] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[86762] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[87223] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[87490] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[87825] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[88292] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[88508] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[88619] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b

    script[89248] = [f(fx.off, fixtures=["rgb7", "rgb8"]),
                     f(fx.set_rgb, fixtures=["rgb3"], values=fx.orange(brightness), update=True, autoOff=False)]  # c
    script[89469] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[89676] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[89863] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[90139] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[90256] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[90578] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[90787] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[91002] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[91441] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[91644] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[91897] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[92199] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[92416] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[92597] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[92843] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[93073] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[93304] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[93728] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[94262] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[94486] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[94704] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[95151] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[95378] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[95832] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[96056] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[96254] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[96491] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[96969] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[97207] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[97449] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[97950] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[98289] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[98564] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[98995] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[99242] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[99783] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[99919] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[100222] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[100483] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[100772] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[100984] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[101210] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # v
    script[101650] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # c
    script[102004] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.orange(brightness), update=True, autoOff=0.1)]  # b
    script[103888] = [f(fx.fade_out, fixtures=["rgb3"])]  # right shift

    #######REFRAIN
    color_rotate_off_delay = 1100
    deltatime = 101187-27492
    script[27492+deltatime] = [f(fx.mh_set_start, fixture="gobo1", rotation=8, tilt=100),
                     f(fx.mh_set_start, fixture="gobo2", rotation=255, tilt=155),
                     f(fx.mh_set_color, fixture="gobo", name="purple"),
                     f(fx.mh_set_gobo, fixture="gobo", name="spot")]  # n

    script[30492+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[30492+deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[34177+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[34177+deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[38117+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[38117+deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[41552+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[41552+deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[45232+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[45232+deltatime + color_rotate_off_delay - 200] = [f(fx.mh_color_rotate_off, fixture="gobo"),
                                                    f(fx.mh_set_color, fixture="gobo", name="red")]  # n

    script[48994+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[48994+deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[52815+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[52815+deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[56356+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[56356+deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    #script[18508+deltatime] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    #script[22549+deltatime] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    #script[26116+deltatime] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[29288+deltatime] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=False),
                               f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3"], speed=10)]  # space

    deltatime += 4000
    script[59603+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=165, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=100, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="orange", speed=70),
                     f(fx.mh_set_gobo, fixture="gobo", name="puzzle")]  # n
    script[63322+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=155, speed=165, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=100, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="violet", speed=70)]  # n
    script[66972+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=165, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=100, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="green", speed=70)]  # n
    script[70702+deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=155, speed=165, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=100, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # n

    script[104286] = [f(fx.set_rgb, fixtures=["rgb7","rgb8"], values=fx.orange(brightness), update=True, autoOff=False)] # v

    script[107509] = [f(fx.set_front_rgb, values=fx.white_blue(brightness), update=True, autoOff=0.2)]  # c
    script[111143] = [f(fx.set_front_rgb, values=fx.white_blue(brightness), update=True, autoOff=0.2)]  # c
    script[118208] = [f(fx.set_front_rgb, values=fx.white_blue(brightness), update=True, autoOff=0.2)]  # v

    script[132587] = [f(fx.fade_out, fixtures=["rgb7", "rgb8"]),
                      f(fx.mh_off)]  # right shift
    script[135347] = [f(fx.set_rgb, fixtures=["rgb3"], values=fx.white_blue(brightness), update=True, autoOff=False)]  # c
    script[136990] = [f(fx.fade_out, fixtures=["rgb3"])]  # right shift

    script[150054] = [f(fx.set_rgb, fixtures=["rgb3"], values=fx.white_blue(brightness), update=True, autoOff=False)]  # c
    script[151424] = [f(fx.fade_out, fixtures=["rgb3"])]  # right shift

    script[152001] = [f(fx.mh_off), f(fx.set_rgb, fixtures=["rgb3"], values=fx.orange(brightness), update=True, autoOff=False)]  # nach-unten
    script[159059] = [f(fx.fade_out, fixtures=["rgb3"])]  # right shift
    script[159287] = [f(fx.set_rgb, fixtures=["rgb3"], values=fx.green(brightness), update=True, autoOff=False)]  # c

    script[151888] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[152241] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[152593] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[153020] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[153511] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[153791] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[154144] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[154489] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[154964] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[155364] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[155614] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[155986] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[156322] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[156777] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[157171] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[157378] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[157602] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[158523] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[158762] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[159333] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[159653] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[159998] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[160634] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[160941] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[161196] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[161535] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[161854] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[162301] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[162687] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[162822] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[163043] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[163364] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[163723] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[164128] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[164648] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[164764] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[164946] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[165263] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[165578] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[165960] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[166279] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[166692] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[167069] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[167390] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[167853] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[168300] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[168563] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[168904] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[169192] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[169696] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[170107] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[170410] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[170736] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[171108] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[171513] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[171900] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[172265] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[172580] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[172959] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[173432] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[173855] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[174108] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[174423] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[174763] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[175040] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[175413] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[175935] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[176235] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[176584] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[177074] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[177496] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[177783] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[178127] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[178461] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[179111] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[179428] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[179666] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[180013] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[180298] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[180761] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[181203] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[181525] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[181859] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[182243] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[182436] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[182737] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[183071] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[183315] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[183680] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[184017] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[184246] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[184607] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[184975] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[185180] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[185518] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[185875] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[186077] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[186427] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[186779] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[186986] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[187350] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[187705] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[187937] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[188283] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[188615] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[188855] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[189214] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[189564] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[189781] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[190130] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[190527] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[190737] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[191040] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[191418] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[191637] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[191952] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[192335] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[192549] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[192896] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[193287] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[193494] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[193822] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[194236] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[194441] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[194738] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[195153] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[195387] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[195691] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # v
    script[196065] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[196312] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b

    script[166720] = [f(fx.off, fixtures=["rgb3"]), f(fx.rgb_pulse, fixtures=["rgb7", "rgb8"], color="purple", speed=236)]
    script[177680] = [f(fx.set_rgb, fixtures=["rgb3"], values=fx.green(), update=True, autoOff=0.2)]  # c
    script[192590] = [f(fx.rgb_pulse, fixtures=["rgb3"], color="green", speed=236)]
    script[196621] = [f(fx.off, fixtures=[ "rgb3", "rgb3", "rgb7", "rgb8"])]

    #######REFRAIN
    color_rotate_off_delay = 1100
    deltatime = 193721 - 27492
    script[27492 + deltatime] = [f(fx.mh_set_start, fixture="gobo1", rotation=8, tilt=100),
                                 f(fx.mh_set_start, fixture="gobo2", rotation=255, tilt=155),
                                 f(fx.mh_set_color, fixture="gobo", name="purple"),
                                 f(fx.mh_set_gobo, fixture="gobo", name="spot")]  # n

    script[30492 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                                 f(fx.mh_color_rotate_on, fixture="gobo", speed=255),
                                 f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=False),
                                 f(fx.fade_out, fixtures=["rgb4", "rgb5", "rgb6"], speed=2)]  # n
    script[30492 + deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[34177 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                                 f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[34177 + deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[38117 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                                 f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[38117 + deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[41552 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                                 f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[41552 + deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[45232 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                                 f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[45232 + deltatime + color_rotate_off_delay - 200] = [f(fx.mh_color_rotate_off, fixture="gobo"),
                                                                f(fx.mh_set_color, fixture="gobo", name="red")]  # n

    script[48994 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                                 f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[48994 + deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[52815 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=70, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=99, speed=70, update=True),
                                 f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[52815 + deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[56356 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=99, speed=70, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=162, speed=70, update=True),
                                 f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[56356 + deltatime + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    # script[18508+deltatime] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    # script[22549+deltatime] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    # script[26116+deltatime] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[29288 + deltatime] = [f(fx.set_back_rgb, values=fx.orange(), update=True, autoOff=False),
                                 f(fx.fade_out, fixtures=["rgb1", "rgb2", "rgb3"], speed=10)]  # space

    deltatime += 4000
    script[59603 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=165, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=100, speed=165, update=True),
                                 f(fx.mh_strobe, fixture="gobo", color="orange", speed=70),
                                 f(fx.mh_set_gobo, fixture="gobo", name="puzzle")]  # n
    script[63322 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=155, speed=165, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=100, speed=165, update=True),
                                 f(fx.mh_strobe, fixture="gobo", color="violet", speed=70)]  # n
    script[66972 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=165, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=100, speed=165, update=True),
                                 f(fx.mh_strobe, fixture="gobo", color="green", speed=70)]  # n
    script[70702 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=155, speed=165, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=100, speed=165, update=True),
                                 f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # n

    script[74352 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=165, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=100, speed=165, update=True),
                                 f(fx.mh_strobe, fixture="gobo", color="green", speed=70)]  # n
    script[78082 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=155, speed=165, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=100, speed=165, update=True),
                                 f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # n

    script[81732 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=155, speed=165, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=8, tilt=100, speed=165, update=True),
                                 f(fx.mh_strobe, fixture="gobo", color="green", speed=70)]  # n
    script[85462 + deltatime] = [f(fx.mh_move_to, fixture="gobo1", rotation=8, tilt=155, speed=165, update=True),
                                 f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=100, speed=165, update=True),
                                 f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # n

    script[200001] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[200264] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[200399] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[200646] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[200843] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[201178] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[201294] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[201544] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[201769] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[202118] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[202211] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[202498] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[202708] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[203055] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[203139] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[203436] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[203642] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[203999] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[204101] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[204348] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[204532] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[204903] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[205028] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[205241] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[205467] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[205803] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[205928] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[206154] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[206354] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[206712] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[206819] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[207060] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[207294] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[207635] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[207743] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[207994] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[208244] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[208581] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[208697] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[208944] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[209174] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[209479] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[209600] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[209856] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[210069] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[210434] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[210560] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[210811] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[210994] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[211358] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[211477] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[211714] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[211918] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[212239] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[212380] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[212628] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[212825] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[213181] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[213316] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[213563] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[213779] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[214110] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[214213] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[214486] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[214688] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[215033] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[215131] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[215202] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[215434] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[215645] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[216008] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[216467] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[216732] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[216936] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[217228] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[217473] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[217839] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[218387] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[218600] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[218832] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[219058] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[219308] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[219642] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[220095] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[220396] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[220522] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[220762] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[220955] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[221172] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[221546] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[222103] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[222341] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[222554] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[222755] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[223025] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.green(brightness), update=True, autoOff=0.1)]  # c
    script[223341] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.red(brightness), update=True, autoOff=0.1)]  # b
    script[223823] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[224092] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[224244] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[224476] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[224652] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b
    script[224830] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.red(brightness), update=True, autoOff=0.1)]  # c
    script[225191] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.green(brightness), update=True, autoOff=0.1)]  # b

    script[225769] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # c
    script[226028] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # b
    script[226215] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # c
    script[226484] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # b
    script[226724] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # c
    script[227078] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # b
    script[227176] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # c
    script[227460] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # b
    script[227665] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.yellow(brightness=30), update=True, autoOff=0.1)]  # c

    script[229521] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[229724] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[229971] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[230154] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[230416] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[230654] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[230843] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[231072] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[231330] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[231549] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[231789] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[231993] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[232245] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[232489] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[232718] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[232913] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[233168] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[233390] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[233624] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[233850] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[234107] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[234308] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[234559] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[234763] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[235024] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[235240] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[235486] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[235706] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[235926] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[236155] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[236390] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[236602] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[236865] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[237089] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[237300] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[237540] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[237762] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[237999] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[238190] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[238455] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[238690] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[238920] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[239183] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[239368] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[239639] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[239871] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[240108] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[240314] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[240564] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[240748] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[240996] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[241248] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[241469] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[241672] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[241940] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[242157] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[242433] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[242640] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[242861] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[243089] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[243316] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[243544] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[243766] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[244000] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[244240] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[244464] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[244681] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[244922] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[245151] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[245373] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[245637] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[245824] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[246107] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[246303] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[246549] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[246751] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[247021] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[247260] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[247479] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[247722] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[247992] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[248188] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[248420] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[248635] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[248865] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[249130] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[249303] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[249534] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[249787] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[249990] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[250236] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[250425] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[250707] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[250904] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[251151] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[251390] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[251613] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[251808] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[252065] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[252283] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[252517] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[252748] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[252953] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[253238] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[253462] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[253691] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[253920] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[254139] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[254391] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[254620] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[254856] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[255058] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[255323] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[255536] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[255793] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[255974] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[256251] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[256473] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[256728] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[256901] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[257175] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[257380] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[257632] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[257866] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[258063] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[258261] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[258546] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[258756] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c
    script[258997] = [f(fx.set_rgb, fixtures=["rgb8"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # b
    script[259263] = [f(fx.set_rgb, fixtures=["rgb7"], values=fx.white_blue(brightness), update=True, autoOff=0.1)]  # c

    script[259000] = [f(fx.set_all_rgb, values=fx.white_blue(), update=True, autoOff=False),
                      f(fx.mh_off),
                      f(fx.fade_out, speed=5)]  # space

    ## Start the script now
    runScript(file_name=file_name, startpos=startpos, script=script, duration=duration, dmx=dmx)
