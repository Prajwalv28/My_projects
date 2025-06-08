from Neural_networklibrary import *
import numpy as np

# Checking for Hyperbolic tangent activation
print(" \nChecking for Hyperbolic tangent activation")

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[0]])

# Model definition
model = Sequential()
model.add(Linearlayer(2, 2))
model.add(Tanh())
model.add(Linearlayer(2, 1))
model.add(Tanh())

# Training parameters
lr_rate = 0.1
nm_epochs = 10000

# Instantiate the loss layer before the training loop
loss_layer = BinaryCrossEntropyLoss()

# Training loop
for epoch in range(nm_epochs):
    # Forward pass
    predictions = model.forward(X)
    # Compute loss
    loss = loss_layer.forward(predictions, Y)
    # Compute gradients with respect to predictions
    loss_grad = loss_layer.backward(predictions, Y)
    # Backward pass through the model
    input_grad = loss_grad
    for layer in reversed(model.layers):
        if hasattr(layer, 'backward'):
            input_grad = layer.backward(input_grad)

    # Parameters update
    for layer in model.layers:
        if isinstance(layer, Linearlayer):
            layer.weights -= lr_rate * layer.grad_weights
            layer.bias -= lr_rate * layer.grad_bias

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# Calculate final accuracy
output = model.forward(X)
print("\n Predicted Output for tangent activation:\n", output)
correct_pred = np.sum((output > 0.5) == Y)
total = Y.shape[0]
acc = correct_pred / total
print(f"Final Accuracy: {acc}")

# Save the model weights
save_model(model, "xor_solved_w_tanh.npz")

# Load the model weights
load_model(model, "xor_solved_w_tanh.npz")

def model_weights(model):
    for idx, layer in enumerate(model.layers):
        if hasattr(layer, 'weights'):
            print(f"Layer {idx} weights:\n", layer.weights)
            print(f"Layer {idx} biases:\n", layer.bias)

model_weights(model)

def tanh_outputs(model, X):
    input = X
    for idx, layer in enumerate(model.layers):
        output = layer.forward(input)
        if isinstance(layer,Sigmoid ):
            print(f"tanh layer {idx} output:\n", output)
        input = output

tanh_outputs(model, X)
