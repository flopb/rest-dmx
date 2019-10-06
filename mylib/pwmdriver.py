from __future__ import division
import time
# Import the PCA9685 module.
import Adafruit_PCA9685
# Uncomment to enable debug output.
import logging
import random
logging.basicConfig(level=logging.CRITICAL)
import threading
from queue import Queue

class Servo:
    def __init__(self):
        # Initialise the PCA9685 using the default address (0x40).
        self.pwm = Adafruit_PCA9685.PCA9685()
        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)
        # Configure min and max servo pulse lengths
        self.servo_min = 150  # Min pulse length out of 4096
        self.servo_max = 550  # Max pulse length out of 4096
        self.pulse_length = 1000000  # 1,000,000 us per second
        self.pulse_length //= 60  # 60 Hz
        print('{0}us per period'.format(self.pulse_length))
        self.pulse_length //= 4096  # 12 bits of resolution
        print('{0}us per bit'.format(self.pulse_length))
        self.servos = {"paolo": 1, "paulinchen": 0}
        self.fixed_positions = {"open": 150, "close": 450, "half": 350}

        self.q = Queue()
        t1 = threading.Thread(name='speaker',
                              target=self.dospeak)
        t1.setDaemon(True)
        t1.start()

    def speak(self, who, pause=0.2, minmax=[350,450]):
        if who is None:
            who = "paulinchen"

        if type(who) is str:
            who = [who]
        data={"speak": True, "who": who, "pause": pause, "minmax":minmax }
        self.q.put(data)

    def stop(self, who, minmax=[350,450]):
        if who is None:
            who = "paulinchen"

        if type(who) is str:
            who = [who]
        data = {"speak": False, "who": who, "minmax":minmax}
        self.q.put(data)


    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pos(self, servo, pulse):
        if type(servo) == str:
            channel = self.servos.get(servo, 0)
        else:
            channel = servo

        if pulse < self.servo_min:
            pulse = self.servo_min
        if pulse > self.servo_max:
            pulse = self.servo_max

        #pulse *= 1000
        #pulse //= self.pulse_length
        #print(channel, pulse)
        self.pwm.set_pwm(channel, 0, pulse)

    def set(self, servo, position):
        if type(servo) == str:
            servo = [servo]
        for i in servo:
            self.set_servo_pos(i, self.fixed_positions.get(position))

    def dospeak(self):
        data = {}
        active_speakers = []
        pause = 0.2
        min=350
        max=450
        ispeakers = {"paulinchen":0, "paolo":0}
        while(True):
            try:
                data = self.q.get_nowait()
                for speaker in data.get("who"):
                    if data.get("speak"):
                        ispeakers[speaker] += 1
                    else:
                        self.set_servo_pos(speaker, self.servo_max)
                        ispeakers[speaker] -= 1

                if data.get("pause"):
                    pause = data.get("pause")

                if data.get("minmax"):
                    min = data.get("minmax")[0]
                    max = data.get("minmax")[1]


                print("Currently active speakers:", ispeakers, "Pause:", pause)

                self.q.task_done()
            except:
                pass

            newvalue = random.randint(min, max)
            value = newvalue
            for speaker in ispeakers.keys():
                if(ispeakers[speaker] > 0):
                    self.set_servo_pos(speaker, value)
            time.sleep(pause)


