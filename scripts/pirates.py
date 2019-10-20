from mylib.helpers import runScript
from time import sleep
from mylib import effects
from mylib.pwmdriver import Servo
import functools


f = functools.partial

def play(**kwargs):
    dmx = kwargs.get("dmx")
    fx = effects.FX(dmx)
    script = {}
    startpos = float(kwargs.get("pos"))
    duration = float(kwargs.get("duration")) if kwargs.get("duration") is not None else None
    fx.uv_off()
    fx.mh_set_start("gobo", rotation=175, tilt=255)
    fx.mh_set_gobo("gobo", "spot")
    fx.mh_set_color("gobo", "lightblue")
    s = Servo()
    ## Create initial mood
    fx.blackout()

    ## Set filename of music-title
    file_name = "./sounds/intro.mp3"

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
    script[21243] = [f(fx.blackout)]
    script[21246] = [f(fx.set_rgb, fixtures=["rgb3"], values=fx.green_blue(), update=True, autoOff=False)]
    script[23034] = [f(fx.blackout)]
    script[23036] = [f(fx.set_rgb, fixtures=["rgb2"], values=fx.red(), update=True, autoOff=False)]
    script[24855] = [f(fx.blackout)]
    #script[24856] = [f(fx.uv_on)]  # space
    script[24857] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[25007] = [f(fx.fade_out, speed=6)]
    script[26536] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[26686] = [f(fx.fade_out, speed=6)]
    script[28536] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[28686] = [f(fx.fade_out, speed=6)]
    script[30132] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[30282] = [f(fx.fade_out, speed=6)]
    script[31980] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[32130] = [f(fx.fade_out, speed=6)]
    script[33638] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[33788] = [f(fx.fade_out, speed=6)]
    script[35422] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[35572] = [f(fx.fade_out, speed=6)]
    script[37222] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[37272] = [f(fx.blackout)]
    script[37321] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[37371] = [f(fx.blackout)]
    script[37532] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[37582] = [f(fx.blackout)]
    script[38160] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[38210] = [f(fx.blackout)]
    script[38354] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[38404] = [f(fx.blackout)]
    script[38502] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39068] = [f(fx.blackout)]
    script[39018] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39068] = [f(fx.blackout)]
    script[39238] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39288] = [f(fx.blackout)]
    script[39388] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39438] = [f(fx.blackout)]
    script[39889] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[39939] = [f(fx.blackout)]
    script[40201] = [f(fx.set_rgb, fixtures=["rgb4", "rgb5", "rgb6"], values=fx.green_blue(), update=True, autoOff=False)]
    script[40251] = [f(fx.blackout)]

    speed=6
    script[40657] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False),
                     f(fx.fade_out, speed=speed)]  # nach-oben
    script[42307] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False),
                     f(fx.fade_out, speed=speed)]  # nach-oben
    script[44079] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False),
                     f(fx.fade_out, speed=speed)]  # nach-oben
    script[45077] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[45366] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[45917] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False),f(fx.fade_out, speed=speed)]  # nach-oben
    script[46959] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[47365] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[47588] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[48192] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[48773] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[49360] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[49903] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False),f(fx.fade_out, speed=speed)]  # nach-oben

    script[51151] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[51995] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[52265] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[52846] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[53729] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[54079] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[54323] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.050)]  # nach-oben
    script[54588] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False),f(fx.fade_out, speed=3)]  # nach-oben


    end_brightness = 15
    in_stepping=1
    out_stepping=1
    script[56591] = [f(fx.rgb_crossfade, fixtures_out=[], color=fx.green_blue(0), fixtures_in=["rgb4", "rgb6"], out_stepping=out_stepping, in_stepping=in_stepping, step_delay=0, end_brightness=end_brightness)]  # x
    script[57869] = [f(fx.rgb_crossfade, fixtures_out=["rgb4", "rgb6"], color=fx.green_blue(0), fixtures_in=["rgb5","rgb7", "rgb8"], out_stepping=out_stepping, in_stepping=in_stepping, step_delay=0, end_brightness=end_brightness)]  # x
    script[59719] = [f(fx.rgb_crossfade, fixtures_out=["rgb5","rgb7", "rgb8"], color=fx.green_blue(0), fixtures_in=["rgb4", "rgb6"], out_stepping=out_stepping, in_stepping=in_stepping, step_delay=0, end_brightness=end_brightness)]  # x
    script[61467] = [f(fx.rgb_crossfade, fixtures_out=["rgb4", "rgb6"], color=fx.green_blue(0), fixtures_in=["rgb5","rgb7", "rgb8"], out_stepping=out_stepping, in_stepping=in_stepping, step_delay=0, end_brightness=end_brightness)]  # x
    script[63331] = [f(fx.rgb_crossfade, fixtures_out=["rgb5","rgb7", "rgb8"], color=fx.green_blue(0), fixtures_in=["rgb4", "rgb6"], out_stepping=out_stepping*12, in_stepping=in_stepping*3, step_delay=0, end_brightness=end_brightness*12)]  # x
    script[64920] = [f(fx.rgb_crossfade, fixtures_out=["rgb4", "rgb6"], color=fx.green_blue(0), fixtures_in=["rgb5","rgb7", "rgb8"], out_stepping=out_stepping*12, in_stepping=in_stepping*3, step_delay=0, end_brightness=end_brightness*12)]  # x
    script[66688] = [f(fx.rgb_crossfade, fixtures_out=["rgb5","rgb7", "rgb8"], color=fx.green_blue(0), fixtures_in=["rgb4", "rgb6"], out_stepping=out_stepping*12, in_stepping=in_stepping*3, step_delay=0, end_brightness=end_brightness*12)]  # x
    script[68491] = [f(fx.rgb_crossfade, fixtures_out=["rgb4", "rgb6"], color=fx.green_blue(0), fixtures_in=["rgb5","rgb7", "rgb8"], out_stepping=out_stepping*12, in_stepping=in_stepping*3, step_delay=0, end_brightness=end_brightness*12)]  # x

    speed=35
    script[70180] = [f(fx.blackout),
                     f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=speed, update=True)]  # n
    script[71671] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=150, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=150, speed=speed, update=True)]  # m
    script[71965] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=200, speed=speed, update=True)]  # m
    script[73460] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=150, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=150, speed=speed, update=True)]  # m
    script[73745] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=speed, update=True)]  # n

    script[75651] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=150, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=150, speed=0, update=True)]
    script[76292] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=0, update=True)]  #
    script[76880] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=200, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=200, speed=0, update=True)]  # m

    script[77322] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=speed, update=True)]  # n
    script[78703] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=150, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=150, speed=speed, update=True)]  # m
    script[79034] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=200, speed=speed, update=True)]  # m
    script[80489] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=150, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=150, speed=speed, update=True)]  # m
    script[80755] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=speed, update=True)]  # n

    script[82499] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=150, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=150, speed=0, update=True)]
    script[83094] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=0, update=True)]  #
    script[83654] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=255, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=255, speed=0, update=True)]  # m

    script[84654] = [f(fx.mh_off, fixture="gobo"),
                     f(fx.mh_set_color, fixture="gobo", name="yellow"),
                     f(fx.mh_set_gobo, fixture="gobo", name="bubbles")]  # m

    script[84862] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=0, speed=160, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=0, speed=160, update=True)]  # m
    script[86466] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=255, speed=160, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=255, speed=160, update=True)]  # m
    script[88263] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=0, speed=160, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=0, speed=160, update=True)]  # m
    script[90084] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=255, speed=160, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=255, speed=160, update=True)]  # m

    script[91826] = [f(fx.mh_off, fixture="gobo"),
                     f(fx.mh_set_color, fixture="gobo", name="lightblue"),
                     f(fx.mh_set_gobo, fixture="gobo", name="spot")
                     ]
    script[91926] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=127, speed=30, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=127, speed=30, update=True)]  # m
    script[92476] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=0, speed=30, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=0, speed=30, update=True)]  # m
    script[93025] = [f(fx.mh_move_to, fixture="gobo1", rotation=175, tilt=127, speed=30, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=175, tilt=127, speed=30, update=True)]  # m
    script[93583] = [f(fx.mh_move_to, fixture="gobo1", rotation=175, tilt=225, speed=30, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=175, tilt=225, speed=30, update=True)]  # m

    autoOff=0.1
    script[94214] = [#f(fx.uv_on),
                     f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[95164] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[95752] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[96017] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[96672] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[97001] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[97576] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[97908] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[98590] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[98887] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[99510] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[99811] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[100114] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[100449] = [f(fx.set_back_rgb, values=fx.green_blue(), update=True, autoOff=autoOff)]  # space
    script[100731] = [f(fx.blackout),
                      f(fx.set_floor_rgb, values=fx.green_blue(), update=True, autoOff=False),
                      f(fx.fade_out, speed=8)]  # space
    #script[101682] = [f(fx.set_back_rgb, values=fx.red(), update=True, autoOff=False)]  # space
    script[101682] = [f(fx.mh_set_gobo, fixture="gobo", name="bubbles"),
                        f(fx.mh_move_to, fixture="gobo1", rotation=0, tilt=160, speed=60, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=160, speed=60, update=True)]  # m
    script[101683] = [f(fx.sparkle, color=fx.green_blue(), duration=1.2, sparkletime=0.05, pause=0),
                      f(fx.blackout)]  # space
    #script[102432] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=0.1)]  # space
    script[102621] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False)]
    script[103000] = [f(fx.fade_out),
                      f(fx.mh_fade_out, fixtures="gobo", speed=6),
                      f(fx.uv_fade_out, speed=20)]

    script[105988] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[106085] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[106197] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[106397] = [f(fx.fade_out)]  # nach-oben
    script[106800] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[106921] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[107061] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[107261] = [f(fx.fade_out)]  # nach-oben
    script[107657] = [f(fx.set_front_rgb, values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[107769] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[107947] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]  # nach-oben
    script[108123] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]  # nach-oben

    #script[108230] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False)]  # ,
    script[109548] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[109689] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[109832] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[110032] = [f(fx.fade_out)]  # nach-oben
    script[110467] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[110612] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[110790] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[110990] = [f(fx.fade_out)]  # nach-oben
    script[111477] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green(), update=True, autoOff=False)]
    script[111623] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[111787] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[112465] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=0.1)]  # .
    script[112671] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=0.1)]  # .
    script[113021] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]  # ,
    script[114453] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[114550] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green(), update=True, autoOff=False)]  # nach-oben
    script[114666] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.blue(), update=True, autoOff=False),
                      f(fx.fade_out)]  # nach-oben
    script[116279] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green(), update=True, autoOff=False)]
    script[116374] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[116542] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green(), update=True, autoOff=False),
                      f(fx.fade_out)]  # nach-oben
    script[117177] = [f(fx.set_rgb, fixtures=["rgb4","rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[117366] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[117508] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[117785] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out, speed=50)]
                       # .
    script[118086] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[118343] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[118422] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[118722] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=0.1),
                      f(fx.fade_out, speed=20)]  # .

    script[119923] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[120128] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[120287] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[120387] = [f(fx.fade_out)]
    script[120851] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[121056] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[121231] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[121331] = [f(fx.fade_out)]
    script[121780] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[121996] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[122158] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[122479] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]  # nach-oben
    script[122728] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[122951] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[123114] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[123291] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]  # nach-oben
    script[123453] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[123595] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[123754] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[123930] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]  # nach-oben
    script[124087] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[124628] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[124816] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[125006] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]  # nach-oben
    script[125525] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[125758] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[125934] = [f(fx.set_front_rgb, values=fx.green(), update=True, autoOff=False)]
    script[126246] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False)]  # nach-oben
    script[126494] = [f(fx.set_front_rgb, values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out, speed=5, limit=5)]  # nach-oben
    speed=5
    start_brigth = 5
    end_bright = 60
    script[127720] = [f(fx.fade_in, color=fx.green_blue_white(), fixtures="rgb", stepping=speed, start_brightness=start_brigth, end_brightness=end_bright)]  # nach-oben
    script[128594] = [f(fx.fade_out, speed=speed, limit=5)]
    script[129488] = [f(fx.fade_in, color=fx.green_blue_white(), fixtures="rgb", stepping=speed, start_brightness=start_brigth, end_brightness=end_bright)]
    script[130533] = [f(fx.fade_out, speed=speed, limit=5)]
    script[131518] = [f(fx.fade_in, color=fx.green_blue_white(), fixtures="rgb", stepping=speed, start_brightness=start_brigth, end_brightness=end_bright)]
    script[132390] = [f(fx.fade_out, speed=speed, limit=5)]
    script[133302] = [f(fx.fade_in,  color=fx.green_blue_white(), fixtures="rgb", stepping=speed, start_brightness=start_brigth, end_brightness=end_bright)]

    script[134349] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=False)]  # nach-oben
    script[134449] = [f(fx.fade_out, speed=20, limit=0)]
    script[134871] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[135050] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[135298] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]
    script[135801] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[135984] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[136273] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]
    script[136582] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False)]  # nach-oben
    script[136891] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=False)]  # nach-oben
    script[137232] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False)]  # nach-oben
    script[137785] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[137995] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[138176] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]
    script[138661] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[138854] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[139152] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]
    script[139384] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[139696] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[140008] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]
    script[140517] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[140709] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[140974] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False)]  # nach-oben
    script[141146] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=False)]  # nach-oben
    script[141297] = [f(fx.set_front_rgb, values=fx.green_blue(), update=True, autoOff=False)]  # nach-oben

    script[141630] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[141726] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[141919] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]

    script[142424] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[142620] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[142882] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]

    script[143123] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[143444] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[143805] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]

    script[144356] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[144463] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[144790] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]

    script[145347] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[145529] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[145705] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]

    script[145982] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[146286] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[146595] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]

    script[147186] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[147290] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[147579] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]

    script[148101] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[148248] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=False)]
    script[148510] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out)]

    script[149003] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[149156] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[149484] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.green_blue_white(), update=True, autoOff=False),
                      f(fx.fade_out),
                      f(fx.mh_set_start, fixture="gobo", rotation=132, tilt=150),
                      f(fx.mh_set_color, fixture="gobo", name="yellow"),
                      f(fx.mh_set_gobo, fixture="gobo", name="bubbles"),
                      f(fx.mh_set_brightness, fixture="gobo", brightness=20)
                      ]

    script[150287] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=False)]  # nach-oben
    script[151289] = [f(fx.fade_out, fixtures="rgb4", speed=25, limit=0)]
    script[151629] = [f(fx.fade_out, fixtures="rgb5", speed=25, limit=0)]
    script[151963] = [f(fx.fade_out, fixtures="rgb6", speed=50, limit=0)]

    speed = 190
    left = 170
    right = 80
    script[152037] = [f(fx.mh_swipe, fixture="gobo", left=left, right=right, speed=speed)]

    script[153023] = [f(fx.mh_swipe, fixture="gobo", left=right, right=left, speed=speed)]
    script[154087] = [f(fx.mh_swipe, fixture="gobo", left=left, right=right, speed=speed)]

    script[154463] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # nach-oben
    script[154957] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # nach-oben
    script[155160] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # nach-oben

    script[155062] = [f(fx.mh_swipe, fixture="gobo", left=right, right=left, speed=speed)]

    script[155437] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # nach-oben

    script[156014] = [f(fx.mh_swipe, fixture="gobo", left=left, right=right, speed=speed)]
    script[157037] = [f(fx.mh_swipe, fixture="gobo", left=right, right=left, speed=speed)]

    script[155710] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # nach-oben
    script[156008] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # nach-oben
    script[157156] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=False)]  # nach-oben
    script[157256] = [f(fx.fade_out)]

    script[158119] = [f(fx.mh_swipe, fixture="gobo", left=left, right=right, speed=speed)]
    script[159115] = [f(fx.mh_swipe, fixture="gobo", left=right, right=left, speed=speed)]
    script[160072] = [f(fx.mh_swipe, fixture="gobo", left=left, right=right, speed=speed)]
    script[160978] = [f(fx.mh_swipe, fixture="gobo", left=right, right=left, speed=speed)]

    script[161981] = [f(fx.mh_swipe, fixture="gobo", left=left, right=right, speed=speed)]
    script[162908] = [f(fx.mh_swipe, fixture="gobo", left=right, right=left, speed=speed)]
    script[163798] = [f(fx.mh_swipe, fixture="gobo", left=left, right=right, speed=speed)]
    script[164849] = [f(fx.mh_swipe, fixture="gobo", left=right, right=left, speed=speed)]


    script[159131] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False),f(fx.fade_out, speed=30)]  # nach-oben
    script[160132] = [f(fx.set_front_rgb, values=fx.green(), update=True, autoOff=False),f(fx.fade_out, speed=30)]  # nach-oben
    script[161049] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False),f(fx.fade_out, speed=30)]  # nach-oben
    script[161858] = [f(fx.set_front_rgb, values=fx.green(), update=True, autoOff=False),f(fx.fade_out, speed=30)]  # nach-oben
    script[163471] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False), f(fx.fade_out, speed=30)]  # nach-oben
    script[164419] = [f(fx.set_front_rgb, values=fx.green(), update=True, autoOff=False), f(fx.fade_out, speed=30)]

    script[165041] = [f(fx.mh_off)]
    script[165128] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.blue(), update=True, autoOff=0.1)]
    script[165443] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[165750] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.blue(), update=True, autoOff=0.1)]
    script[166090] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]

    script[166419] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.blue(), update=True, autoOff=0.1)]
    script[166689] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[167022] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.blue(), update=True, autoOff=0.1)]
    script[167326] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]

    script[167656] = [f(fx.set_rgb, fixtures=["rgb4", "rgb6"], values=fx.blue(), update=True, autoOff=0.1)]
    script[167948] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.green_blue_white(), update=True, autoOff=0.1)]
    script[168101] = [f(fx.set_front_rgb, values=fx.green(), update=True, autoOff=False), f(fx.fade_out, speed=5)]



    script[171320] = [f(fx.sparkle, color=fx.orange(120), duration=5.5, sparkletime=0.2, pause=0)]  # nach-oben
    script[176461] = [f(fx.kitt, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"], color=fx.blue(), pausetime=0.1)]  # nach-oben

    script[177931] = [f(fx.mh_set_start, fixture="gobo1", rotation=135, tilt=220),
                      f(fx.mh_set_start, fixture="gobo2", rotation=215, tilt=220),
                      f(fx.mh_set_color, fixture="gobo", name="lightblue"),
                     f(fx.mh_set_gobo, fixture="gobo", name="spot"),
                      f(fx.sparkle, color=fx.green_blue(120), duration=7.7, sparkletime=0.1, pause=0)]


    speed = 35
    color = fx.orange(255)
    script[185481] = [f(fx.blackout),
                      #f(fx.uv_on),
                      f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]  # n
    script[186562] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=120, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=120, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]  # m
    script[187528] = [f(fx.mh_move_to, fixture="gobo1", rotation=220, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=130, tilt=200, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]  # m
    script[188454] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=120, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=120, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]  # m
    script[189392] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]  # n

    script[190304] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=120, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=120, speed=0, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]
    script[191276] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=0, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]  #
    script[192224] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=200, speed=0, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=200, speed=0, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]  # m

    script[192513] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=speed, update=True),
                     f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1","rgb2","rgb3","rgb4","rgb5","rgb6"])]  # n

    ######################################
    script[194476] = [f(fx.mh_move_to, fixture="gobo1", rotation=130, tilt=250, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=220, tilt=250, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6"])]  # n

    script[195385] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=170, speed=0, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=170, speed=0, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6"])]
    script[196316] = [f(fx.mh_move_to, fixture="gobo1", rotation=180, tilt=200, speed=0, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=170, tilt=200, speed=0, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6"])]  #
    script[196566] = [f(fx.mh_move_to, fixture="gobo1", rotation=200, tilt=220, speed=0, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=150, tilt=220, speed=0, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6"])]  # m

    script[196900] = [f(fx.mh_move_to, fixture="gobo1", rotation=130, tilt=180, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=220, tilt=180, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6"])]  # n
    ######################################

    script[198177] = [f(fx.mh_move_to, fixture="gobo1", rotation=0, tilt=109, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=145, speed=speed, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6"])]  # n

    script[199159] = [f(fx.mh_move_to, fixture="gobo1", rotation=0, tilt=109, speed=0, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=255, tilt=145, speed=0, update=True),
                      f(fx.set_all_rgb, values=color, update=True, autoOff=False),
                      f(fx.fade_out, fixtures=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6"])]


    script[199560] = [f(fx.mh_set_gobo, fixture="gobo", name="jdotrings")]
    script[199561] = [f(fx.mh_move_to, fixture="gobo1", rotation=127, tilt=65, speed=215, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=127, tilt=205, speed=215, update=True),
                      f(fx.sparkle, color=fx.orange(120), duration=2.9, sparkletime=0.05, pause=0)]
    script[202561] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=95, speed=215, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=155, speed=215, update=True),
                      f(fx.sparkle, color=fx.orange(120), duration=3.4, sparkletime=0.05, pause=0)]

    script[206062] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[206327] = [f(fx.set_front_rgb, values=fx.orange(), update=True, autoOff=0.1)]  # space
    script[206655] = [f(fx.set_front_rgb, values=fx.violet(), update=True, autoOff=False),
                      f(fx.mh_set_color, fixture="gobo", name="violet"),
                      f(fx.fade_out, speed=5)]  # space

    #Phantom of the opera starts here
    #fx.mh_set_gobo("gobo", "dotrings")
    #fx.mh_set_color("gobo", "violet")

    script[207736] = [f(fx.mh_set_gobo, fixture="gobo", name="dotrings")]
    script[207837] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=165, speed=245, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=95, speed=245, update=True)]

    speed=0
    script[214309] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=135, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=115, speed=speed, update=True)]  # n
    script[217313] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=115, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=135, speed=speed, update=True)]  # n
    script[217530] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=95, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=155, speed=speed, update=True)]  # n
    script[217726] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=75, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=175, speed=speed, update=True)]  # n
    script[217952] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=55, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=195, speed=speed, update=True)]  # n
    script[218180] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=35, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=215, speed=speed, update=True)]  # n

    script[220062] = [f(fx.set_all_rgb, values=fx.violet(), update=True, autoOff=0.1)]  # space
    script[220276] = [f(fx.set_all_rgb, values=fx.violet(), update=True, autoOff=False),
                      f(fx.fade_out)]  # space

    script[221044] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=55, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=195, speed=speed, update=True)]  # n
    script[221300] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=75, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=175, speed=speed, update=True)]  # n
    script[221533] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=95, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=155, speed=speed, update=True)]  # n
    script[221742] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=115, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=135, speed=speed, update=True)]  # n
    script[221949] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=135, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=115, speed=speed, update=True)]  # n

    script[224763] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=115, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=135, speed=speed, update=True)]  # n
    script[224936] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=95, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=155, speed=speed, update=True)]  # n
    script[225201] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=75, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=175, speed=speed, update=True)]  # n
    script[225391] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=55, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=195, speed=speed, update=True)]  # n
    script[225656] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=35, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=215, speed=speed, update=True)]  # n

    script[227550] = [f(fx.set_all_rgb, values=fx.violet(), update=True, autoOff=0.1)]  # space
    script[227751] = [f(fx.set_all_rgb, values=fx.violet(), update=True, autoOff=False),
                      f(fx.fade_out)]  # space

    script[228490] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=55, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=195, speed=speed, update=True)]  # n
    script[228736] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=75, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=175, speed=speed, update=True)]  # n
    script[228953] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=95, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=155, speed=speed, update=True)]  # n
    script[229123] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=115, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=135, speed=speed, update=True)]  # n
    script[229397] = [f(fx.mh_move_to, fixture="gobo1", rotation=255, tilt=135, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=0, tilt=115, speed=speed, update=True)]  # n

    script[231775] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=126, speed=247, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=131, speed=247, update=True)]  #

    speed=160
    script[248108] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=0, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=255, speed=speed, update=True)]  # n
    script[250050] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=255, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=0, speed=speed, update=True)]  # n
    script[251953] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=0, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=255, speed=speed, update=True)]  # n
    script[253734] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=126, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=131, speed=speed, update=True)]  # n

    script[254734] = [f(fx.mh_off)]
    script[254434] =  [f(fx.mh_set_start, fixture="gobo1", rotation=175, tilt=240),
                      f(fx.mh_set_start, fixture="gobo2", rotation=175, tilt=240)]  # n

    script[255534] = [f(fx.mh_move_to, fixture="gobo1", rotation=175, tilt=115, speed=222, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=175, tilt=115, speed=222, update=True)]  # n

    script[263184] = [f(fx.mh_set_gobo, name="jdotrings")]

    script[265904] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=135, speed=speed, update=True)]  # m
    script[266123] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=155, speed=speed, update=True)]  # n
    script[266323] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=175, speed=speed, update=True)]  # m
    script[266575] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=195, speed=speed, update=True)]  # n
    script[266813] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=215, speed=speed, update=True)]  # m


    script[269694] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=195, speed=speed, update=True)]  # n
    script[269982] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=175, speed=speed, update=True)]  # m
    script[270173] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=155, speed=speed, update=True)]  # n
    script[270419] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=135, speed=speed, update=True)]  # m
    script[270619] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=115, speed=speed, update=True)]  # n

    script[274364] = [f(fx.mh_set_gobo, name="dotrings"),
                      f(fx.mh_move_to, fixture="gobo1", rotation=47, tilt=126, speed=246, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=47, tilt=131, speed=246, update=True)]

    script[289368] = [f(fx.mh_move_to, fixture="gobo1", rotation=47, tilt=255, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=47, tilt=0, speed=speed, update=True)]  # n
    script[291157] = [f(fx.mh_move_to, fixture="gobo1", rotation=47, tilt=0, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=47, tilt=255, speed=speed, update=True)]  # n
    script[293056] = [f(fx.mh_move_to, fixture="gobo1", rotation=47, tilt=255, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=47, tilt=0, speed=speed, update=True)]  # n
    script[294910] = [f(fx.mh_move_to, fixture="gobo1", rotation=47, tilt=0, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=47, tilt=255, speed=speed, update=True)]  # n

    script[296130] = [f(fx.mh_off)]
    script[296230] = [f(fx.mh_set_start, fixture="gobo1", rotation=90, tilt=15),
                      f(fx.mh_set_start, fixture="gobo2", rotation=90, tilt=25)]  # n

    script[296830] = [f(fx.mh_move_to, fixture="gobo1", rotation=90, tilt=140, speed=222, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=90, tilt=150, speed=222, update=True)]  #  n

    script[304330] = [f(fx.mh_set_gobo, name="jdotrings")]

    script[307076] = [f(fx.mh_move_to, fixture="gobo1", rotation=90, tilt=120, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=90, tilt=130, speed=speed, update=True)]  # n
    script[307281] = [f(fx.mh_move_to, fixture="gobo1", rotation=90, tilt=100, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=90, tilt=110, speed=speed, update=True)]  # n
    script[307519] = [f(fx.mh_move_to, fixture="gobo1", rotation=90, tilt=80, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=90, tilt=90, speed=speed, update=True)]  # n
    script[307727] = [f(fx.mh_move_to, fixture="gobo1", rotation=90, tilt=60, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=90, tilt=70, speed=speed, update=True)]  # n
    script[307949] = [f(fx.mh_move_to, fixture="gobo1", rotation=90, tilt=40, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=90, tilt=50, speed=speed, update=True)]  # n

    script[309913] = [f(fx.mh_set_gobo, name="dotrings")]
    script[310913] = [f(fx.mh_fade_out, speed=5, steppingtime=0)]
    script[311413] = [f(fx.mh_set_start, fixture="gobo1", rotation=47, tilt=126),
                      f(fx.mh_set_start, fixture="gobo2", rotation=47, tilt=131)]

    script[314313] = [f(fx.mh_fade_in, color="violet", speed=5, steppingtime=0),
                      f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=126, speed=250, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=131, speed=250, update=True)]

    #Swipe
    script[330495] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=0, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=255, speed=speed, update=True)]  # n
    script[332354] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=255, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=0, speed=speed, update=True)]  # n
    script[334232] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=0, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=255, speed=speed, update=True)]  # n
    script[336099] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=126, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=131, speed=speed, update=True)]  # n

    script[336826] = [f(fx.mh_off)]
    script[336926] = [f(fx.mh_set_start, fixture="gobo1", rotation=175, tilt=240),
                      f(fx.mh_set_start, fixture="gobo2", rotation=175, tilt=240)]  # n

    script[337926] = [f(fx.mh_move_to, fixture="gobo1", rotation=175, tilt=115, speed=222, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=175, tilt=115, speed=222, update=True)]  # n

    script[345475] = [f(fx.mh_set_gobo, name="jdotrings")]

    script[348222] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=135, speed=speed, update=True)]  # m
    script[348443] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=155, speed=speed, update=True)]  # n
    script[348640] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=175, speed=speed, update=True)]  # m
    script[348885] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=195, speed=speed, update=True)]  # n
    script[349111] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=215, speed=speed, update=True)]  # m

    script[351993] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=195, speed=speed, update=True)]  # n
    script[352162] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=175, speed=speed, update=True)]  # m
    script[352422] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=155, speed=speed, update=True)]  # n
    script[352632] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=135, speed=speed, update=True)]  # m
    script[352869] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=115, speed=speed, update=True)]  # n

    script[355790] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=135, speed=speed, update=True)]  # m
    script[355966] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=155, speed=speed, update=True)]  # n
    script[356171] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=175, speed=speed, update=True)]  # m
    script[356401] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=195, speed=speed, update=True)]  # n
    script[356616] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=215, speed=speed, update=True)]  # m


    script[366808] = [f(fx.mh_off)]
    script[366908] = [f(fx.mh_set_gobo, name="dotrings"),
                      f(fx.mh_set_start, fixture="gobo1", rotation=47, tilt=126),
                      f(fx.mh_set_start, fixture="gobo2", rotation=47, tilt=131)]
    script[367908] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=126, speed=250, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=131, speed=250, update=True)]  # n

    script[382816] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=0, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=255, speed=speed, update=True)]  # n
    script[384731] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=255, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=0, speed=speed, update=True)]  # n
    script[386594] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=0, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=255, speed=speed, update=True)]  # n
    script[388405] = [f(fx.mh_move_to, fixture="gobo1", rotation=133, tilt=126, speed=speed, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=133, tilt=131, speed=speed, update=True)]  # n

    script[389221] = [f(fx.mh_off)]
    script[389321] = [f(fx.mh_set_start, fixture="gobo1", rotation=175, tilt=240),
                      f(fx.mh_set_start, fixture="gobo2", rotation=175, tilt=240)]  # n
    script[390321] = [f(fx.mh_move_to, fixture="gobo1", rotation=175, tilt=115, speed=222, update=True),
                      f(fx.mh_move_to, fixture="gobo2", rotation=175, tilt=115, speed=222, update=True)]  # n


    script[397869] = [f(fx.mh_set_gobo, name="jdotrings")]

    script[400610] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=135, speed=speed, update=True)]  # m
    script[400810] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=155, speed=speed, update=True)]  # n
    script[401029] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=175, speed=speed, update=True)]  # m
    script[401249] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=195, speed=speed, update=True)]  # n
    script[401478] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=215, speed=speed, update=True)]  # m

    script[404402] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=195, speed=speed, update=True)]  # n
    script[404616] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=175, speed=speed, update=True)]  # m
    script[404857] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=155, speed=speed, update=True)]  # n
    script[405059] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=135, speed=speed, update=True)]  # m
    script[405290] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=115, speed=speed, update=True)]  # n

    script[408107] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=135, speed=speed, update=True)]  # m
    script[408335] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=155, speed=speed, update=True)]  # n
    script[408555] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=175, speed=speed, update=True)]  # m
    script[408766] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=195, speed=speed, update=True)]  # n
    script[408979] = [f(fx.mh_move_to, fixture="gobo", rotation=175, tilt=215, speed=speed, update=True)]  # m


    #FINAL
    speed=120
    pt1=180
    pt2=75
    sparkle_speed1=0.06
    sparkle_speed12=0.04
    sparkle_speed2=0.02
    sparkle_duration=1.9
    fixtures=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6", "rgb7", "rgb8"]
    fixtures2=["rgb1", "rgb2", "rgb3", "rgb4", "rgb5", "rgb6", "rgb7", "rgb8"]
    script[412678] = [f(fx.mh_strobe, fixture="gobo", color="violet", speed=80)]
    script[412778] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed1, pause=0)]  # n
    script[414596] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed1, pause=0)]  # m
    script[416425] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed1, pause=0)]  # n
    script[418318] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed1, pause=0)]  # m
    script[420220] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed1, pause=0)]  # n
    script[422061] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed1, pause=0)]  # m
    script[423928] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed1, pause=0)]  # n
    script[425828] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed1, pause=0)]  # m
    script[427555] = [f(fx.mh_strobe, fixture="gobo", color="violet", speed=90),
                      f(fx.mh_set_gobo, name="dotrings")]
    script[427655] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed12, pause=0)]  # n
    script[429549] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed12, pause=0)]  # m
    script[431426] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed12, pause=0)]  # n
    script[433276] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed12, pause=0)]  # m
    script[435126] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed12, pause=0)]  # n
    script[437023] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed12, pause=0)]  # m
    script[438886] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed12, pause=0)]  # n
    script[440737] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=sparkle_duration, sparkletime=sparkle_speed12, pause=0)]  # m
    script[442650] = [f(fx.mh_strobe, fixture="gobo", color="violet", speed=100),
                      f(fx.mh_set_gobo, name="jdotrings")]
    script[442672] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=1.5, sparkletime=sparkle_speed2, pause=0)]  # n
    script[444487] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=1.5, sparkletime=sparkle_speed2, pause=0)]  # m
    script[446391] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=1.5, sparkletime=sparkle_speed2, pause=0)]  # n
    script[448231] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=1.5, sparkletime=sparkle_speed2, pause=0)]  # m
    script[450157] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=1.5, sparkletime=sparkle_speed2, pause=0)]  # n
    script[451987] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=1.5, sparkletime=sparkle_speed2, pause=0)]  # m
    script[453880] = [f(fx.mh_move_to, fixture="gobo", rotation=0, tilt=pt1, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=1.5, sparkletime=sparkle_speed2, pause=0)]  # n
    script[455720] = [f(fx.mh_move_to, fixture="gobo", rotation=255, tilt=pt2, speed=speed, update=True, autoOn=False),
                      f(fx.sparkle, fixtures=fixtures2, color=fx.blue(), duration=1.5, sparkletime=sparkle_speed2, pause=0)]  # m
    script[457195] = [f(fx.set_front_rgb, values=fx.violet(), update=True, autoOff=0.1)]  # nach-oben
    script[457420] = [f(fx.set_front_rgb, values=fx.violet(), update=True, autoOff=False)]  # nach-oben
    script[457641] = [f(fx.fade_out),
                      f(fx.mh_off)]  # space


    #Singers
    script[231691] = [f(fx.fade_in, fixtures=["rgb2"], color=fx.blue())]  # 1
    script[267284] = [f(fx.fade_out, fixtures=["rgb2", "rgb3"])]  # right shift
    script[272607] = [f(fx.fade_in, fixtures=["rgb3"], color=fx.blue())]  # 2
    script[306356] = [f(fx.fade_out, fixtures=["rgb2", "rgb3"])]  # right shift
    script[313951] = [f(fx.fade_in, fixtures=["rgb2"], color=fx.blue())]  # 1
    script[324527] = [f(fx.fade_out, fixtures=["rgb2", "rgb3"])]  # right shift
    script[325376] = [f(fx.fade_in, fixtures=["rgb3"], color=fx.blue())]  # 2
    script[328809] = [f(fx.fade_in, fixtures=["rgb2"], color=fx.blue())]  # 1
    script[336254] = [f(fx.fade_out, fixtures=["rgb2", "rgb3"])]
    script[337981] = [f(fx.fade_in, fixtures=["rgb2", "rgb3"], color=fx.blue())]  # 1)] #right shift
    script[348254] = [f(fx.fade_out, fixtures=["rgb2", "rgb3"])]  # right shift[f(fx.fade_in, fixtures=["rgb2", "rgb3"], color=fx.blue())]  # 1)] #right shift

    script[366175] = [f(fx.fade_in, fixtures=["rgb3"], color=fx.blue())]  # 2
    script[376904] = [f(fx.fade_out, fixtures=["rgb2", "rgb3"])]  # right shift
    script[377631] = [f(fx.fade_in, fixtures=["rgb2"], color=fx.blue())]  # 1
    script[381274] = [f(fx.fade_in, fixtures=["rgb3"], color=fx.blue())]  # 2
    script[388335] = [f(fx.fade_out, fixtures=["rgb2", "rgb3"])]  # right shift
    script[390128] = [f(fx.fade_in, fixtures=["rgb2","rgb3"], color=fx.blue())]  # 1
    script[401321] = [f(fx.fade_out, fixtures=["rgb2", "rgb3"])]  # right shift
    #script[402021] = [f(fx.fade_in, fixtures=["rgb3"], color=fx.blue())]  # 2

    #specials
    script[360437] = [f(fx.mh_set_gobo, name="dotrings"),
                      f(fx.set_front_rgb, values=fx.violet(), update=True, autoOff=0.1),
                      f(fx.sparkle, color=fx.blue(), duration=1.5, sparkletime=0.10, pause=0),
                      f(fx.blackout)]  # strg

    script[362044] = [f(fx.set_front_rgb, values=fx.violet(), update=True, autoOff=0.1)]  # space
    script[362227] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False),
                      f(fx.sparkle, color=fx.blue(), duration=1.5, sparkletime=0.1, pause=0),
                      f(fx.blackout)]  # strg
    script[363406] = [f(fx.set_front_rgb, values=fx.violet(), update=True, autoOff=False)]  # strg
    script[363961] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False)]  # space
    script[364157] = [f(fx.set_front_rgb, values=fx.violet(), update=True, autoOff=0.1),
                      f(fx.sparkle, color=fx.blue(), duration=1.5, sparkletime=0.1, pause=0),
                      f(fx.blackout)]  # strg
    script[365901] = [f(fx.set_front_rgb, values=fx.blue(), update=True, autoOff=False)]  # strg
    script[366056] = [f(fx.set_front_rgb, values=fx.violet(), update=True, autoOff=False),
                      f(fx.fade_out, speed=10)]  # space


    #additional effects
    stepping=5
    end_brightness=127
    script[231256] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten
    script[233214] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten
    script[235020] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten
    script[236814] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten
    script[238697] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten
    script[240631] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten
    script[242476] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten
    script[244352] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten
    script[246224] = [f(fx.fade_in, fixtures=["rgb7", "rgb8"], color=fx.red(), stepping=stepping, end_brightness=end_brightness),
                      f(fx.fade_out, fixtures=["rgb7", "rgb8"], speed=stepping)]  # nach-unten


