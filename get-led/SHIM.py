import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26

GPIO.setup(led, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

pwm = GPIO.PWM(led, 1000)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1
    if(duty >= 20):
        duty = 0
