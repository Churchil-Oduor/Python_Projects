import numpy as np
import matplotlib.pyplot as plt


n = 50
w = np.exp(-2j * np.pi / n)
x, y = np.meshgrid(np.arange(n), np.arange(n))
DFT = np.power(w, x*y)
DFT = np.real(DFT)
plt.imshow(DFT)
plt.show()