import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN)

while True:
    
    print(GPIO.input(16))
    time.sleep(0.5)