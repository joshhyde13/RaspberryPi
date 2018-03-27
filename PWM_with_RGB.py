"""
Used starter code from:
http://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
"""

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


def run(t=.2, duty_cycle_range=50):
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
    for i in range(1,duty_cycle_range):
        p_red.ChangeDutyCycle(i)
        p_blue.ChangeDutyCycle(50-i)
        p_green.ChangeDutyCycle(25-i/2)
        time.sleep(t)
    # can also change the frequency Hz (floats also work) --> p_red.ChangeFrequency(100)

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
