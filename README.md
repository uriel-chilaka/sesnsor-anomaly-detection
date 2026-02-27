# Sensor Fusion Anomaly Detection 

## Overview

This project implements an end-to-end sensor fusion anomaly detection system using an Arduino Grove Beginner Kit and a PyTorch autoencoder.

The system collects environmental sensor data (light, sound, temperature), performs sliding-window feature engineering, and trains an unsupervised neural network to model normal behavior. Anomalies are detected using reconstruction error.

---

## System Architecture

1. Arduino collects real-time sensor data.
2. Data is logged and converted into time-series features.
3. A PyTorch autoencoder is trained on normal data.
4. Reconstruction error is used to detect anomalies.

---

## Sensors Used

- Light sensor
- Sound sensor
- Temperature sensor

---

## Machine Learning Approach

- Sliding window feature extraction (mean, std)
- Feature normalization (StandardScaler)
- Autoencoder (dim → 8 → 3 → 8 → dim)
- Reconstruction error thresholding (mean + 3σ)

---

## Results

The model successfully learns patterns of normal environmental behavior and flags deviations using anomaly scores.

---

## How to Run

### 1. Install dependencies
### 2. Train model
### 3. Detect anomalies

## Future Improvements

- Real-time anomaly detection loop
- Raspberry Pi edge deployment
- Model comparison (KMeans vs Autoencoder)
- Live dashboard
