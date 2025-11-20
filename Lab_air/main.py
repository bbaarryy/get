import RPi.GPIO as GPIO
import spidev

spi = spider.SpiDev()
spi.open(0,0)

def getAdc():
    adcResponse = spi.xfer2([0,0])
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1

try:
    for i in range(20000):
        print(getAdc(), end = '\r')
finally:
    spi.close()
