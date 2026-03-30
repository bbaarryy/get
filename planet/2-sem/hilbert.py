import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import hilbert, chirp
import numpy as np

samplerate, data = wavfile.read('./planet/2-sem/signal.WAV')

data = data.tolist()
data = data[:70000]

arrx = []
for i in range(70000):
    data[i] = data[i] - 130
    arrx.append(i)


xah = hilbert(data)
amplitude_envelope = np.abs(xah)

plt.plot(arrx,amplitude_envelope,color = 'b')
plt.plot(arrx,data,color='r')
plt.show()

