import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()


class Layer_Dense:
    """
    This class creates a dense layer
    """
    def __init__(self, n_inputs, n_neurons):

        """
        initializes a layer

        n_inputs: number of inputs
        n_neurons: number of neurons in layer
        """

        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        """
        does the forwad pass

        inputs: inputs fed to the layer

        """
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)



class Activation_Softmax():
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities


X, Y = spiral_data(samples=100, classes=3)

layer1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()


layer2 = Layer_Dense(3, 3)
activation2 = Activation_Softmax()


layer1.forward(X)
activation1.forward(layer1.output)

layer2.forward(activation1.output)
activation2.forward(layer2.output)

print(activation2.output[:5])







