import RPi.GPIO as GPIO

import MCP4725_driver as MCP
import signal_generator as sg
import time

print("start")
amplitude = 3
signal_frequency = 5
sampling_frequency = 1000
my_plate = MCP.MCP4725(4096)
now_time = 0

try:
    while(True):
        now_time += 1/sampling_frequency
        #print(now_time)
        my_plate.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_frequency, now_time))
        sg.wait_for_sampling_period(sampling_frequency)
except Exception:
    my_plate.deinit()
finally:
    my_plate.deinit()
