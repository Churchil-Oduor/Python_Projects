import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

dt = 0.001
t  = np.arange(0, 1, dt)

# creating two signals with different frequencies.
f = np.sin(2 * np.pi * 200 * t) + np.sin(2 * np.pi * 50 * t)

f_clean = f

# adding random noise of amplitude 2.5..noise is additive.
f = f + 2.5 * np.random.randn(len(t))

n = len(t)
fhat = np.fft.fft(f, n)
PSD = fhat * np.conj(fhat) / n
freq = (1/(dt*n)) * np.arange(n)
L = np.arange(1, np.floor(n/2), dtype='int')
fig, axs = plt.subplots(2, 1)

#plt.plot(t, f, color='r', linewidth=1.5, label='Noisy')
#plt.plot(t, f_clean, color='k', linewidth=1.5, label='clean')
#plt.xlim(t[0], t[-1])
#plt.legend()
#plt.show()

plt.sca(axs[0])
plt.plot(t, f, color='c', linewidth=1.5, label='Noisy')
plt.plot(t, f_clean, color='k', linewidth=2, label='Clean')
plt.xlim(t[0], t[-1])
#plt.legend()
#plt.show()

plt.sca(axs[1])
plt.plot(freq[L], PSD[L], color='c', linewidth=2, label='Noisy')
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()
plt.show()
