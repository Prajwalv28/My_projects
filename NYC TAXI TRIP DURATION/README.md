# ETA Unlocked 🚕 – Predicting NYC Taxi Trip Duration with Deep Neural Networks

## 📌 Project Overview

This project focuses on building a custom deep learning model from scratch to predict the **trip duration of NYC taxi rides** using key spatial and temporal features. The goal was to explore different network architectures, activation functions, and optimization techniques to improve predictive accuracy.

The final model achieved a **Root Mean Squared Logarithmic Error (RMSLE) of 0.5637**, demonstrating strong performance on the regression task.

---

## 🧠 Techniques Used

- Custom-built Neural Network Library (Forward & Backward Pass Implemented)
- Sigmoid, Tanh, and ReLU Activation Functions
- Early Stopping Based on Validation Loss
- MinMax Feature Normalization
- Feature Engineering: Haversine Distance, Pickup/Dropoff Time Attributes
- Evaluation Metric: RMSLE

---

## 📊 Dataset

- Source: Modified NYC Taxi Trip Duration dataset
- Format: `.npy` file with `X_train`, `y_train`, `X_test`, `y_test` dictionaries
- Features used:
  - `passenger_count`
  - `pickup_hour`, `pickup_day`, `pickup_month`
  - `dropoff_hour`, `dropoff_day`, `dropoff_month`
  - `distance` (Haversine)

---

## 🏗️ Model Architecture

Three different architectures were tested:

1. **Model 1**: `64 → 32 → 16`, ReLU, RMSLE: **0.5637**
2. **Model 2**: `150 → 100 → 50`, ReLU, RMSLE: **0.797**
3. **Model 3**: `256 → 128 → 64`, ReLU, RMSLE: **0.6077**

Each model was trained with:
- `batch_size = 32`
- `learning_rate = 0.1`
- `early_stopping patience = 3`

---

## 📈 Results & Insights

- Best performance was achieved using `Model 1` with ReLU activations.
- Hyperbolic Tangent activation helped in earlier convergence during XOR tests but ReLU proved more stable for real-world data.
- Early stopping was key to avoiding overfitting.

---

## 📁 Files

- `Neural_networklibrary.py`: Core neural network components (layers, loss, activation)
- `model1.py`,` model2.py`, ` model3.py`: scripts to train and evaluate different models
- `data_preprocessing.py`: Processed dataset for training and testing
- `XOR_file.py`: XOR classification test using Sigmoid
- `XOR_Tanh.py`: XOR classification test using Tanh

---

## 💡 Future Improvements

- Extend to multi-modal inputs (weather, traffic)

---

## 🧑‍💻 Author

**Prajwal Venkat Venkatesh**  
📧 prajwalvenkatv@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/prajwal-venkat-v-9654a5180)

