import time
from time import sleep
import random

class FX:
    def __init__(self, dmx):
        self.dmx = dmx

    def fade_in(self, fixtures, speed=20, limit=255):
        brightness = 0
        while brightness <= limit:
            for fixture in fixtures:
                values = self.dmx.getFixtureValues(fixture)
                values[4] = brightness if brightness < limit else limit
                self.dmx.setFixtureValues("rgb1", values)
            self.dmx.update()
            brightness = brightness + speed
            sleep(0.005)

    def fade_out(self, fixtures, speed=20, limit=0):
        brightness = 255
        while brightness >= limit:
            for fixture in fixtures:
                values = self.dmx.getFixtureValues(fixture)
                values[4] = brightness if brightness > limit else limit
                self.dmx.setFixtureValues("rgb1", values)
            self.dmx.update()
            brightness = brightness - speed
            sleep(0.005)


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