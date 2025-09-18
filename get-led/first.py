import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26

GPIO.setup(led, GPIO.OUT)
flag = 0
T = 1
while True:
    GPIO.output(led, flag)
    flag = abs(flag-1)
    time.sleep(T)

