from mylib.helpers import runScript
from time import sleep
from mylib import effects
from mylib.pwmdriver import Servo
import functools

f = functools.partial

def play(**kwargs):
    ## Default settings, always usable
    dmx = kwargs.get("dmx")
    fx = effects.FX(dmx)
    script = {}
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
    file_name = "./sounds/Culcha_Candela_Monsta.mp3"

    ## Here comes the script
    script[1378] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[1951] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[2528] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[2987] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[3668] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[4282] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[4768] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[5247] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[5439] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[5682] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[5884] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[6101] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[6146] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[6584] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[7302] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[7966] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[8000] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[8195] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    #Flash
    script[8196] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[8392] = [f(fx.set_front_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[8592] = [f(fx.blackout)]
    #
    script[9146] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[9803] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[10238] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[10915] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[11600] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[12062] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[12713] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[13422] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[13876] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[14522] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[15202] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    #Flash
    script[15636] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False)]
    script[15936] = [f(fx.fade_out, fixtures=["rgb4", "rgb5", "rgb6"], speed=11)]
    #
    script[16313] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[17032] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[17437] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[18158] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[18778] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[19248] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[19956] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[20646] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[21087] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[21787] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[22386] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[22471] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[22662] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[22883] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[23636] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[24267] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[24654] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[24696] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[25099] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[25572] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[26004] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[26433] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[26875] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[27363] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[27801] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[28241] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[28674] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[29144] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[29594] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[30068] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[30516] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[30961] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[31417] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[31840] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[32296] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[32756] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[33220] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[33700] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[34149] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[34596] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[35049] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[35484] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[35920] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[36358] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[36806] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[37258] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[37706] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[38198] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[38646] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[39106] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[39543] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[39975] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[40405] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[40862] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[41327] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[41771] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[42200] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[42645] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[43084] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[43532] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[43976] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[44429] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[44906] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[45394] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[45824] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[46290] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[46754] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[47191] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[47655] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[48126] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[48576] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[49015] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[49455] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[49891] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[50347] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[50779] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[51244] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[51709] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[52169] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[52621] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[53074] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[53550] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[53998] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[54414] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[54871] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[55317] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[55796] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[56248] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[56673] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[57135] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[57585] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[58015] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[58479] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[58903] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[59363] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    # Gobo fahrt
    script[57410] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]  # space
    script[59385] = [f(fx.blackout)]  # space
    script[59390] = [f(fx.set_rgb, fixtures=["rgb1", "rgb2","rgb3"], values={"4": 255, "5": 0, "6": 0, "7": 255, "8": 0})]  # space
    script[59394] = [f(fx.mh_move_to, fixture="gobo1", rotation=175, tilt=110, speed=150, update=True)]  # space
    script[60299] = [f(fx.mh_move_to, fixture="gobo2", rotation=175, tilt=110, speed=140, update=True)]  # space
    script[61090] = [f(fx.mh_set_color, fixture="gobo", name="red")]
    script[61184] = [f(fx.set_rgb, fixtures=["rgb1", "rgb2", "rgb3"], values={"4": 0})]  # space
    script[61185] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values={"4": 255, "5": 255, "6": 0, "7": 0, "8": 0})]  # space
    script[61192] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=182, update=True)]  # space
    script[62546] = [f(fx.mh_off, fixture="gobo")]
    script[62547] = [f(fx.blackout)]
    script[62548] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[63004] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[63437] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[63885] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[64362] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[64815] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[65247] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[65697] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[66144] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[66625] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[67071] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[67518] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[67954] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[68422] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[68869] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[69299] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[69765] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[70231] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[70653] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[71098] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[71581] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[72020] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[72470] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[72910] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[73351] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[73812] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[74278] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[74739] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[75199] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[75651] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[76110] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[76578] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[77004] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[77473] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[77911] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[78345] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[78796] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[79260] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[79711] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[80154] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[80636] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[81093] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[81515] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[81949] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[82411] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[82873] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[83335] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[83773] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[84222] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[84657] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[85121] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[85582] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[86035] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[86502] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[86937] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[87362] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[87808] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[88289] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[88753] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[89200] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[89637] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[90070] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[90520] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[90972] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[91448] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[91905] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[92349] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[92768] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[93243] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[93683] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[94134] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[94566] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[95036] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[95508] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[95962] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[96411] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[96869] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[97318] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[97776] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[98214] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[98652] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[99107] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[99585] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[100024] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[100467] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[100924] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[101361] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[101807] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[102212] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[102679] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[103146] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[103630] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[104072] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[104500] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[104978] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[105435] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[105870] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[106319] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[106777] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[107265] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[107690] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[108153] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[108572] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[109022] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[109481] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[109947] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[110377] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[110845] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[111289] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[111722] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[112155] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[112615] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[113076] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[113515] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[113959] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[114404] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[114866] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[115296] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[115734] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[116184] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[116673] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[117119] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[117583] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[118053] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[118514] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[118956] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[119404] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[119839] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[120290] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[120718] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[121183] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[121630] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[122080] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[122530] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[122996] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[123444] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[123904] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[124316] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[124777] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[125256] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[125717] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[126150] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[126589] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[127064] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[127517] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[127969] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[128405] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[128837] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[129286] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[129729] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[130198] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[130654] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[131098] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[131538] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[131989] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[132425] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[132897] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[133329] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[133789] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[134263] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[134729] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[135197] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[135666] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[136152] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[136549] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[136981] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[137440] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[137848] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[138289] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[138716] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[139184] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[139701] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[140143] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[140574] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[141062] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[141492] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[141939] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[142403] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[142863] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[143284] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[143732] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[144191] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[144642] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[145094] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[145515] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[145953] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[146397] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[146883] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[147346] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[147799] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[148267] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[148723] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[149145] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[149603] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[150086] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[150526] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[150983] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[151429] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[151899] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[152324] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[152773] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[153212] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[153670] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[154124] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[154579] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[155055] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[155485] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[155937] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[156413] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[156838] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[157265] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[157722] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[158172] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[158634] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[159099] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[159529] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[160000] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[160438] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[160882] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[161353] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[161867] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[162315] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[162733] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[163200] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[163639] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[164088] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[164553] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[164995] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[165449] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[165897] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[166348] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[166771] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[167220] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[167690] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[168124] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[168590] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[169067] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[169499] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[169956] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[170387] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[170838] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[171296] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[171782] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[172187] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[172638] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[173107] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[173569] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[173978] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[174454] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[174903] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[175352] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[175814] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[176257] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[176709] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[177159] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[177620] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[178088] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[178516] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[178957] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[179400] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[179851] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[180279] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[180744] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[181158] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[181624] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[182066] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[182511] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[182964] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[183437] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[183945] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[184360] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[184784] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[185255] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[185715] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[186175] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[186597] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[187055] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[187493] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[187923] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[188382] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[188846] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[189304] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[189748] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[190188] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[190665] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[191118] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[191587] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[192021] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[192468] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[192904] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[193362] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[193803] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[194271] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[194703] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[195149] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[195643] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space

    ## Start the script now
    runScript(file_name=file_name,startpos=startpos,script=script,duration=duration)

