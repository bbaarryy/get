import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26

GPIO.setup(led, GPIO.OUT)
GPIO.setup(13, GPIO.IN)

flag = 0
T = 0.2
while True:
    
    if(GPIO.input(13)):
        flag = abs(flag-1)
        GPIO.output(led, flag)
        
        time.sleep(T)

