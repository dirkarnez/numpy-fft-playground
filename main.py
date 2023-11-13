# import matplotlib

# matplotlib.use('Agg')
# import matplotlib.pyplot as plt

# import numpy as np


# t = np.arange(500)
# fourier  = np.fft.fft(0.7* np.cos(2* np.pi * 50 * t))

# print(fourier.size)
# freq = np.fft.fftfreq(t.shape[-1])

# plt.plot(freq, fourier.real, freq, fourier.imag)
# plt.savefig("123")




import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np

sample_frequency = 500
duration = 2

numberofsamples = sample_frequency * duration
timevector = np.arange(0, duration, 1/sample_frequency)

cos = 0.7 * np.cos(2 * np.pi * 50 * timevector)
S = np.fft.fft(cos)
S_oneside = S[:int(numberofsamples/2)]
f = sample_frequency * np.arange(0, numberofsamples/2) / numberofsamples
S_meg = np.abs(S_oneside) / (numberofsamples/2)
plt.plot(f, S_meg)

plt.title('Magnitude Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')


plt.savefig("output.jpg")
