import numpy as np

inputs = [1, 3, 6, 8, 9]
weights = [1, 5, -1, 6, 8]
bias =  3

outpt = np.dot(inputs, weights) + bias
print(outpt)