import time
from time import sleep
import random
from mylib.udmx import uDMX

class FX:
    def __init__(self, dmx):
        self.dmx = dmx
        self.strobe_colors = {"all": 1, "red": 40, "green": 50, "blue":60, "yellow": 70, "cyan":80, "purple": 90, "white": 100 }

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
        values = {"1": intensity, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        self.dmx.setFixtureValues("fog", values)
        self.dmx.update()
        sleep(duration)
        values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        self.dmx.setFixtureValues("fog", values)
        self.dmx.update()
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