#background beels
    brightness=30
    autoOff=0.1
    script[311704] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[311908] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[312198] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[312450] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[312697] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[312924] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[313160] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[313380] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[313606] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[313819] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[314059] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[314244] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[314514] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[314806] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[315023] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[315247] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[315465] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[315693] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[315897] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[316174] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[316395] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[316633] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[316881] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[317123] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[317373] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[317595] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[317817] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[318047] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[318282] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[318502] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[318727] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[319002] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[319209] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[319440] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[319638] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[319896] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[320129] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[320355] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[320572] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[320850] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[321081] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[321336] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[321558] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[321782] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[322022] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[322245] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[322476] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[322752] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[322988] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[323204] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[323438] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[323628] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[323858] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[324108] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[324333] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[324579] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[324814] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[325085] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[325290] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[325496] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[325778] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[326002] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[326229] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[326428] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[326660] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[326924] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[327142] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[327392] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[327596] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[327851] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[328064] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[328314] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[328542] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[328776] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[329035] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[329262] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[329490] = [f(fx.set_rgb, fixtures=["rgb5"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # v
    script[329716] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c
    script[329927] = [f(fx.set_rgb, fixtures=["rgb6"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # b
    script[330172] = [f(fx.set_rgb, fixtures=["rgb4"], values=fx.white(brightness), update=True, autoOff=autoOff)]  # c


#SPEAKING
    silent = [350,500]
    medium = [300, 450]
    loud = [150,350]
    script["a231308"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a235174"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a235467"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a238730"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a239236"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a242753"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a242850"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a246383"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a246604"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a250185"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a250453"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a254753"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a255301"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a267277"] = [f(s.stop, who=["paulinchen"])]  # z

    script["a272851"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a276370"] = [f(s.stop, who=["paolo"])]  # z
    script["a276815"] = [f(s.speak, who=["paolo"], minmax=loud)]  # a
    script["a279852"] = [f(s.stop, who=["paolo"])]  # z
    script["a280310"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a283710"] = [f(s.stop, who=["paolo"])]  # z
    script["a284143"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a287435"] = [f(s.stop, who=["paolo"])]  # z
    script["a287726"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a291255"] = [f(s.stop, who=["paolo"])]  # z
    script["a291555"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a295695"] = [f(s.stop, who=["paolo"])]  # z
    script["a296320"] = [f(s.speak, who=["paolo"], minmax=loud)]  # s
    script["a302330"] = [f(s.stop, who=["paolo"])]  # z
    script["a302892"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a306804"] = [f(s.stop, who=["paolo"])]  # z

    script["a313932"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a317568"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a317858"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a321212"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a321634"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a325182"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a325489"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a328528"] = [f(s.stop, who=["paolo"])]  # z
    script["a328936"] = [f(s.speak, who=["paolo", "paulinchen"], minmax=medium)]  # s
    script["a332606"] = [f(s.stop, who=["paolo", "paulinchen"])]  # z
    script["a332920"] = [f(s.speak, who=["paolo", "paulinchen"], minmax=medium)]  # s
    script["a336100"] = [f(s.stop, who=["paolo", "paulinchen"])]  # z
    script["a337575"] = [f(s.speak, who=["paolo", "paulinchen"], minmax=loud)]  # s
    script["a343553"] = [f(s.stop, who=["paolo", "paulinchen"])]  # z
    script["a344046"] = [f(s.speak, who=["paolo", "paulinchen"], minmax=medium)]  # s
    script["a348129"] = [f(s.stop, who=["paolo", "paulinchen"])]  # z
    script["a352875"] = [f(s.speak, who=["paulinchen"], minmax=silent)]  # d


    script["a360383"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a366435"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a369853"] = [f(s.stop, who=["paolo"])]  # z
    script["a370107"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a373551"] = [f(s.stop, who=["paolo"])]  # z
    script["a373735"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a377430"] = [f(s.stop, who=["paolo"])]  # z
    script["a377730"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a381326"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a381602"] = [f(s.speak, who=["paolo", "paulinchen"], minmax=medium)]  # s
    script["a384735"] = [f(s.stop, who=["paolo", "paulinchen"])]  # z
    script["a385082"] = [f(s.speak, who=["paolo", "paulinchen"], minmax=medium)]  # s
    script["a388359"] = [f(s.stop, who=["paolo", "paulinchen"])]  # z
    script["a390080"] = [f(s.speak, who=["paolo", "paulinchen"], minmax=loud)]  # a
    script["a395782"] = [f(s.stop, who=["paolo", "paulinchen"])]  # z
    script["a396274"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a401427"] = [f(s.stop, who=["paulinchen"])]  # z

    script["a402254"] = [f(s.speak, who=["paolo"], minmax=medium)]  # s
    script["a409058"] = [f(s.stop, who=["paolo"])]  # z

    script["a407246"] = [f(s.speak, who=["paulinchen"], minmax=silent)]  # d
    script["a412523"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a413086"] = [f(s.speak, who=["paulinchen"], minmax=silent)]  # d
    script["a422673"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a423286"] = [f(s.speak, who=["paulinchen"], minmax=silent)]  # d
    script["a426624"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a428438"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a442909"] = [f(s.stop, who=["paulinchen"])]  # z
    script["a443405"] = [f(s.speak, who=["paulinchen"], minmax=medium)]  # s
    script["a457715"] = [f(s.stop, who=["paulinchen"])]  # z


    runScript(file_name=file_name,startpos=startpos,script=script,duration=duration)

