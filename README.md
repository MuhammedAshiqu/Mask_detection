# Mask Detection App

This is a simple web application built with Streamlit for detecting whether a person in an uploaded image is wearing a mask or not. It uses a pre-trained deep learning model for inference.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Upload an image containing a person.

3. The app will display the uploaded image and provide a prediction whether the person is wearing a mask or not.

## Dependencies

- Streamlit
- OpenCV (cv2)
- NumPy
- TensorFlow
- Keras

## Model

The app uses a pre-trained deep learning model for mask detection. You can find the model file at `path/to/your/model.h5`. If you want to use your own model, make sure it follows the same architecture and is saved in the HDF5 format.


##Output

![1](https://github.com/MuhammedAshiqu/Mask_detection/assets/69718823/30f1ba68-66ca-44e0-94fc-5f379940858b)


![2](https://github.com/MuhammedAshiqu/Mask_detection/assets/69718823/5a45c5e3-3325-46e6-92d1-dc9ac10ddfa4)


![3](https://github.com/MuhammedAshiqu/Mask_detection/assets/69718823/1f9360bd-eb42-4b67-9c68-a8b75121a072)
