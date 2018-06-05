import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
import time
pin1 = 17
pin2 = 27
pin3 = 22

gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)
gpio.setup(pin3, gpio.OUT)

while True:
	number = input("Choose a number between 1 and 3: ")
	while number != 1 and number != 2 and number != 3:
		number = input("Not a valid input. Choose a number between 1 and 3: ")
	if number == 1:
		gpio.output(pin1, gpio.HIGH)
		gpio.output(pin2, gpio.LOW)
		gpio.output(pin3, gpio.LOW)
	elif number == 2:
		gpio.output(pin1, gpio.HIGH)
		gpio.output(pin2, gpio.HIGH)
		gpio.output(pin3, gpio.LOW)
	elif number == 3:
		gpio.output(pin1, gpio.HIGH)
		gpio.output(pin2, gpio.HIGH)
		gpio.output(pin3, gpio.HIGH)
	#gpio.cleanup()
