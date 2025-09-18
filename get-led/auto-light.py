import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26

GPIO.setup(led, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

flag = 0
T = 0.2
while True:
    GPIO.output(led,(GPIO.input(6)-1))
    time.sleep(0.01)
    

