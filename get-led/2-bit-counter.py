import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16,12,25,17,27,23,22,24]
for i in range(len(leds)):
    GPIO.setup(leds[i], GPIO.OUT)

led = 26

GPIO.setup(led, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

GPIO.setup(9,GPIO.IN)
GPIO.setup(10,GPIO.IN)

def binn(n):
    s = ""
    m = n
    while(m > 0):
        s = str(m%2) + s
        m = m//2
    s = s.zfill(8)
    return s

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
    return s

curr = 0
bi = 0
while True:
    GPIO.output(led,(GPIO.input(6)-1))

    bi = watch_num(curr)
    if(GPIO.input(9) and GPIO.input(10)):
        curr = 2**8-1
        print(binn(curr),curr)
        time.sleep(0.4)
    elif(GPIO.input(9)):
        curr+=1
        if(curr >= 2**8):
            curr = 0
        time.sleep(0.4)
        print(binn(curr),curr)
    elif(GPIO.input(10)):
        curr -= 1
        curr = max(curr,0)
        time.sleep(0.4)
        print(binn(curr),curr)
    
    #time.sleep(0.1)
