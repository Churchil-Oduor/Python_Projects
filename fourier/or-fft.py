import numpy as np
import matplotlib.pyplot as plt
import time as ti

# Number of samples
N = 100

angle = -2j * np.pi / N  # Negative sign for correct DFT calculation

# Generate sine wave signal
signal = []
freq = 20 # specify the signal frequency here.


# getting the sampled data points
for t in range(N):
    data_point = np.sin(2 * np.pi * freq * t / N)  # Normalizing by N
    signal.append(data_point)

# Compute DFT
DFT = []

for k in range(N):  # Computing first 10 frequencies
    transform = 0
    for n in range(N):
        transform += signal[n] * np.exp(angle * k * n) 
    DFT.append(transform)

# Plot original signal and DFT magnitude spectrum
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(signal, label="Original Signal")
plt.title("Time Domain Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(range(N//2), np.abs(DFT[:N//2]), marker='o', label="DFT Magnitude")
plt.title("DFT Magnitude Spectrum")
plt.xlabel("Frequency Index (k)")
plt.ylabel("Magnitude")
plt.legend()

plt.tight_layout()
plt.show()

