import time
from time import sleep
import random
from mylib.udmx import uDMX

class FX:
    def __init__(self, dmx):
        self.dmx = dmx
        self.strobe_colors = {"all": 1, "red": 40, "green": 50, "blue":60, "yellow": 70, "cyan":80, "purple": 90, "white": 100 }
        self.mh_colors = {"white": 1, "red": 16, "lightblue": 32, "orange": 48, "darkblue": 64, "yellow": 80, "green": 96, "violet": 112}
        self.mh_gobos = {"spiral": 0, "star": 8, "spot": 16, "flower": 24, "dotrings": 32, "mudball": 40, "puzzle": 48, "bubbles": 56}
        self.mh_gobos_jitter = {"spiral": 64, "star": 72, "spot": 80, "flower": 88, "dotrings": 96, "mudball": 104, "puzzle": 112,
                         "bubbles": 120}

    def mh_move_to(self, fixture, rotation, tilt, speed, autoOn=True, update=True, autoOffAfter=False):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            values = {"1": rotation, "2": tilt, "7": speed}
            if autoOn:
                self.mh_on(fixture)
            self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update(fixtures=fixtures)

        if autoOffAfter:
            sleep(autoOffAfter)
            for fixture in fixtures:
                self.mh_off(fixture)

    def mh_set_start(self, fixture, rotation, tilt, autoOff=True, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            if autoOff:
                self.mh_off(fixture)
            self.dmx.setFixtureValues(fixture, {"1": rotation, "2": tilt, "5": 0, "7": 50})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_set_gobo(self, fixture, name, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"4": self.mh_gobos.get(name, 80)})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_set_color(self,fixture, name, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"3": self.mh_colors.get(name, 1)})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_off(self, fixture, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"5": 1})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_on(self, fixture, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, {"5": 8})
        if update:
            self.dmx.update(fixtures=fixtures)

    def mh_strobe(self, fixture, color, speed, update=True):
        fixtures = self.dmx.get_all_fixtures(filter=fixture)
        for fixture in fixtures:
            self.mh_set_color(fixture, color, False)
            speed += 16
            if speed > 131:
                speed = 131

            self.dmx.setFixtureValues(fixture, {"5": speed})
        if update:
            self.dmx.update(fixtures=fixtures)

    def uv_on(self):
        self.dmx.setFixtureValues("uv", {"1": 255, "2": 255, "3": 255, "4": 255})
        self.dmx.update(fixtures="uv")

    def uv_off(self):
        self.dmx.setFixtureValues("uv", {"1": 0, "2": 0, "3": 0, "4": 0})
        self.dmx.update(fixtures="uv")

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
            values = {"1": 0, "2": 0, "3": 0, "4": color_brgbw[0], "5": color_brgbw[1], "6": color_brgbw[2], "7": color_brgbw[3], "8": color_brgbw[4]}

            for fixture in fixtures:
                self.dmx.setFixtureValues(fixture, values)
                if previous_fixture is not None:
                    self.dmx.setFixtureValues(previous_fixture, values_previous_fixture)
                self.dmx.update()
                previous_fixture = fixture
                sleep(splittime)
            laps_done = laps_done + 1
        return True

    def strobe(self, fixtures, color="all", speed=255):
        if color in self.strobe_colors.keys():
            color = self.strobe_colors.get(color)

        values = {"1": 201, "2": color, "3": speed, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, values)
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

    def fade_in(self, color_brgbw, fixtures=None, speed=20, limit=255):
        if fixtures is None:
            fixtures = self.dmx.get_all_fixtures()
        values = {"1": 0, "2": 0, "3": 0, "4": color_brgbw[0], "5": color_brgbw[1], "6": color_brgbw[2],
                  "7": color_brgbw[3], "8": color_brgbw[4]}
        brightness = 0
        while brightness < limit:
            for fixture in fixtures:
                values = self.dmx.getFixtureValues(fixture)
                brightness = values.get(4, 0)
                values[4] = brightness + speed if brightness + speed <= limit else limit
                self.dmx.setFixtureValues(fixture, values)
            self.dmx.update()
        return True

    def fade_out(self, fixtures=None, speed=20, limit=0):
        if fixtures is None:
            fixtures = self.dmx.get_all_fixtures()

        brightness = 255
        while brightness > limit:
            for fixture in fixtures:
                values = self.dmx.getFixtureValues(fixture)
                brightness = values.get(4, 0)
                values[4] = brightness - speed if brightness - speed > limit else limit
                self.dmx.setFixtureValues(fixture=fixture, values=values)
            self.dmx.update()
        return True


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

    def off(self, fixtures=None, update=True):
        values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        for fixture in fixtures:
            self.dmx.setFixtureValues(fixture, values)
        if update:
            self.dmx.update()
        return True


    def blue(self):
        return {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 255, "8": 0}
    def red(self):
        return {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0}
    def white(self):
        return {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 0, "7": 0, "8": 255}
    def green(self):
        return {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 255, "7": 0, "8": 0}
    def all(self):
        return {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 255, "7": 255, "8": 255}