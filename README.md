# 🐶 Dog Vision - Dog Breed Classification using Transfer Learning

**Dog Vision** is a deep learning project built using **Transfer Learning** to classify images of dogs into different breeds. The model leverages pretrained CNN architectures to achieve high accuracy with limited data and training time.

---

## 📌 Overview

- 🔍 Problem: Classify images of dogs into their respective breeds
- 🧠 Solution: Use Transfer Learning with a pretrained CNN model (like MobileNetV2)
- 📦 Framework: TensorFlow & Keras
- 🖼️ Input: Dog images (resized to 224x224)
- 🎯 Output: Predicted breed of the dog

---

## ▶️ Run This Project on Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayushsrivastava07/dog-vision/blob/main/Dog_vision.ipynb)

Click the badge above to open and run the notebook in Google Colab. Make sure to upload the `dataset/` folder when prompted.

---

## 🏗️ Model Architecture

- Base model: **MobileNetV2** (pretrained on ImageNet)
- Top layers: Custom classification head (Dense + Dropout + Softmax)
- Loss function: Categorical Crossentropy
- Optimizer: Adam
- Accuracy: ~92% (update with actual)

---

## 🗂️ Project Structure


