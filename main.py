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




import json
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np

sample_frequency = 44100
duration = 0.5

number_of_samples = sample_frequency * duration
time_intervals = np.arange(0, duration, 1/sample_frequency)

cos = 0.7 * np.cos(2 * np.pi * 5000 * time_intervals)

# Serializing json
# json_object = json.dumps({
#     "y": cos.tolist(),
#     "x": time_intervals.tolist(),
# }, indent=4)

 
# # Writing to sample.json
# with open("cos.json", "w") as outfile:
#     outfile.write(json_object)

np.savetxt("cos_y.csv", cos)
np.savetxt("cos_x.csv", time_intervals)

S = np.fft.fft(cos, norm="forward")        

S_oneside = S[:int(number_of_samples/2)]
f = sample_frequency * np.arange(0, number_of_samples/2) / number_of_samples
S_meg = np.abs(S_oneside) / (number_of_samples/2)
plt.plot(f, S_meg)

plt.title('Magnitude Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.savefig("output.jpg")
