import RPi.GPIO as gpio
import time

# Servo-GPIO (PWM-GPIO 18, Pin 12)
servopin = 17
servopin2 = 18
# GPIO initialisieren
gpio.setmode(gpio.BCM)
gpio.setup(servopin, gpio.OUT)
gpio.setup(servopin2, gpio.OUT)
# PWM-Frequenz auf 50 Hz setzen
servo = gpio.PWM(servopin, 50)
servo2 = gpio.PWM(servopin2, 50)
# PWM starten, Servo auf 0 Grad
servo.start(2.5)
servo2.start(2.5)
try:
  # Endlosschleife Servoansteuerung
  while True:
    # 90 Grad
    servo.ChangeDutyCycle(7.5)
    servo2.ChangeDutyCycle(7.5)
    time.sleep(1)
    # 180 Grad
    servo.ChangeDutyCycle(12.5)
    servo2.ChangeDutyCycle(12.5)
    time.sleep(1)
    # 0 Grad
    servo.ChangeDutyCycle(2.5)
    servo2.ChangeDutyCycle(2.5)
    time.sleep(1)

except KeyboardInterrupt:
  # Abbruch mit [Strg][C],
  # Servo auf 0 Grad, PWM beenden
  servo.ChangeDutyCycle(2.5)
  servo2.ChangeDutyCycle(2.5)
  servo.stop()
  servo2.stop()
  gpio.cleanup()