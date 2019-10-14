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

    #1/4

    #2/4

    ## Start the script now
    runScript(file_name=file_name, startpos=startpos, script=script, duration=duration)
