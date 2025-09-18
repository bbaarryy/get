import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16,12,25,17,27,23,22,24]
for i in range(len(leds)):
    GPIO.setup(leds[i], GPIO.OUT)

GPIO.setup(9,GPIO.IN)
GPIO.setup(10,GPIO.IN)

def watch_num(n):
    s = ""
    m = n
    while(m > 0):
        s = str(m%2) + s
        m = m//2
    s = s.zfill(8)

    for i in range(len(s)):
        if(s[i] == '1'):
            GPIO.output(leds[7-i],1)
        else:
            GPIO.output(leds[7-i],0)

curr = 0
while True:
    watch_num(curr)
    if(GPIO.input(9)):
        curr+=1
        time.sleep(0.4)
        print(curr)
    if(GPIO.input(10)):
        curr -= 1
        curr = max(curr,0)
        time.sleep(0.4)
        print(curr)
    #time.sleep(0.1)
