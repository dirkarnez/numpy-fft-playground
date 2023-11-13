close all; clear; clc;
sample_frequency=500;
duration = 2;

numberofsamples = sample_frequency*duration;
timevector = 0:1/sample_frequency:duration-1/sample_frequency;

cos = 0.7*cos(2*pi*50*timevector);
S = fft(cos)
S_oneside = S(1:numberofsamples/2);
f = sample_frequency*(0:numberofsamples/2-1)/numberofsamples;
S_meg = abs(S_oneside) / (numberofsamples/2);
figure
plot(f, S_meg)
