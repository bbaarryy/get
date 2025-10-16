import smbus
import RPi.GPIO as GPIO
import time
import numpy
import math

def get_sin_wave_amplitude(freq, time):
    t = 1/freq
    speed = 1/t
    x = 1 - speed * (time % (2/freq))
    return abs(x)
    #sinus = math.sin(2 * 3.1415926535 * freq * time) 
    #return (sinus + 1)/2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)