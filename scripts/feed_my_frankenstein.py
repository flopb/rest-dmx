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
    file_name = "./sounds/Alice_Cooper_Feed_My_Frankenstein.mp3"

    ## Here comes the script
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
    script[69249] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=160, speed=50)]  # space
    script[69250] = [f(fx.mh_move_to, fixture="gobo2", rotation=142, tilt=175, speed=50)]  # space
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
    script[78934] = [f(fx.mh_move_to, fixture="gobo1", rotation=199, tilt=160, speed=50)]  # space
    script[78935] = [f(fx.mh_move_to, fixture="gobo2", rotation=142, tilt=175, speed=50)]  # space
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
    script[104296] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[104549] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[104692] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[105493] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[106615] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[107800] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[108954] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[110154] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[111355] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[112552] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[113722] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[114902] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[116084] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[117248] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[118416] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[119636] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[120824] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[121961] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[123172] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[124370] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[125552] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[126701] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[127895] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[129046] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[130177] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[131379] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[132596] = [f(fx.set_back_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[133772] = [f(fx.set_back_rgb, values=fx.green(), update=True, autoOff=False)]  # space
    script[134974] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space

    ## Start the script now
    runScript(file_name=file_name,startpos=startpos,script=script,duration=duration)

