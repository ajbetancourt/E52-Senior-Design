#counterclockwise stepper motor
import RPi.GPIO as GPIO
import time

#sudo apt install -y python-opencv

import cv2

#Stepper motor code

GPIO.setmode(GPIO.BCM)
AIN1 = 17 
AIN2 = 4
BIN1 = 18
BIN2 = 27
GPIO.setwarnings(False)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

def turn_clockwise(s):
    GPIO.output(BIN1,1)
    GPIO.output(AIN2,0)
    time.sleep(s)
    GPIO.output(AIN2,1)
    GPIO.output(BIN2,0)  
    time.sleep(s)
    GPIO.output(BIN2, 1)
    GPIO.output(AIN1, 0)
    time.sleep(s)
    GPIO.output(AIN1, 1)
    GPIO.output(BIN1, 0)
    time.sleep(s)
    
def turn_counterclockwise(s):
    GPIO.output(AIN1, 1)
    GPIO.output(BIN1, 0)
    time.sleep(s)
    GPIO.output(BIN2, 1)
    GPIO.output(AIN1, 0)
    time.sleep(s)
    GPIO.output(AIN2,1)
    GPIO.output(BIN2,0)
    time.sleep(s)
    GPIO.output(BIN1,1)
    GPIO.output(AIN2,0)
    time.sleep(s)

def main():
    print("GUI is Orgels bloodsport\n")
    option = input("Choose an option below:\n 1. Turn Clockwise | 2. Turn Counter ClockWise")
    if option == '1':
        turn_clockwise(0.5)
    elif option == '2':
        turn_counterclockwise(0.5)
    else:
        print("Please provide a valid input")
    
    
if __name__ == '__main__':
	main()