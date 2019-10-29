import time
from time import sleep
import random
from mylib.udmx import uDMX

class FX:
    def __init__(self, dmx):
        self.dmx = dmx
        self.strobe_colors = {"all": 1, "red": 40, "green": 50, "blue":60, "yellow": 70, "cyan":80, "purple": 90, "white": 100 }
        self.mh_colors = {"white": 1, "red": 16, "lightblue": 32, "orange": 48, "darkblue": 64, "yellow": 80, "green": 96, "violet": 112}
        self.mh_gobos = {"spiral": 0, "star": 8, "spot": 16, "flower": 24, "dotrings": 32, "mudball": 40, "puzzle": 48, "bubbles": 56,
                         "jspiral": 64, "jstar": 72, "jspot": 80, "jflower": 88, "jdotrings": 96, "jmudball": 104, "jpuzzle": 112,
                         "jbubbles": 120}

    def mh_reset(self, fixture="gobo"):
            fixtures = self.dmx.get_all_fixtures(filter=fixture)
            for fixture in fixtures:
                self.dmx.setFixtureValues(fixture, {"1": 175, "2": 255, "3": 0, "4": 16, "5": 10, "6": 255, "7": 125, "8": 0, "9":0})
                self.dmx.update(fixtures=fixtures)

    def mh_move_to(self, fixture, rotation, tilt, speed, autoOn=True, update=True, autoOffAfter=False):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            values = {"1": rotation, "2": tilt, "7": speed, "8":0}
            if autoOn:
                self.mh_on(fixture)
            self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update(fixtures=fixtures)

        if autoOffAfter:
            sleep(autoOffAfter)
            for fixture in fixtures:
                self.mh_off(fixture)

    def mh_set_start(self, fixture="gobo", rotation=0, tilt=0, autoOff=True, update=True, speed=50):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            if autoOff:
                self.mh_off(fixture)
            self.dmx.setFixtureValues(fixture, {"1": rotation, "2": tilt, "5": 0, "7": speed, "8":0, "9": 0})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_set_gobo(self, fixture="gobo", name="spot", update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"4": self.mh_gobos.get(name, 80), "8":0})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_fade_out(self, fixtures="gobo", speed=20, limit=0,steppingtime=0.01):
        if type(fixtures) is str or fixtures is None:
            fixtures = self.dmx.get_all_fixtures(fixtures)

        brightness = 255
        while brightness > limit:
            for fixture in fixtures:
                values = self.dmx.getFixtureValues(fixture)
                fbrightness = values.get(6, 0)
                values[6] = fbrightness - speed if fbrightness - speed > limit else limit
                self.dmx.setFixtureValues(fixture=fixture, values=values)
            brightness -= speed
            self.dmx.update()
            sleep(steppingtime)

        for fixture in fixtures:
            self.mh_off(fixture=fixture)
            self.mh_set_brightness(fixture=fixture, brightness=255)

        return True

    def mh_fade_in(self, fixtures="gobo", color=None, speed=20, limit=255, start_brightness=0, steppingtime=0.01):
        if type(fixtures) is str or fixtures is None:
            fixtures = self.dmx.get_all_fixtures(fixtures)

        for fixture in fixtures:
            self.mh_set_color(fixture=fixture,name=color)
            self.mh_set_brightness(fixture=fixture,brightness=start_brightness)
            self.mh_on(fixture=fixture)

        brightness = start_brightness
        print(brightness, "<", limit)
        while brightness < limit:
            print(brightness)
            for fixture in fixtures:
                values = self.dmx.getFixtureValues(fixture)
                fbrightness = values.get(6, 0)
                values[6] = fbrightness + speed if fbrightness + speed < limit else limit
                print("FadeIN", values)
                self.dmx.setFixtureValues(fixture, {"6": brightness})
            brightness += speed
            self.dmx.update()
            sleep(steppingtime)
        return True

    def mh_set_brightness(self, fixture=None, brightness=255):
        if type(fixture) is str or fixture is None:
            fixtures = self.dmx.get_all_fixtures(fixture)

        for fixture in fixtures:
            values = self.dmx.getFixtureValues(fixture)
            self.dmx.setFixtureValues(fixture, {"6": brightness})

        self.dmx.update(fixtures=fixtures)

    def mh_set_color(self,fixture, name, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"3": self.mh_colors.get(name, 1)})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_off(self, fixture="gobo", update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"5": 1, "8":0})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_on(self, fixture, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"5": 8, "8":0})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_strobe(self, fixture, color, speed, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        speed += 16
        for fixture in fixtures:
            self.mh_set_color(fixture, color, False)
            if speed > 131:
                speed = 131

            self.dmx.setFixtureValues(fixture, {"5": speed})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_strobe_off(self, fixture, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"5": 8})
        if update:
            self.dmx.update(fixtures=fixtures)

    #speed has to be between 128-189 (fast2slow) or 194-255 (slow2fast)
    def mh_color_rotate_on(self, fixture, speed, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"3": speed})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_color_rotate_off(self, fixture, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"3": 190})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_infinity(self, fixture, duration=5, speed=150, sleeptime=0.8):

        coordinates = [
            #{"rotation": 65, "tilt": 165},
            {"rotation": 65, "tilt": 175},
            {"rotation": 65, "tilt": 55},
            {"rotation": 35, "tilt": 55},
            {"rotation": 35, "tilt": 175}
        ]
        t_end = time.time() + duration

        while time.time() < t_end:
            i=0
            for pos in coordinates:
                if time.time() > t_end:
                    break
                i+=1
                if i == 2 or i==4:
                    sspeed = speed * 0.8
                else:
                    sspeed = speed
                if sspeed > 255:
                    sspeed = 255
                if sspeed <= 0:
                    sspeed = 0
                print(sspeed)
                self.mh_move_to(fixture=fixture, rotation=pos.get("rotation"), tilt=pos.get("tilt"), speed=int(sspeed))
                sleep(sleeptime)
                if time.time() > t_end:
                    break

        return True


    def mh_swipe(self, fixture, left, right, speed=40):
        value = left
        if value == left:
            value = right
        else:
            value = left
        self.mh_move_to("gobo", rotation=132, tilt=value, speed=speed, update=True)


    def uv_on(self):
        self.dmx.setFixtureValues("uv", {"1": 255, "2": 255, "3": 255, "4": 255})
        self.dmx.update(fixtures="uv")

    def uv_off(self):
        self.dmx.setFixtureValues("uv", {"1": 0, "2": 0, "3": 0, "4": 0})
        self.dmx.update(fixtures="uv")

    def uv_fade_out(self, speed=20, limit=0):
        brightness = 255
        while brightness > limit:
            self.dmx.setFixtureValues("uv", {"1": brightness, "2": brightness, "3": brightness, "4": brightness})
            self.dmx.update(fixtures="uv")
            brightness -= speed

        return True


    def sparkle(self, color, fixtures=None, duration=0.5, sparkletime=0.1, pause=0.2, sparkle_amount=1):
        if fixtures is None:
            fixtures = self.dmx.get_all_fixtures()
        if sparkle_amount > len(fixtures):
            sparkle_amount=len(fixtures)
        amount = random.randint(1, sparkle_amount)

        t_end = time.time() + duration
        while time.time() < t_end:
            fix = random.sample(fixtures, amount)
            for fixture in fix:
                self.dmx.setFixtureValues(fixture, color)
                self.dmx.update()
            sleep(sparkletime)
            self.blackout()
            sleep(pause)




    def random(self, color_brgbw, fixtures=None, splittime=0.1, laps=1, reverse=False):
        if fixtures is None:
            fixtures = self.dmx.get_all_fixtures()

        if reverse:
            fixtures.reverse()

        laps_done = 0
        previous_fixture = None
        values_previous_fixture = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        while laps_done < laps:
            values = {"1": 0, "2": 0, "3": 0, "4": color_brgbw[0], "5": color_brgbw[1], "6": color_brgbw[2], "7": color_brgbw[3], "8": color_brgbw[4]}
            random.shuffle(fixtures)
            for fixture in fixtures:
                self.dmx.setFixtureValues(fixture, values)
                if previous_fixture is not None:
                    self.dmx.setFixtureValues(previous_fixture, values_previous_fixture)
                self.dmx.update()
                previous_fixture = fixture
                sleep(splittime)
            laps_done = laps_done + 1
        return True

    def racer(self, color_brgbw, fixtures=None, splittime=0.1, laps=1, reverse=False):
        if fixtures is None:
            fixtures = self.dmx.get_all_fixtures()

        if reverse:
            fixtures.reverse()

        laps_done = 0
        previous_fixture = None
        values_previous_fixture = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        while laps_done < laps:
            if type(color_brgbw) == list:
                values = {"1": 0, "2": 0, "3": 0, "4": color_brgbw[0], "5": color_brgbw[1], "6": color_brgbw[2], "7": color_brgbw[3], "8": color_brgbw[4]}
            else:
                values = color_brgbw
            for fixture in fixtures:
                self.dmx.setFixtureValues(fixture, values)
                if previous_fixture is not None:
                    self.dmx.setFixtureValues(previous_fixture, values_previous_fixture)
                self.dmx.update()
                previous_fixture = fixture
                sleep(splittime)
            laps_done = laps_done + 1
        self.blackout()
        return True

    def strobe(self, fixtures, color="all", speed=255):
        if color in self.strobe_colors.keys():
            color = self.strobe_colors.get(color)

        values = {"1": 201, "2": color, "3": speed, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, values)
        return True

    def rgb_pulse(self, fixtures, color="all", speed=255):
        if color in self.strobe_colors.keys():
            color = self.strobe_colors.get(color)

        values = {"1": 101, "2": color, "3": speed, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, values)
        self.dmx.update()
        return True


    def blackout(self):
        values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        self.set_all_rgb(values=values, update=True)
        self.dmx.update()
        return True

    def fog(self, intensity=255, duration=0.2):
        print("FOG ON FOR", duration)
        values = {"1": intensity, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        self.dmx.setFixtureValues("fog", values)
        self.dmx.update()
        sleep(duration)
        values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        self.dmx.setFixtureValues("fog", values)
        self.dmx.update()
        print("FOG OFF FOR", duration)
        return True

    def rgb_crossfade(self, fixtures_in, color, fixtures_out, in_stepping=20, out_stepping=20, step_delay=0, end_brightness=255):
        if type(fixtures_in) is str:
            fixtures_in = self.dmx.get_all_fixtures(filter=fixtures_in)
        if type(fixtures_out) is str:
            fixtures_out = self.dmx.get_all_fixtures(filter=fixtures_out)

        for fixture_in in fixtures_in:
            self.dmx.setFixtureValues(fixture_in, color)


        max_brightness = 0
        for fixture_out in fixtures_out:
            tmp_brightness = self.dmx.getFixtureValues(fixture_out).get(4)
            if tmp_brightness > max_brightness:
                max_brightness = tmp_brightness

        #print("Starting from maxvalue:", max_brightness)
        values = color
        in_brightness = 0

        while in_brightness < end_brightness or max_brightness > 0:
            for fixture_in in fixtures_in:
                values = self.dmx.getFixtureValues(fixture_in)
                in_brightness = values.get(4, 0)
                values[4] = int(in_brightness + in_stepping) if in_brightness + in_stepping <= end_brightness else end_brightness
                self.dmx.setFixtureValues(fixture_in, values)
                #print("New in value for fixture", fixture_in, values)
                #self.dmx.update()

            for fixture_out in fixtures_out:
                values = self.dmx.getFixtureValues(fixture_out)
                fbrightness = values.get(4, 0)
                values[4] = fbrightness - out_stepping if fbrightness - out_stepping > 0 else 0
                self.dmx.setFixtureValues(fixture=fixture_out, values=values)
                #print("New out value for fixture", fixture_out, values)
            self.dmx.update()
            max_brightness -= out_stepping

            sleep(step_delay)

    def fade_in(self, color, fixtures=None, stepping=20, start_brightness=0, end_brightness=255, step_delay=0):
        if type(fixtures) is str:
            fixtures = self.dmx.get_all_fixtures(filter=fixtures)

        color["4"] = start_brightness

        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, color)
        values = color
        brightness = start_brightness
        while brightness < end_brightness:
            for fixture in fixtures:
                values = self.dmx.getFixtureValues(fixture)
                brightness = values.get(4, 0)
                values[4] = int(brightness + stepping) if brightness + stepping <= end_brightness else end_brightness
                self.dmx.setFixtureValues(fixture, values)

            self.dmx.update()
            sleep(step_delay)
        return True

    def fade_out(self, fixtures=None, speed=20, limit=0):
        if type(fixtures) is str or fixtures is None:
            fixtures = self.dmx.get_all_fixtures(fixtures)

        brightness = 255
        while brightness > limit:
            for fixture in fixtures:
                values = self.dmx.getFixtureValues(fixture)
                fbrightness = values.get(4, 0)
                values[4] = fbrightness - speed if fbrightness - speed > limit else limit
                self.dmx.setFixtureValues(fixture=fixture, values=values)
            brightness -= speed
            self.dmx.update()
        return True

    def kitt(self, fixtures, color, pausetime):
        if type(fixtures) == str:
            fixtures = [fixtures]

        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, color)
            self.dmx.update()
            sleep(pausetime)

    def color_row(self, fixtures, rows, duration=3, speed=0.2, rand=False):
        if type(fixtures) == str:
            fixtures = [fixtures]
        t_end = time.time() + duration
        switch = True
        newrow = random.choice(rows)
        prev_row = None
        while time.time() < t_end:
            if rand is not True:
                for row in rows:
                    for fixture in fixtures:
                        self.dmx.setFixtureValues(fixture, row)
                    self.dmx.update()
                    sleep(speed)
            else:
                while prev_row == newrow:
                    newrow = random.choice(rows)
                for fixture in fixtures:
                    self.dmx.setFixtureValues(fixture, newrow)
                prev_row = newrow
                self.dmx.update()

                sleep(speed)
        return True

    def color_switch(self, value1, value2, durration=10, speed=0.2):
        t_end = time.time() + durration
        switch = True
        while time.time() < t_end:
            switch = not switch
            if switch is True:
                values = value1
            else:
                values = value2
            self.dmx.setFixtureValues("rgb1", values)
            self.dmx.update()
            sleep(speed)
        return True

    def set_all_rgb(self, values, update=False, autoOff=False):
        fixtures = self.dmx.get_all_fixtures()
        for fixture in fixtures:
            if fixture[:3] == "rgb":
                self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update(fixtures=fixtures)
        if autoOff:
            sleep(autoOff)
            for fixture in fixtures:
                if fixture[:3] == "rgb":
                    self.off([fixture], update=False)
            self.dmx.update(fixtures=fixtures)
        return True

    def set_back_rgb(self, values, update=False, autoOff=False):
        fixtures = ["rgb1", "rgb2", "rgb3"]
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update(fixtures=fixtures)
        if autoOff:
            sleep(autoOff)
            for fixture in fixtures:
                if fixture[:3] == "rgb":
                    self.off([fixture], update=False)
            self.dmx.update(fixtures=fixtures)
        return True

    def front_back_sync(self, fixtures1: list, fixtures2: list, colors: list, duration=1, speed=0.1):
        t_end = time.time() + duration
        previous_fixtures = []
        while time.time() < t_end:
            for color in colors:
                for f1, f2 in zip(fixtures1, fixtures2):
                    self.off(fixtures=previous_fixtures, update=False)
                    if f1 is not None:
                        self.dmx.setFixtureValues(f1, color)
                    if f2 is not None:
                        self.dmx.setFixtureValues(f2, color)
                    previous_fixtures = [f1, f2]
                    self.dmx.update()
                    sleep(speed)
        self.blackout()
        return True

    def set_front_rgb(self, values, update=False, autoOff=False):
        fixtures = ["rgb4", "rgb5", "rgb6"]
        for fixture in fixtures:
            if fixture[:3] == "rgb":
                self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update(fixtures=fixtures)
        if autoOff:
            sleep(autoOff)
            for fixture in fixtures:
                if fixture[:3] == "rgb":
                    self.off([fixture], update=False)
            self.dmx.update(fixtures=fixtures)
        return True

    def set_floor_rgb(self, values, update=False, autoOff=False):
        fixtures = ["rgb7", "rgb8"]
        for fixture in fixtures:
            if fixture[:3] == "rgb":
                self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update(fixtures=fixtures)
        if autoOff:
            sleep(autoOff)
            for fixture in fixtures:
                if fixture[:3] == "rgb":
                    self.off([fixture], update=False)
            self.dmx.update(fixtures=fixtures)
        return True

    def set_rgb(self, fixtures, values, update=True, autoOff=False):
        for fixture in fixtures:
            if fixture[:3] == "rgb":
                self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update(fixtures=fixtures)
        if autoOff:
            sleep(autoOff)
            for fixture in fixtures:
                if fixture[:3] == "rgb":
                    self.off([fixture], update=False)
            self.dmx.update(fixtures=fixtures)
        return True

    def off(self, fixtures=None, update=True):
        values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update()
        return True

    def rgb_strobe(self, fixtures=None, colorname=None, speed=255):
        values = {"1": 210, "2": self.strobe_colors.get(colorname), "3": speed, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}

        for fixture in fixtures:
            print("Updating", fixture, "with", values)
            self.dmx.setFixtureValues(fixture, values)
        self.dmx.update()
        return True

    def rgb_strobe_front(self, colorname=None, speed=255):
        self.rgb_strobe(fixtures=["rgb4","rgb5","rgb6"], colorname=colorname, speed=speed)
    def rgb_strobe_back(self, colorname=None, speed=255):
        self.rgb_strobe(fixtures=["rgb1","rgb2","rgb3"], colorname=colorname, speed=speed)
    def rgb_strobe_floor(self, colorname=None, speed=255):
        self.rgb_strobe(fixtures=["rgb7","rgb8"], colorname=colorname, speed=speed)



    def blue(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 0, "6": 0, "7": 255, "8": 0}
    def red(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 255, "6": 0, "7": 0, "8": 0}
    def white(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 0, "6": 0, "7": 0, "8": 255}
    def green(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 0, "6": 255, "7": 0, "8": 0}
    def all(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 255, "6": 255, "7": 255, "8": 255}
    def white_green(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 0, "6": 255, "7": 0, "8": 255}
    def white_blue(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 0, "6": 0, "7": 255, "8": 255}
    def white_red(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 255, "6": 0, "7": 0, "8": 255}
    def green_blue(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 0, "6": 128, "7": 128, "8": 0}
    def green_blue_white(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 0, "6": 128, "7": 128, "8": 255}
    def yellow(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 255, "6": 255, "7": 0, "8": 0}
    def orange(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 255, "6": 255, "7": 0, "8": 0}
    def violet(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 255, "6": 0, "7": 255, "8": 0}
    def purple(self, brightness=255):
        return {"1": 0, "2": 0, "3": 0, "4": brightness, "5": 70, "6": 0, "7": 255, "8": 0}