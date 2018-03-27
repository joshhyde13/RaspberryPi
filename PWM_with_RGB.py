
import RPi.GPIO as GPIO # always needed with RPi.GPIO
import time

GPIO.cleanup()
  
GPIO.setmode(GPIO.BOARD)  # choose BCM or BOARD numbering schemes.

def PWM_setup(pins = {'red': 11, 'green':12, 'blue':13}):
    """
    Set GPIO pins as output
    """
    GPIO.setmode(GPIO.BOARD)
    for i in pins:
        GPIO.setup(pins[i],GPIO.OUT)

PWM_setup()  
  
# create an object for PWM on ports 11, 12, 13 at 50 Hertz   
p_red = GPIO.PWM(11, 100)
p_green = GPIO.PWM(12, 50)
p_blue = GPIO.PWM(13, 100)
 

p_red.start(0)             # start the PWM on x percent duty cycle
p_blue.start(0)
p_green.start(0)
for i in range(1,50):
    p_red.ChangeDutyCycle(i)
    p_blue.ChangeDutyCycle(50-i)
    p_green.ChangeDutyCycle(25-i/2)
    time.sleep(.2)

# duty cycle value can be 0.0 to 100.0%, floats are OK  
#p_red.ChangeFrequency(100)  # change the frequency to 100 Hz (floats also work)            

p_red.stop()                # stop the PWM output  
p_blue.stop()
p_green.stop()

GPIO.cleanup()          # when your program exits, tidy up after yourself
