import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import hilbert, chirp
import numpy as np
from scipy.signal import resample

samplerate, data = wavfile.read('./planet/2-sem/signal.WAV')

data = data.tolist()
data = data[:70000]

arrx = []
for i in range(70000):
    data[i] = data[i] - 130
    arrx.append(i)

new_data = resample(data,int(len(data) / 1))

xah = hilbert(new_data)
amplitude_envelope = np.abs(xah)

plt.plot(arrx[0:600],amplitude_envelope[0:600],color = 'b')
plt.plot(arrx[0:600],data[0:600],color='r')
plt.show()

