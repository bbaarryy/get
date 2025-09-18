import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16,12,25,17,27,23,22,24]
for i in range(len(leds)):
    GPIO.setup(leds[i], GPIO.OUT)


curr = 0
while True:
    GPIO.output(leds[curr],0)
    curr+=1
    curr = curr%8
    GPIO.output(leds[curr],1)
    time.sleep(0.1)
