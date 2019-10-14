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
    script = {}  # type: Dict[int, Union[List[partial[bool]], List[Union[partial[bool], partial[None]]], List[partial[None]]]]
    startpos = float(kwargs.get("pos"))
    duration = float(kwargs.get("duration")) if kwargs.get("duration") is not None else None

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

    script[30061] = [f(fx.set_all_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # nach-oben
    script[30161] = [f(fx.fade_out, speed=20)]
    script[44855] = [f(fx.set_all_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # nach-oben
    script[44955] = [f(fx.fade_out, speed=20)]


    color_rotate_off_delay = 1100
    script[27492] = [f(fx.mh_set_start, fixture="gobo", rotation=0, tilt=0),
                     f(fx.mh_set_color, fixture="gobo", name="purple"),
                     f(fx.mh_set_gobo, fixture="gobo", name="spot")]   # n

    script[30492] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[30492 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[34177] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=0, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[34177 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[38117] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[38117 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[41552] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=0, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[41552 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[45232] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[45232 + color_rotate_off_delay - 200] = [f(fx.mh_color_rotate_off, fixture="gobo"),
                                              f(fx.mh_set_color, fixture="gobo", name="red")]  # n

    script[48994] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=0, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[48994 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[52815] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # n
    script[52815 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[56356] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=0, speed=70, update=True),
                     f(fx.mh_color_rotate_on, fixture="gobo", speed=255)]  # m
    script[56356 + color_rotate_off_delay] = [f(fx.mh_color_rotate_off, fixture="gobo")]  # n

    script[18508] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[22549] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[26116] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[29288] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.4)]  # space

    script[59603] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=115, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="orange", speed=70),
                     f(fx.mh_set_gobo, fixture="gobo", name="puzzle")]  # n
    script[63322] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=115, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="violet", speed=70)]  # n
    script[66972] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=115, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="green", speed=70)]  # n
    script[70702] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=115, speed=165, update=True),
                     f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # n

    ## Start the script now
    runScript(file_name=file_name, startpos=startpos, script=script, duration=duration)
