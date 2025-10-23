import RPi.GPIO as GPIO
import time

def bin_arr(number):
    arr = [0]*8
    s = bin(int(number))[2:].zfill(8)
    for i in range(8):
        arr[i] = int(s[i])
    return arr

class R2R_ADC:
    def __init__(self):
        self.works = [26,20,19,16,13,12,25,11]
        #self.works.reverse()
        self.bits = [0]*8
        self.check = 21
        self.highest_lvl = 3.13

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.works, GPIO.OUT)
        GPIO.setup(self.check, GPIO.IN)

    def set_number(self, number):
        if(0 <= number <= 255 ):
            bin_array = bin_arr(number)
            for i in range(8):
                self.bits[i] = int(bin_array[i])
            for i in range(8):
                GPIO.output(self.works[i],self.bits[i])
        else:
            #print("за пределами")
            pass

    def sequential_counting_adc(self,upd):
        GPIO.output(self.works,0)
        num = 0
        if upd:
            GPIO.output(self.works,0)
        while(GPIO.input(self.check) == 0):
            num += 1
            #print(num,end=" ")
            self.set_number(num)
            time.sleep(0.001)
        return num

    def deinit(self):
        #print(bits)
        GPIO.output(self.works,0)
        GPIO.cleanup()



if __name__ == "__main__":
    try:
        my_plate = R2R_ADC()
        update=0
        ch = 0
        last_ans = -1
        while True:
            ans = my_plate.sequential_counting_adc(update)
            if(ans != 0):
                print(float(int(ans/255 * 3.16 * 100))/100)
            last_ans = ans
            time.sleep(0.01)
    finally:
        my_plate.deinit()

