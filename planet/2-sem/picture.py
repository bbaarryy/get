import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import hilbert
from scipy.signal import resample
from scipy import signal

fs, data = wavfile.read('/home/dimon/projects/get/planet/2-sem/signal.WAV')
samplerate, data = wavfile.read('./planet/2-sem/signal.WAV')

data = data.tolist()

new_data = []
for i in range(0,len(data)):
    new_data.append(data[i] - 130)
    data[i] = data[i] - 130


amplitude_envelope = np.abs(hilbert(data))

duration = len(data) / fs
pixels = resample(amplitude_envelope, int(duration * 4160))

SYNC = np.array([0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0])
corr = np.correlate(pixels[:4160], SYNC * np.max(pixels), mode='valid')
start_index = np.argmax(corr)

width = 2080
aligned_pixels = pixels[start_index:]
height = len(aligned_pixels) // width
image_matrix = aligned_pixels[:height * width].reshape((height, width))

image_matrix = np.roll(image_matrix, shift=1040, axis=1)

plt.figure(figsize=(15, 10))
plt.imshow(image_matrix, cmap='gray', aspect='auto')
plt.tight_layout()
plt.show()