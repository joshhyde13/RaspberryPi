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
    p_red.ChangeDutyCycle(int(red_duty))
    p_blue.ChangeDutyCycle(int(blue_duty))
    p_green.ChangeDutyCycle(int(green_duty))
    print_values()
    time.sleep(int(t))


def print_statement():
    print("\n============================")
    print("This progam allows you to use")
    print("pulse width modulation (PWM)")
    print("to create any color using a")
    print("red, green, blue LED light.\n")
    print("Thousands of tiny red, green and")
    print("blue lights are how modern TVs")
    print("project images on the screen.\n")
    print("The color is determined by the")
    print("ratio of the three lights. The ")
    print("brightness is determined by the.")
    print("total value of the duty cycles...")
    print("which is simply the % of time the")
    print("light is pulsed off.\n")
    """
    print("")
    print("         brigher      dimmer")
    print("         ___^____  ______^______")
    print("        /        \\/             \\")
    print("ON-->   ___   ___       ___      _")
    print("       |   | |   |     |   |    |")
    print("       |   | |   |     |   |    |")
    print("       |   | |   |     |   |    |")
    print("       |   | |   |     |   |    |")
    print("       |   |_|   |_____|   |____|")
    print("OFF-->")
    print("===============================\n")
    """
    print("Press enter to begin.")
    print("Press ctrl + c to end.")
    input()
    
def print_values():
    total = int(red_duty) + int(blue_duty) + int(green_duty)
    red_pct = int(red_duty)/total*100
    blue_pct = int(blue_duty)/total*100
    green_pct = int(green_duty)/total*100
    tot_pct = red_pct + blue_pct + green_pct
    print("\nRED   BLUE    GREEN   Total")
    print(" {}    {}      {}      {}".format(red_duty, blue_duty, green_duty, total))
    print(" {}%   {}%     {}%     {}%".format(round(red_pct), round(blue_pct), round(green_pct), round(tot_pct)))
    print("\nPress enter to continue,")
    print("ctrl + c to end....")
        
def stop():
    """
    Stops the PWM output
    """
    p_red.stop()
    p_blue.stop()
    p_green.stop()

def main():
    print_statement()
    for i in range(100):
        PWM_setup()
        run()
        stop()
        input()
    GPIO.cleanup()

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
