import numpy as np

np.random.seed(0)

# creating a template of creating a neural layer.
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        # creation of weights and biases
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        # getting the output of the layers.
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    # the input being passed is a matrix
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

X = [
        [1, 2, 3, 2.5],
        [2.0, 5.0, -1.0, 2.0],
        [-1.5, 2.7, 3.3, 0.8]
    ]

# creating weights to be be multiplied with the batch input X
layer1 = Layer_Dense(4, 5)

# Getting output using the forward method
layer1.forward(X)
activation = Activation_ReLU()
activation.forward(layer1.output)

print(activation.output)

