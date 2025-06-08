import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from data_preprocessing import X_test,X_train,y_train,y_test
from Neural_networklibrary import *
import matplotlib.pyplot as plt

# Define columns for scaling
cord_columns = ['passenger_count','pickup_month','pickup_day','pickup_hour', 'dropoff_month','dropoff_day', 'dropoff_hour', 'distance']
print("\nFeatures used in model :", cord_columns)
# Normalize the data using MinMaxScaler
scaler_minmax = MinMaxScaler()
X_train[cord_columns] = scaler_minmax.fit_transform(X_train[cord_columns])
X_test[cord_columns] = scaler_minmax.transform(X_test[cord_columns])

# Create DataFrame objects for training and test data
X_train_fnl = pd.DataFrame(X_train[cord_columns])
X_test_fnl = pd.DataFrame(X_test[cord_columns])

# Split the final training data into training and validation sets
X_train_fnl, X_val_fnl, y_train_fnl, y_val_fnl = train_test_split(X_train_fnl, y_train, test_size=0.2, random_state=42)


def model_construct(input_size, l1, l2, l3):
    model = Sequential()
    model.add(Linearlayer(input_size, l1))
    model.add(ReLU())
    model.add(Linearlayer(l1, l2))
    model.add(ReLU())
    model.add(Linearlayer(l2, l3))
    model.add(ReLU())
    model.add(Linearlayer(l3, 1)) 
    return model

# Define the RMSLE loss function
def rmsle(predictions, target):
    predictions = np.clip(predictions.squeeze(), a_min=1e-9, a_max=None)  # Ensure predictions are positive
    return np.sqrt(np.mean((np.log1p(predictions) - np.log1p(target)) ** 2))

# Training function with early stopping and batch processing
def train_model(X_train, y_train, X_val, y_val, input_size, l1, l2, l3, lr_rate, epochs, patience, batch_size):
    X_train_np = X_train.values.astype(np.float32)
    y_train_np = y_train.values.astype(np.float32)
    X_val_np = X_val.values.astype(np.float32)
    y_val_np = y_val.values.astype(np.float32)

    # Assuming model_construct is defined elsewhere to construct the model
    model = model_construct(input_size, l1, l2, l3)

    best_loss = np.inf
    steps_imp = 0

    train_losses = []
    val_losses = []

    for epoch in range(epochs):
        for i in range(0, len(X_train_np), batch_size):
            X_batch = X_train_np[i:i+batch_size]
            y_batch = y_train_np[i:i+batch_size]

            train_predictions = model.forward(X_batch)
            train_loss = rmsle(train_predictions, y_batch)

            loss_grad = (2 / y_batch.shape[0]) * ((np.log1p(train_predictions.squeeze()) - np.log1p(y_batch)) / (1 + train_predictions.squeeze()))
            loss_grad = loss_grad.reshape(-1, 1)  # Ensure the gradient has the correct shape for backpropagation
            model.backward(loss_grad)

            for layer in model.layers:
                if hasattr(layer, 'grad_weights'):
                    layer.weights -= lr_rate * layer.grad_weights
                    layer.bias -= lr_rate * layer.grad_bias

        # Validation loss calculation after each epoch
        val_predictions = model.forward(X_val_np)
        val_loss = rmsle(val_predictions, y_val_np)

        train_losses.append(train_loss)
        val_losses.append(val_loss)

        print(f"Epoch {epoch}: Train Loss = {train_loss}, Validation Loss = {val_loss}")

        if val_loss < best_loss:
            best_loss = val_loss
            steps_imp = 0
        else:
            steps_imp += 1
            if steps_imp >= patience:
                print(f"Stopping early at epoch {epoch}")
                break

    return model, train_losses, val_losses

# hyperparameters configuration
model_hyp = {'l1': 64, 'l2': 32, 'l3': 16, 'lr_rate': 0.1}
print(f"\nTraining model1 with selected hyperparameters configuration\n")
model, train_losses, val_losses = train_model(X_train_fnl, y_train_fnl, X_val_fnl, y_val_fnl, input_size=X_train_fnl.shape[1], **model_hyp, epochs=30, patience=3, batch_size=32)

# Plot training and validation losses
plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Training Loss')
plt.plot(val_losses, label='Validation Loss')
plt.title("Training and Validation Loss")
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Assuming save_model and load_model are defined elsewhere to handle model serialization
save_model(model, "model1_weights.npz")

model_hyp = model_hyp.copy()
del model_hyp['lr_rate']  # Remove the lr_rate key

loaded_model = model_construct(input_size=X_train_fnl.shape[1], **model_hyp)
load_model(loaded_model, "model1_weights.npz")

# Convert test set to numpy arrays and correct format
X_test_np = X_test_fnl.values.astype(np.float32)
y_test_np = y_test.values.astype(np.float32)

# Forward pass on the test set
test_predictions = loaded_model.forward(X_test_np)

# Calculate RMSLE on the test set
test_rmsle = rmsle(test_predictions, y_test_np)
print(f"Test RMSLE: {test_rmsle}")