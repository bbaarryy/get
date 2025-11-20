import jetFunctions as jet
import RPi.GPIO as GPIO
import time

file = open("./Lab_air/90data.txt",'w')
n = 221

x = 550
jet.initSpiAdc()
jet.initStepMotorGpio()

try:
    while True:
        n-=1
        if(n==0):
            break
        else:
            jet.stepBackward(5)
            x-=5
            a = str(jet.getAdc()) + ' ' + str(x)
            file.write(a + '\n')
            print(a,n)
        time.sleep(0.35)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    jet.stepForward(1100)
    jet.deinitSpiAdc()
