import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Set page config
st.set_page_config(page_title="Dog Vision 🐶", layout="centered")

# Load your model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('dog_vision_model.h5')  # change filename if needed
    return model

model = load_model()

# Class names (example, update with actual class names)
class_names = ['Beagle', 'Chihuahua', 'Doberman', 'French Bulldog', 'Golden Retriever', 
               'Maltese', 'Pug', 'Rottweiler', 'Shih-Tzu', 'Siberian Husky']

# Title
st.title("🐶 Dog Vision - Identify Dog Breed")
st.markdown("Upload an image of a dog, and let the model predict its breed using deep learning!")

# Upload image
uploaded_file = st.file_uploader("Choose a dog image...", type=["jpg", "jpeg", "png"])

# Image display and prediction
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    st.write("Classifying...")

    # Preprocess image
    img = image.resize((224, 224))  # Ensure size matches your model's input
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    # Display result
    st.success(f"Predicted Breed: **{predicted_class}**")
