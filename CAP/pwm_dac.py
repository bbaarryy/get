import RPi.GPIO as GPIO
import time

bit = 12
duty = 0.0
test = 22

class R2R_DAC:
    def __init__(self):
        self.highest_lvl = 3.275

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(bit, GPIO.OUT)
        GPIO.setup(test, GPIO.OUT)

        self.pwm = GPIO.PWM(bit, 1000)
        self.pwm.start(duty)

    def set_voltage(self,volt):

        self.pwm.ChangeDutyCycle(volt/self.highest_lvl*100)
        print(volt/self.highest_lvl)
    
    def deinit(self):
        GPIO.output(bit,0)
        GPIO.cleanup()

my_plate = pwm()

try:
    while True:
        try:
            n = float(input("input digit:"))
            my_plate.set_voltage(float(n  + (n-2)*0.2))
        except ValueError:
            print("ошибка")
finally:
    my_plate.deinit()

