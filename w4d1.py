import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

pinNum = 17
button1 = 27
button2 = 22
duty = 50

gpio.setup(pinNum, gpio.OUT)
gpio.setup(button1, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(button2, gpio.IN, pull_up_down = gpio.PUD_DOWN)
pwmLED = gpio.PWM(pinNum, 500)
pwmLED.start(duty)

while True:
	if gpio.input(button1) == gpio.HIGH:
		print "Button 1 was pressed, increasing brightness"
		while duty < 100:
			duty = duty + 5
			time.sleep(0.5)
			pwmLED.ChangeDutyCycle(duty)
		time.sleep(0.1)
	elif gpio.input(button2) == gpio.HIGH:
		print "Button 2 was pressed, decreasing brightness"
		while duty > 0:
			duty = duty - 5
			time.sleep(0.5)
			pwmLED.ChangeDutyCycle(duty)
		time.sleep(0.1)
