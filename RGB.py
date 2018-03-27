import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
red, blue, green = 11, 13, 12

GPIO.output(red, True)
time.sleep(1)
GPIO.output(red, False)

GPIO.cleanup()

for i in range(0,3):
	for v in dic:
		GPIO.output(dic[v], True)
		time.sleep(1)
		GPIO.output(dic[v], False)
		time.sleep(1)
