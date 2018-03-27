class rpi_setups(object):
    """
    *******************************************
    Import necessary libraries and sets up pins
    *******************************************
    """

    def __init__(self):
        self.pins = pins
        
    def rpi_rbg_setup(self, pins = [11, 12, 13]):
        GPIO.setmode(GPIO.BOARD)
        for i in pins:
            GPIO.setup(i,GPIO.OUT)
        red, blue, green = 11, 13, 12
            
    def pin_cleanup(self):
        GPIO.cleanup()
        print("\nPins reset.")
        
    def blink(self, color_order =['red','blue', 'green'], color_pin={'red':11, 'blue':13, 'green':12}, time_on = 1, time_off = 1, n_times = 1):
        """
        INPUT:
           color_order: library of color order
           color_pin: dictionary assigning colors to pins
           time_on: time in seconds you would like each light on
           time_off: time in seconds you would like each light off
           n_times: number of times to cycle through colors
        OUTPUT:
           colored lights blink in order and to time input
        """
        for i in range(0,n_times):
            for color in color_order:
                GPIO.output(color_pin[color], True)
                print("\n{} on.".format(color))
                time.sleep(time_on)
                GPIO.output(color_pin[color], False)
                print("\n{} off.".format(color))
                time.sleep(time_off)

    def run_program(self):
        rpi.rpi_rbg_setup()
        rpi.user_inputs()
        print("\nComplete.")
        print("\nCleaning up GPIO pins...")
        rpi.pin_cleanup()
        print("\nDone.")

    def user_inputs(self):
        a = input("How many seconds would you like the lights on? ")
        #time_on_input = input("How many seconds would you like the lights on? ")
        time_off_input = input("How many seconds would you like the lights off? ")
        n_times_input = input("How many times would you like to cycle through the colors? ")
        color1 = input("\nWhich color would you like to blink first? (red, green, or blue): ")
        color2 = input("\nWhich color would you like to blink second? (red, green, or blue): ")
        color3 = input("\nWhich color would you like to blink last? (red, green, or blue): ")
        color_list = [color1, color2, color3]
        rpi.blink(time_on = int(a), time_off=int(time_off_input), n_times=int(n_times_input), color_order = color_list)
	
if __name__ == "__main__":

    print("\nRunning...")
    import RPi.GPIO as GPIO
    import time
    pins = 'none'
    rpi = rpi_setups()
    
    rpi.run_program()
