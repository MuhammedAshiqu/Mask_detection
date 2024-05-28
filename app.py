import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model


MODEL_PATH = 'path/to/your/model.h5' 
model = load_model(r'mask_model.h5')

# Define prediction function
def prediction(image):
    input_image_resized = cv2.resize(image, (128, 128))
    input_image_scaled = input_image_resized / 255.0
    input_image_reshaped = np.reshape(input_image_scaled, (1, 128, 128, 3))
    input_prediction = model.predict(input_image_reshaped)
    input_pred_label = np.argmax(input_prediction)
    if input_pred_label == 1:
        return 'Wearing Mask'
    else:
        return 'Not Wearing Mask'


def main():
    st.title("Mask Detection App")

    # Define a layout with two columns
    col1, col2 = st.columns([2,2])

    # Left column for file uploader
    with col1:
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])

    # Right column for displaying uploaded image and prediction
    with col2:
        if uploaded_image is not None:
            # Read the uploaded image
            input_image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)

            # Display the image
            st.image(input_image, channels="BGR", caption="Uploaded Image", width=300, use_column_width=False)

            # Make prediction
            result = prediction(input_image)
            st.write(f'Prediction: {result}')
        else:
            st.write("Please upload an image.")

if __name__ == "__main__":
    main()