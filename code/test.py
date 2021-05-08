import RPi.GPIO as GPIO

#import the library
from RpiMotorLib import RpiMotorLib

#define GPIO pins
GPIO_pins = (14,15, 18)
direction = 20
step = 21

mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

mymotortest.motor_go(True, "Full",255 , 0.01, False, .05)

GPIO.cleanup()
