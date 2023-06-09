import numpy as np

#layer 1
inputs = [[1, 2, 3, 2.5],
            [2.0, 5.0, -1.0, 2.0],
            [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]
layer1_output = np.dot(inputs, np.array(weights).T) + biases

#layer1_outputs are going to form layer 2 inputs
weights2 = [[0.1, -0.14, 0.5],
        [-0.5, 0.12, -0.33],
        [-0.44, 0.73, -0.13]]

biases = [-1, 2, -0.5]
layer2_outputs = np.dot(layer1_output, np.array(weights2).T) + biases

print(layer2_outputs)

