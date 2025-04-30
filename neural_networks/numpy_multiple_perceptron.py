import numpy as np
inputs = [1, 2, 3, 4.5]

weights =[
    [3, 8, 9, 1], 
    [2, 6, 8, -1], 
    [3, 5, 7, 8]
    ]

biases = [1, 5, 5]
output = np.dot(weights, inputs) + biases
print(output)