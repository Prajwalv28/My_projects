import numpy as np

class Layer:
    def __init__(self):
        pass

    def forward(self, input):
        raise NotImplementedError

    def backward(self, output_grad):
        raise NotImplementedError


class Linearlayer(Layer):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.input_size = input_size
        self.output_size = output_size

        limit = np.sqrt(6 / (input_size + output_size))
        self.weights = np.random.uniform(-limit, limit, (output_size, input_size))
        self.bias = np.zeros(output_size)

        self.grad_weights = np.zeros_like(self.weights)
        self.grad_bias = np.zeros_like(self.bias)

    def forward(self, input):
        if input.shape[1] != self.input_size:
            raise ValueError(f"Input dimension mismatch. Expected {self.input_size}, got {input.shape[1]}")

        self.input = input  # Store for backward pass
        return np.dot(input, self.weights.T) +self.bias

    def backward(self, output_grad):
        # Ensure output_grad is 2D
        if output_grad.ndim == 1:
            output_grad = output_grad.reshape(-1, 1)

        input_grad = np.dot(output_grad, self.weights)
        self.grad_weights = np.dot(output_grad.T, self.input)
        self.grad_bias = np.sum(output_grad, axis=0)

        return input_grad


# Sigmoid activation layer
class Sigmoid(Layer):
    def forward(self, input):
        self.output = 1 / (1 + np.exp(-input))
        return self.output

    def backward(self, output_grad):
        return self.output * (1 - self.output) * output_grad

class Tanh(Layer):
    def forward(self, input):
        self.output = np.tanh(input)
        return self.output

    def backward(self, output_grad):
        return (1 - self.output ** 2) * output_grad

class ReLU(Layer):
    def forward(self, input):
        self.input = input
        return np.maximum(0, input)

    def backward(self, output_grad):
        input_grad = output_grad.copy()
        input_grad[self.input <= 0] = 0
        return input_grad

class BinaryCrossEntropyLoss(Layer):
    def forward(self, predictions, target):
        # Avoid division by zero
        predictions = np.clip(predictions, 1e-12, 1. - 1e-12)
        # Calculate binary cross-entropy
        loss = -np.mean(target * np.log(predictions) + (1 - target) * np.log(1 - predictions))
        return loss

    def backward(self, predictions, target):
        # Avoid division by zero
        predictions = np.clip(predictions, 1e-12, 1. - 1e-12)
        # Compute gradient of loss with respect to predictions
        input_grad = (predictions - target) / (predictions * (1 - predictions) * predictions.shape[0])
        return input_grad

class Sequential(Layer):
    def __init__(self):
        super().__init__()
        self.layers = []

    def add(self, layer):
        self.layers.append(layer)

    def forward(self, input):
        for layer in self.layers:
            input = layer.forward(input)
        return input

    def backward(self, output_grad):
        for layer in reversed(self.layers):
            output_grad = layer.backward(output_grad)
        return output_grad

def save_model(model, file_name):
    weights = {}
    for idx, layer in enumerate(model.layers):
        if hasattr(layer, 'weights'):
            weights[f'weights_{idx}'] = layer.weights
            weights[f'bias_{idx}'] = layer.bias
    np.savez(file_name, **weights)

def load_model(model, file_name):
    data = np.load(file_name)
    for idx, layer in enumerate(model.layers):
        if hasattr(layer, 'weights'):
            layer.weights = data[f'weights_{idx}']
            layer.bias = data[f'bias_{idx}']


