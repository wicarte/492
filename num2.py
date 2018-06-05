import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
import time

led1 = 17
led2 = 27
led3 = 22
button1 = 5
button2 = 6
button3 = 13
button4 = 12

gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)
gpio.setup(led3, gpio.OUT)
gpio.setup(button1, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(button2, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(button3, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(button4, gpio.IN, pull_up_down = gpio.PUD_DOWN)

while True:
	if gpio.input(button1) == gpio.HIGH:
		#print "button 1 pressed"
		gpio.output(led1, gpio.HIGH)
		gpio.output(led2, gpio.LOW)
		gpio.output(led3, gpio.LOW)
	elif gpio.input(button2) == gpio.HIGH:
		gpio.output(led1, gpio.HIGH)
		gpio.output(led2, gpio.HIGH)
		gpio.output(led3, gpio.LOW)
		#print "button 2 pressed"
	elif gpio.input(button3) == gpio.HIGH:
		gpio.output(led1, gpio.HIGH)
		gpio.output(led2, gpio.HIGH)
		gpio.output(led3, gpio.HIGH)
		#print "button 3 pressed"
	elif gpio.input(button4) == gpio.HIGH:
		gpio.output(led1, gpio.LOW)
		gpio.output(led2, gpio.LOW)
		gpio.output(led3, gpio.LOW)
		#print "button 4 pressed"
