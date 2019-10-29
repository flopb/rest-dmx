from mylib.helpers import runScript
from time import sleep
from mylib import effects
from mylib.pwmdriver import Servo
import functools

f = functools.partial


def play(**kwargs):
    dmx = kwargs.get("dmx")
    # servo = Servo()
    # servo.set("paule", "open")
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
    # fx.sparkle(color=fx.white_blue(), duration=5 , sparkletime=0.1, pause=0.1)
    ## Set filename of music-title
    file_name = "./sounds/Alice_Cooper_Feed_My_Frankenstein.mp3"

    s = Servo()

    ## Here comes the script
    #audio script
    script["a2201"] = [f(s.speak, who=["paulinchen"], minmax=[350,500])]  # d
    script["a4507"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a4762"] = [f(s.speak, who=["paolo"], minmax=[350,500])]  # d
    script["a7247"] = [f(s.stop, who=["paolo"])]  # z
    script["a7980"] = [f(s.speak, who=["paulinchen", "paolo"], minmax=[150,350])]  # d
    script["a12004"] = [f(s.stop, who=["paulinchen", "paolo"])]  # z

    script["a35995"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a40582"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a40712"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a54674"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a55258"] = [f(s.speak, who=["paulinchen", "paolo"], minmax=[300, 450])]  # s
    script["a64127"] = [f(s.stop, who=["paulinchen", "paolo"])]  # z
    script["a64680"] = [f(s.speak, who=["paulinchen"], minmax=[150, 350])]  # a
    script["a68858"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a69496"] = [f(s.speak, who=["paulinchen"], minmax=[350, 500])]  # d
    script["a71519"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a72359"] = [f(s.speak, who=["paolo"], minmax=[300, 450])]  # s
    script["a73592"] = [f(s.stop, who=["paolo"])]  # z
    script["a74119"] = [f(s.speak, who=["paulinchen"], minmax=[150, 350])]  # a
    script["a78301"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a78720"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a82928"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a85798"] = [f(s.speak, who=["paulinchen"], minmax=[350, 500])]  # d
    script["a94756"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a95122"] = [f(s.speak, who=["paulinchen"], minmax=[350, 500])]  # d
    script["a99268"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a99895"] = [f(s.speak, who=["paulinchen"], minmax=[350, 500])]  # d
    script["a103835"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a104080"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a108436"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a108762"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a113822"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a114248"] = [f(s.speak, who=["paulinchen", "paolo"], minmax=[150, 350])]  # a
    script["a121324"] = [f(s.stop, who=["paulinchen", "paolo"])]  # z
    script["a121512"] = [f(s.speak, who=["paolo"], minmax=[300, 450])]  # s
    script["a123122"] = [f(s.stop, who=["paolo"])]  # z
    script["a123678"] = [f(s.speak, who=["paulinchen"], minmax=[150, 350])]  # a
    script["a127736"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a128194"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a132100"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a132550"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a135508"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a135747"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a137815"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a138543"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a141922"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a142071"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a144804"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a145129"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a149340"] = [f(s.stop, who=["paulinchen"])]  # z
    #script["a149505"] = [f(s.speak, who=["paulinchen"], minmax=[150, 350])]  # a

    script["a187829"] = [f(s.speak, who=["paolo"], minmax=[300, 450])]  # s
    script["a189317"] = [f(s.stop, who=["paolo"])]  # z
    script["a201245"] = [f(s.speak, who=["paulinchen"], minmax=[150, 350])]  # a
    script["a205690"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a206147"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a208094"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a209431"] = [f(s.speak, who=["paolo"], minmax=[300, 450])]  # s
    script["a210471"] = [f(s.stop, who=["paolo"], minmax=[300, 450])]  # s

    script["a211017"] = [f(s.speak, who=["paulinchen"], minmax=[150, 350])]  # a
    script["a213011"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a213304"] = [f(s.speak, who=["paulinchen"], minmax=[150, 350])]  # a
    script["a214968"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a215220"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a224410"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a224920"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a229178"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a229415"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s

    script["a231863"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a232406"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a234068"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a234482"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a238475"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a239133"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a241295"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a241584"] = [f(s.speak, who=["paulinchen"], minmax=[300, 450])]  # s
    script["a243287"] = [f(s.stop, who=["paulinchen"])]  # z

    #light script
    script[0] = [f(fx.fog, intensity=255, duration=1.0)]  # manual
    script[7890] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=150)]  # space
    script[10425] = [f(fx.mh_set_color, fixture="gobo", name="red")]
    script[10426] = [f(fx.mh_move_to, fixture="gobo2", rotation=105, tilt=100, speed=200)]
    script[10427] = [f(fx.mh_move_to, fixture="gobo1", rotation=245, tilt=100, speed=200)]
    script[12174] = [f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=60, speed=40)]
    script[12175] = [f(fx.mh_move_to, fixture="gobo1", rotation=0, tilt=60, speed=40)]
    script[12176] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=100)]  # space
    script[12177] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.02, laps=2, reverse=False)]  # 2
    script[12889] = [f(fx.blackout)]  # 1
    script[12890] = [f(fx.mh_off, fixture="gobo", update=True)]
    script[12891] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[13404] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[14001] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[14623] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[15162] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[15764] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[16331] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[16930] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[17509] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[18111] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[18682] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[19280] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[19850] = [f(fx.blackout)]  # 1
    script[19852] = [f(fx.random, color_brgbw=[255, 255, 255, 255, 255], splittime=0.02, laps=6, reverse=False)]  # 2
    script[22247] = [f(fx.blackout)]  # 1
    script[22248] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[22887] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[23446] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[24031] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[24576] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[25203] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[25766] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[26357] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[26980] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[27543] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[28126] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[28754] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[29300] = [f(fx.random, color_brgbw=[255, 255, 255, 255, 255], splittime=0.02, laps=2, reverse=False)]  # 2
    script[29921] = [f(fx.blackout)]  # 1
    script[29922] = [f(fx.set_back_rgb, values=fx.all(), update=True, autoOff=0.2)]  # space
    script[30253] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=0.1)]  # space
    script[30450] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=0.2)]  # space
    script[30650] = [f(fx.set_back_rgb, values=fx.all(), update=True, autoOff=0.1)]  # space
    script[30891] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=0.2)]  # space
    script[31091] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[31200] = [f(fx.fade_out, speed=9)]  # space
    script[31700] = [f(fx.fog, intensity=255, duration=0.5)]  # manual
    script[32294] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[33451] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[34652] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[35824] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[37021] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[38179] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[39383] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[40542] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[41727] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[42917] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[44109] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[45256] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[46461] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[47630] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[48828] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[49990] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[51215] = [f(fx.set_back_rgb, values=fx.green(), update=True)]  # space
    script[52364] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[53573] = [f(fx.set_back_rgb, values=fx.red(), update=True)]  # space
    script[54713] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[54950] = [f(fx.set_back_rgb, values=fx.all(), update=True, autoOff=0.1)]  # space
    script[55150] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=0.1)]  # space
    script[55400] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=12, reverse=False)]
    script[56445] = [f(fx.blackout)]  # 1
    script[56450] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[56500] = [f(fx.fade_out, speed=15)]  # space
    script[54501] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]
    script[56500] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=10, autoOffAfter=0.5)]
    script[56550] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=7, reverse=True)]
    script[62400] = [f(fx.blackout)]  # 1
    script[62399] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[62722] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # c
    script[63198] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # n
    script[63757] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[63840] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # c
    script[63971] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[64224] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[64369] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[64595] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[64748] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[64847] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # c
    script[63847] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]  # space
    script[64849] = [f(fx.blackout)]  # 1
    script[64850] = [f(fx.uv_on)]  # 1
    script[64748] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]  # space
    script[65147] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70)]  # space
    script[66547] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    script[66548] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[66948] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[67749] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=210)]  # space
    script[67750] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=210)]  # space
    script[69249] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=50)]  # space
    script[69250] = [f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=50)]  # space
    script[69351] = [f(fx.set_floor_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[69252] = [f(fx.uv_off)]  # 1
    script[71834] = [f(fx.mh_off, fixture="gobo")]  # 1
    script[71835] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=2, reverse=False)]
    script[71864] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # n
    script[71958] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[72104] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # n
    script[72239] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # c
    script[72403] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # n
    script[72713] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[72852] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[73185] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[73307] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[73401] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[73640] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[73901] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[73900] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]  # space
    script[74193] = [f(fx.mh_set_color, fixture="gobo", name="blue", update="false")]  # 1
    script[74192] = [f(fx.blackout)]  # 1
    script[74193] = [f(fx.uv_on)]  # 1
    script[74194] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]  # space
    script[74819] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70)]  # space
    script[76014] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    script[76015] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[76614] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[77384] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=210)]  # space
    script[77385] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=210)]  # space
    script[78934] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=50)]  # space
    script[78935] = [f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=50)]  # space
    script[79034] = [f(fx.set_floor_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[79035] = [f(fx.uv_off)]  # 1

    script[84174] = [f(fx.mh_off, fixture="gobo")]  # 1
    script[84175] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[85391] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[86579] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[87806] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[88896] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[90103] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[91320] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[92479] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[93646] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[94842] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[96022] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[97233] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[98386] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[99565] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[100754] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[101904] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[103104] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space

    script[104296] = [f(fx.set_back_rgb, values=fx.all(), update=True, autoOff=0.1)]  # space
    script[104549] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=0.1)]  # space
    script[104692] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=12, reverse=False)]
    script[107800] = [f(fx.blackout)]  # 1
    script[108953] = [f(fx.set_back_rgb, values=fx.blue(), update=True)]  # space
    script[108955] = [f(fx.fade_out, speed=20)]  # space
    script[104295] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]
    script[108954] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=10, autoOffAfter=0.5)]
    script[108999] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=7, reverse=True)]
    script[110154] = [f(fx.blackout)]  # 1
    script[110155] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]  # space
    script[110156] = [f(fx.mh_set_color, fixture="gobo", name="darkblue", update=True)]  # 1

    script[111969] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[112431] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[112811] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # n
    script[113390] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # c
    script[113535] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # n
    script[113808] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[114052] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[114175] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[114317] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c

    script[114317] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]  # space
    script[114118] = [f(fx.mh_set_color, fixture="gobo", name="darkblue", update=True)]  # 1
    script[114319] = [f(fx.blackout)]  # 1
    script[114320] = [f(fx.uv_on)]  # 1
    script[114321] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]  # space
    script[114722] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70)]  # space
    script[115922] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    script[115923] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[116522] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[117222] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=210)]  # space
    script[117223] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=210)]  # space
    script[118823] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=50)]  # space
    script[118824] = [f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=50)]  # space
    script[118924] = [f(fx.set_floor_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[118925] = [f(fx.uv_off)]  # 1

    script[121224] = [f(fx.mh_off, fixture="gobo")]  # 1
    script[121225] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]  # space
    script[121226] = [f(fx.mh_set_color, fixture="gobo", name="darkblue", update=True)]  # 1
    script[121227] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=7, reverse=True)]

    script[123227] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=10, autoOffAfter=0.5)]
    script[123627] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=10, autoOffAfter=0.5)]

    script[124828] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    script[124827] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[125927] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[126627] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=210)]  # space
    script[126628] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=210)]  # space
    script[128228] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=50)]  # space
    script[128229] = [f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=50)]  # space
    script[128329] = [f(fx.set_floor_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[128330] = [f(fx.uv_off)]  # 1

    script[130820] = [f(fx.mh_off, fixture="gobo")]  # 1
    script[130821] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=7, reverse=True)]

    script[130819] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]  # space
    script[130820] = [f(fx.mh_set_color, fixture="gobo", name="darkblue", update=True)]  # 1
    script[130821] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=7, reverse=True)]

    script[132821] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=10, autoOffAfter=0.5)]
    script[133221] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=10, autoOffAfter=0.5)]

    script[134421] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    script[134422] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[135521] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[136221] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=210)]  # space
    script[136222] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=210)]  # space
    script[137822] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=50)]  # space
    script[137823] = [f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=50)]  # space

    script[140190] = [f(fx.mh_off, fixture="gobo"),
                      f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255, speed=0),
                      f(fx.racer, color_brgbw=[255, 255, 0, 0, 0], splittime=0.017, laps=7, reverse=True),
                      f(fx.mh_set_color, fixture="gobo", name="darkblue", update=True),
                      ]  # space
    script[142632] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=10, autoOffAfter=0.5)]
    script[143232] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=10, autoOffAfter=0.5)]

    script[144332] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    script[143333] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[143334] = [f(fx.mh_set_color, fixture="gobo", name="red")]  # space
    script[145014] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=60)]  # space
    script[145015] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=60)]  # space
    script[145586] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=60)]  # space
    script[145587] = [f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=60)]  # space
    script[146160] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=60)]  # space
    script[146161] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=60)]  # space

    # script[134421] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    # script[134422] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[147346] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[147347] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=170, speed=210)]  # space
    script[147346] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=170, speed=210)]  # space

    script[149577] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=7, reverse=True),
                      f(fx.mh_off, fixture="gobo")]

    # script[152065] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[153116] = [f(fx.sparkle, color=fx.white_blue(), duration=0.3, sparkletime=0.05, pause=0)]  # space
    script[154119] = [f(fx.sparkle, color=fx.red(), duration=0.6, sparkletime=0.05, pause=0)]
    script[155221] = [f(fx.sparkle, color=fx.white_blue(), duration=0.3, sparkletime=0.05, pause=0)]
    script[156119] = [f(fx.sparkle, color=fx.red(), duration=1.2, sparkletime=0.05, pause=0)]
    script[157676] = [f(fx.sparkle, color=fx.white_blue(), duration=0.3, sparkletime=0.05, pause=0)]  # space
    script[158119] = [f(fx.sparkle, color=fx.red(), duration=0.6, sparkletime=0.05, pause=0)]
    script[159676] = [f(fx.sparkle, color=fx.white_blue(), duration=1.5, sparkletime=0.05, pause=0)]  # space
    script[161376] = [f(fx.kitt, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.white_blue(), pausetime=0.03)]  # space
    script[161876] = [f(fx.blackout)]
    script[162276] = [f(fx.kitt, fixtures=["rgb6", "rgb5", "rgb4"], color=fx.white_blue(), pausetime=0.03)]  # space
    script[162776] = [f(fx.blackout)]

    script[163486] = [f(fx.kitt, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.white_blue(), pausetime=0.03)]  # space
    script[163986] = [f(fx.blackout)]
    script[164586] = [f(fx.kitt, fixtures=["rgb6", "rgb5", "rgb4"], color=fx.white_blue(), pausetime=0.03)]  # space
    script[165086] = [f(fx.blackout)]
    script[165586] = [f(fx.kitt, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.white_blue(), pausetime=0.03)]  # space
    script[166086] = [f(fx.blackout)]
    script[166886] = [f(fx.kitt, fixtures=["rgb6", "rgb5", "rgb4"], color=fx.white_blue(), pausetime=0.03)]  # space
    script[167370] = [f(fx.blackout)]

    script[167371] = [f(fx.sparkle, color=fx.white_blue(), duration=3.3, sparkletime=0.05, pause=0)]

    script[170905] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # space
    script[171205] = [f(fx.fade_out, speed=10)]  # space
    script[172049] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[172222] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[172406] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[172564] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[172718] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # space
    script[172818] = [f(fx.fade_out, speed=20)]  # space
    script[173282] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[173555] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[173743] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[173913] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[174072] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[174264] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[174488] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[174732] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[174977] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # space
    script[175210] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # space
    script[175310] = [f(fx.fade_out, speed=20)]

    script[175864] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=False)]
    script[176164] = [f(fx.fade_out, speed=10)]
    script[176843] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # c
    script[177015] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # n
    script[177198] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=0.1)]  # c
    script[177416] = [f(fx.set_back_rgb, values=fx.white_blue(), update=True, autoOff=False)]  # n
    # script[178172] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[177516] = [f(fx.fade_out, speed=10, limit=50)]
    script[177716] = [f(fx.fade_in, fixtures=["rgb1", "rgb2", "rgb3"], color=fx.white_blue(), start_brightness=50, end_brightness=200, stepping=5)]
    script[177816] = [f(fx.fade_out, speed=10, limit=50)]
    script[177916] = [f(fx.fade_in, fixtures=["rgb1", "rgb2", "rgb3"], color=fx.white_blue(), start_brightness=50, end_brightness=200, stepping=10)]
    script[178016] = [f(fx.fade_out, speed=10)]

    script[178017] = [f(fx.mh_set_start, fixture="gobo1", rotation=175, tilt=255, update=False),
                      f(fx.mh_set_color, fixture="gobo", name="red", update=False),
                      f(fx.mh_set_gobo, fixture="gobo", name="bubbles", update=True)]  # space

    script[180356] = [f(fx.set_front_rgb, values=fx.white_red(), update=True, autoOff=False)]  # space
    script[180456] = [f(fx.fade_out, speed=5)]
    script[181456] = [f(fx.sparkle, color=fx.red(), duration=0.7, sparkletime=0.05, pause=0)]
    script[182856] = [f(fx.sparkle, color=fx.red(), duration=1.8, sparkletime=0.05, pause=0)]
    script[184656] = [f(fx.set_front_rgb, values=fx.white_red(), update=True, autoOff=False),
                      f(fx.fade_out, speed=10)]
    script[185556] = [f(fx.set_front_rgb, values=fx.white_red(), update=True, autoOff=False),
                      f(fx.fade_out, speed=10)]
    script[186556] = [f(fx.set_front_rgb, values=fx.white_red(), update=True, autoOff=False),
                      f(fx.fade_out, speed=20, limit=50),
                      f(fx.fade_in, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.white_red(), start_brightness=50, end_brightness=200, stepping=10),
                      f(fx.fade_out, speed=6)]

    script[187972] = [f(fx.mh_move_to, fixture="gobo1", rotation=35, tilt=160, speed=30, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=55, tilt=85, speed=30, update=True)]  # space

    script[189815] = [f(fx.mh_off, fixture="gobo", update=True),
                      f(fx.set_front_rgb, values=fx.white_red(), update=True, autoOff=False)]
    script[190315] = [f(fx.fade_out, speed=20, limit=50),
                      f(fx.fade_in, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.white_red(), start_brightness=50, end_brightness=200, stepping=10),
                      f(fx.fade_out, speed=6)]
    script[192423] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.red())]  # space
    script[192892] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.red())]  # space
    script[193305] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.red())]  # space
    script[194856] = [f(fx.fade_out, speed=20, limit=10),
                      f(fx.fade_in, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.red(), start_brightness=50, end_brightness=200, stepping=10),
                      f(fx.fade_out, speed=20, limit=10),
                      f(fx.fade_in, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.red(), start_brightness=50, end_brightness=200, stepping=10),
                      f(fx.fade_out, speed=20, limit=10),
                      f(fx.fade_in, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.red(), start_brightness=50, end_brightness=200, stepping=10),
                      f(fx.fade_out, speed=2)]  # space

    script[192893] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255),
                      f(fx.mh_set_gobo, fixture="gobo", name="spot")]  # space
    script[199486] = [f(fx.sparkle, color=fx.red(), duration=1.5, sparkletime=0.05, pause=0)]

    script[201600] = [  # f(fx.blackout),
        # f(fx.uv_on),
        f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]  # space
    script[201947] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70)]  # space
    script[203347] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    script[203348] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[203748] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[204549] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=210)]  # space
    script[204550] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=210)]  # space
    script[206049] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=50)]  # space
    script[206050] = [f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=50)]  # space
    script[206151] = [f(fx.set_floor_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[206052] = [f(fx.uv_off)]  # 1
    script[208634] = [f(fx.mh_off, fixture="gobo")]  # 1

    script[208635] = [f(fx.racer, color_brgbw=[255, 255, 255, 255, 255], splittime=0.017, laps=2, reverse=False)]
    script[208664] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # n
    script[208758] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[208904] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # n
    script[209039] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # c
    script[209203] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # n
    script[209513] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[209652] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[209985] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[210107] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[210201] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[210440] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[210701] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # c
    script[210700] = [f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=255)]  # space
    script[210991] = [f(fx.mh_set_color, fixture="gobo", name="darkblue", update="false")]  # 1
    script[210992] = [f(fx.blackout)]  # 1
    script[210993] = [f(fx.uv_on)]  # 1
    script[210994] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]  # space
    script[211619] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=255, speed=70)]  # space
    script[212814] = [f(fx.mh_set_start, fixture="gobo1", rotation=199, tilt=170)]  # space
    script[212815] = [f(fx.mh_set_start, fixture="gobo2", rotation=155, tilt=170)]  # space
    script[213414] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[214184] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=100, speed=210)]  # space
    script[214185] = [f(fx.mh_move_to, fixture="gobo2", rotation=155, tilt=100, speed=210)]  # space
    script[215734] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=50)]  # space
    script[215735] = [f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=50)]  # space
    script[215834] = [f(fx.set_floor_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[215835] = [f(fx.uv_off)]  # 1

    script[218500] = [f(fx.mh_off, fixture="gobo")]  # 1

    script[218647] = [f(fx.kitt, fixtures=["rgb1", "rgb2", "rgb3"], color=fx.red(), pausetime=0.1)]  # space
    script[219199] = [f(fx.kitt, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.red(), pausetime=0.1)]  # space
    script[219599] = [f(fx.fade_out, speed=15),
                      f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.blue(), duration=0.5, sparkletime=0.05, pause=0)]

    script[220482] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]  # space
    script[221107] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=235, speed=70),
                      f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.blue(), duration=2.4, sparkletime=0.05, pause=0)]  # space
    script[223403] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=120, speed=200),
                      f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.blue(), duration=1.6, sparkletime=0.05, pause=0)]  # space

    script[225222] = [f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=50)]  # space
    script[225223] = [f(fx.mh_set_gobo, fixture="gobo", name="puzzle"),
                      f(fx.mh_set_color, fixture="gobo", name="red"),
                      f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=50),
                      f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.blue(), duration=1.8, sparkletime=0.05, pause=0)
                      ]  # space

    script[227412] = [f(fx.mh_strobe, fixture="gobo", color="red", speed=70)]  # space
    script[227512] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=160, autoOn=False)]
    script[228012] = [f(fx.mh_move_to, fixture="gobo1", rotation=95, tilt=110, speed=160, autoOn=False),
                      f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=110, speed=160, autoOn=False),
                      f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.red(), duration=1.2, sparkletime=0.05, pause=0)]
    script[229312] = [f(fx.mh_off, fixture="gobo"),
                      f(fx.mh_set_start, fixture="gobo", rotation=175, tilt=235),
                      f(fx.mh_set_gobo, fixture="gobo", name="spot")]  # 1

    script[229901] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]  # space
    script[230526] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=235, speed=70),
                            f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.red(), duration=1.8, sparkletime=0.05, pause=0)]  # space

    script[232269] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[232816] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[233440] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space

    script[234569] = [f(fx.blackout),
                      f(fx.uv_on),
                      f(fx.mh_set_gobo, fixture="gobo", name="bubbles", update=True),
                      f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=150),
                      f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=150)]  # space
    script[236644] = [f(fx.mh_move_to, fixture="gobo1", rotation=95, tilt=110, speed=160, autoOn=False),
                      f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=110, speed=160, autoOn=False)]

    script[239374] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]  # space
    script[239374] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=235, speed=70),
                      f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.red(), duration=1.8, sparkletime=0.05, pause=0)]  # space

    script[241717] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=110, speed=70)]
    script[242384] = [f(fx.mh_set_color, fixture="gobo", name="red")]
    script[242484] = [ f(fx.mh_move_to, fixture="gobo1", rotation=205, tilt=160, speed=150),
                      f(fx.mh_move_to, fixture="gobo2", rotation=138, tilt=175, speed=150)]

    script[244021] = [f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.blue(), duration=1.8, sparkletime=0.05, pause=0)]  # space
    script[246393] = [f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.red(), duration=1.8, sparkletime=0.05, pause=0)]  # space
    script[248771] = [ f(fx.sparkle, fixtures=["rgb4", "rgb5", "rgb6"], color=fx.green(), duration=1.8, sparkletime=0.05, pause=0)]  # space
    script#[251074] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space

    script[251148] = [f(fx.set_all_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[251281] = [f(fx.set_all_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[251437] = [f(fx.set_all_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[251574] = [f(fx.set_all_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[251743] = [f(fx.set_all_rgb, values=fx.red(), update=True, autoOff=False)]  # n
    script[252019] = [f(fx.set_all_rgb, values=fx.blue(), update=True, autoOff=False)]  # c
    script[252163] = [f(fx.set_all_rgb, values=fx.white_red(), update=True, autoOff=False),
                      f(fx.uv_off),
                      f(fx.fade_out, speed=5)]  # n
    script[253163] = [f(fx.mh_fade_out, fixtures="gobo", speed=3, limit=0, steppingtime=0.001)]

    ## Start the script now
    runScript(file_name=file_name, startpos=startpos, script=script, duration=duration, dmx=dmx)
