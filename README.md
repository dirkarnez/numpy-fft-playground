numpy-fft-playground
====================
- [How to Do FFT in MATLAB - YouTube](https://www.youtube.com/watch?v=XEbV7WfoOSE)
- [Discrete Fourier Transform (numpy.fft) — NumPy v1.26 Manual](https://numpy.org/doc/stable/reference/routines.fft.html)

### Matlab
![](./matlab/0.7_magnitude_50hz.jpg)

### numpy
![](./output.jpg)

### Notes
- Some discrete signal DOES NOT depend on sampling Frequency:
  - Hard-coded signals
  - Constant signals
  - Random signals
- Some discrete signal DOES depend on sampling Frequency:
  - Sampled signal (audio)
  - parametic signal (math functions like sin / cos / etc.)
- Sampling Frequency affects the frequency range
  - Nyquist–Shannon sampling theorem
- if N is odd
  - ceil(N / )
- if N is even
  - (N/2) + 1
- Bigger the N, the narrower each freq bin (more bin)
