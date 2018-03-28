"""
Used starter code from:
http://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
"""

import RPi.GPIO as GPIO 
import time

def print_statement():
    print("\n=================================")
    print("This program will show the many")
    print("colors that can be created with")
    print("a red, green, blue LED light.")
    print("=================================\n")
    print("Thousands of tiny red, green and")
    print("blue lights are how modern TVs")
    print("project images on the screen.\n")
    #print("This program is set at 100Hz with")
    #print("with duty cycles combined as")
    #print("multiples of 10.\n")
    #print("For hardware seup see: link")
    print("To begin, please press enter.")
    print("To cancel press ctrl + C\n")
    print("ENJOY!!!\n")
    input()

 
def PWM_setup(pins={'red':11, 'green':12, 'blue':13}, Hz={'red':500, 'green':500, 'blue':500}):
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


def run(t=.05):
    """
    INPUT:
       t = time in seconds between PWM changes
       duty_cycle_range = range from 0 to 100
    """
    # start the PWM on 0 percent duty cycle
    p_red.start(0)
    p_blue.start(0)
    p_green.start(0)
    # duty cycle value can be 0.0 to 100.0%, floats are OK
    l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for g in l:
        for b in l:
            for r in l:
                p_red.ChangeDutyCycle(r)
                p_blue.ChangeDutyCycle(b)
                p_green.ChangeDutyCycle(g)
                time.sleep(t)
                print("r:{} b:{} g:{}".format(r, b, g))
    # can also change the frequency Hz (floats also work) --> p_red.ChangeFrequency(100)

def stop():
    """
    Stops the PWM output
    """
    p_red.stop()
    p_blue.stop()
    p_green.stop()
    print("\nResetting pins...")

def main():
    PWM_setup()
    print_statement()
    run()
    stop()
    GPIO.cleanup()
    print("Done")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop()
