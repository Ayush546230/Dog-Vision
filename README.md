# 🐶 Dog Vision - Deep Learning with Transfer Learning

This project uses transfer learning to build an image classification model that identifies different dog breeds. It leverages pre-trained models to make the training process faster and more accurate.

Build with Google Colab

## 📁 Project Structure

Dog_Vision/
│
├── Dog_Vision.ipynb           # Main Jupyter notebook (Google Colab linkable)
├── README.md                  # Project documentation (this file)
├── requirements.txt           # List of dependencies (optional, for local runs)
│
├── dataset/                   # Folder containing training and testing images
│   ├── train/
│   │   ├── labrador/
│   │   ├── german_shepherd/
│   │   └── ... 
│   └── test/
│       ├── beagle/
│       └── ...
│
├── models/                    # Folder for saving trained models (e.g., .h5)
│   └── best_model.h5
│
├── outputs/                   # For storing result plots, logs, etc.
│   ├── accuracy_loss_plot.png
│   └── sample_predictions.png
│
└── utils/                     # Optional: for helper scripts (data loading, augmentation, etc.)
    └── preprocessing.py


## 🚀 Run this Project

Click below to open and run the notebook directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ayush546230/Amazon/blob/main/Dog_Vision.ipynb)

---

## 🧠 Model Overview

- ✅ **Model Type:** Image Classification
- 🔁 **Transfer Learning:** Yes (Pretrained model from TensorFlow Hub)
- 📚 **Framework:** TensorFlow / Keras
- 🎯 **Accuracy Achieved:** 93%)

---

## 📦 Features

- Image preprocessing and data augmentation  
- Transfer learning using MobileNetV2 / EfficientNet  
- Training with early stopping and model checkpoint  
- Evaluation with accuracy, loss graphs, and predictions on new images

---

## 🐕 Sample Predictions

| Input Image | Predicted Breed |
|-------------|------------------|
| ![](sample_dog1.jpg) | Golden Retriever |
| ![](sample_dog2.jpg) | Beagle |

---

## 🛠️ Requirements

- Python 3.8+
- TensorFlow
- TensorFlow Hub
- NumPy, Matplotlib, Pandas

(If using Google Colab, all dependencies are pre-installed ✅)

---

## 📬 Contact

Made with ❤️ by **[Ayush Srivastava](https://github.com/Ayush546230)**  
📧 For any questions or feedback, feel free to raise an issue!

---



