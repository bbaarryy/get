import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import hilbert
from scipy.signal import resample
from scipy import signal

fs, data = wavfile.read('./planet/2-sem/signal.WAV')

samplerate, data = wavfile.read('./planet/2-sem/signal.WAV')

data = data.tolist()

new_data = []
for i in range(0,len(data)):
    new_data.append(data[i] - 130)
    data[i] = data[i] - 130

new_data = signal.resample(new_data,int(len(new_data) / 2.65))

SYNC_STR = "000011001100110011001100110011000000000"

xah = hilbert(new_data)
amplitude_envelope = np.abs(xah)

print(amplitude_envelope[0:100])

print("Огибающая рассчитана для всех данных.")

width = 2080
height = len(amplitude_envelope) // width
truncated_envelope = amplitude_envelope[:height * width]
image_matrix = truncated_envelope.reshape((height, width))

plt.figure(figsize=(15,10))
plt.imshow(image_matrix, cmap='gray', aspect='auto')
plt.tight_layout()
plt.show()