from __future__ import division
import time
# Import the PCA9685 module.
import Adafruit_PCA9685
# Uncomment to enable debug output.
import logging
import random
logging.basicConfig(level=logging.CRITICAL)

class Servo:
    def __init__(self):
        # Initialise the PCA9685 using the default address (0x40).
        self.pwm = Adafruit_PCA9685.PCA9685()
        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)
        # Configure min and max servo pulse lengths
        self.servo_min = 150  # Min pulse length out of 4096
        self.servo_max = 600  # Max pulse length out of 4096
        self.pulse_length = 1000000  # 1,000,000 us per second
        self.pulse_length //= 60  # 60 Hz
        print('{0}us per period'.format(self.pulse_length))
        self.pulse_length //= 4096  # 12 bits of resolution
        print('{0}us per bit'.format(self.pulse_length))
        self.servos = {"paolo": 1, "paule": 0, "paulinchen": 2}
        self.fixed_positions = {"open": 150, "close": 450, "half": 350}

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
        print(channel, pulse)
        self.pwm.set_pwm(channel, 0, pulse)

    def set(self, servo, position):
        self.set_servo_pos(servo, self.fixed_positions.get(position))

    def speak(self, servo, value=None):
        if value is None:
            value = random.randint(350, 450)
        self.set_servo_pos(servo, value)


