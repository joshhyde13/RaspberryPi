import RPi.GPIO as GPIO
import time

def PWM_setup(pins={'red':11, 'green':12, 'blue':13}, Hz={'red':50, 'green':50, 'blue':50}):
    """
    Set GPIO pins as output
    INPUT:
       dictionaries: pins = {'pin_name': pin_numer} --> {string: int}
                     hertz = {'pin_name': hertz} --> {string: int}
    """
    GPIO.setmode(GPIO.BOARD)  # choose BCM or BOARD numbering schemes.
    for i in pins:
        GPIO.setup(pins[i],GPIO.OUT)
    #set object as global
    global p_red, p_green, p_blue
    # create an object for PWM on ports per dictionary at 50 Hertz   
    p_red = GPIO.PWM(pins['red'], Hz['red'])
    p_green = GPIO.PWM(pins['green'],Hz['green'])
    p_blue = GPIO.PWM(pins['blue'], Hz['blue'])
    # start the PWM on 0 percent duty cycle
    p_red.start(0)
    p_blue.start(0)
    p_green.start(0)

def inputs():
    global red_duty, blue_duty, green_duty, t
    red_duty = input("Enter the duty cycle for red (0-100): \n")
    blue_duty = input("Enter the duty cycle for blue (0-100): \n")
    green_duty = input("Enter the duty cycle for green (0-100): \n")
    t = input("How long in seconds would you like to see the color you've created? \n")                  

def run():
    inputs()
    p_red.ChangeDutyCycle(red_duty)
    p_blue.ChangeDutyCycle(blue_duty)
    p_green.ChangeDutyCycle(green_duty)
    time.sleep(t)
    
def stop():
    """
    Stops the PWM output
    """
    p_red.stop()
    p_blue.stop()
    p_green.stop()

def main():
    PWM_setup()
    run()
    stop()
    GPIO.cleanup()

if __name__=="__main__":
    
    main()
