import numpy as np

np.random.seed()

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



X = [
        [1, 4, 5, 8], 
        [1, 5, 8, 9], 
        [2, 6, 8, 9]
        ]

layer1 = Layer_Dense(4, 3)
layer2 = Layer_Dense(3, 2)

layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)
