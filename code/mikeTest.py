import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib

def move_up():  
    #define GPIO pins
    GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
    direction= 20       # Direction -> GPIO Pin
    step = 21      # Step -> GPIO Pin

    # Declare an named instance of class pass GPIO pins numbers
    mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")


    # call the function, pass the arguments
    mymotortest.motor_go(True, "Full" , 200, 0, False, .05)

    # good practise to cleanup GPIO at some point before exit
    GPIO.cleanup()