import RPi.GPIO as GPIO
import time

def buttonCallback(channel):
	print channel

if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.add_event_detect(20,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(16,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(12,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(23,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(27,GPIO.RISING,callback = buttonCallback)
    GPIO.add_event_detect(22,GPIO.RISING,callback = buttonCallback)
    while True:
    	print ''
