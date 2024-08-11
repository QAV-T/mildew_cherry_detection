import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pickle_file
import os


def plot_prediction_probabilities(prediction_prob, prediction_class):
    """
    Plot prediction probability result
    """
    probability_per_class = pd.DataFrame(
        data=[0, 0],
        index={'healthy': 0, 'mildew': 1}.keys(),
        columns=['Probability']
    )
    probability_per_class.loc[prediction_class] = prediction_prob
    for label in probability_per_class.index.to_list():
        if label != prediction_class:
            probability_per_class.loc[label] = 1 - prediction_prob

    probability_per_class = probability_per_class.round(3)
    probability_per_class['Diagnostic'] = probability_per_class.index

    fig = px.bar(
        probability_per_class,
        x='Diagnostic',
        y='Probability',
        range_y=[0, 1],
        width=600, height=300, template='seaborn'
    )
    st.plotly_chart(fig)


def resize_input_image(img, target_shape):
    """
    Resize image to the target shape expected by the model.

    Parameters:
    img (PIL.Image.Image): The input image to be resized.
    target_shape (tuple): The target shape (height, width) to resize the image to.

    Returns:
    np.ndarray: The resized image as a numpy array, normalized and expanded to include a batch dimension.
    """
    # Resize the image to the target shape
    img_resized = img.resize(target_shape, Image.Resampling.LANCZOS)

    # Convert the resized image to a numpy array
    img_array = np.array(img_resized)

    # Normalize the image array to be in the range [0, 1]
    img_array = img_array / 255.0

    # Expand dimensions to add batch size (1, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def make_prediction(my_image, version='v1'):
    """
    Load and perform ML prediction over images provided
    """
    file_path = os.path.join('models')
    print("Files in models directory:", os.listdir("models/"))
    print("Current working directory:", os.getcwd())
    model = load_model('models/cherry_leaf_model.h5')

    # Verify the input shape
    print(f"Model input shape: {model.input_shape}")
    print(f"Image shape: {my_image.shape}")

    prediction_probability = model.predict(my_image)[0, 0]
    predictions_labels = {'healthy': 0, 'mildew': 1}
    target_map = {v: k for k, v in predictions_labels.items()}
    predicted_class = target_map[prediction_probability > 0.5]

    if predicted_class == target_map[0]:
        prediction_probability = 1 - prediction_probability

    statement = "The predictive analysis indicates the cherry leaf"
    if predicted_class.lower() == 'healthy':
        statement = f"{statement} is **{predicted_class.lower()}**"
    else:
        statement = f"{statement} has **powdery mildew**."

    st.write(statement)
    return prediction_probability, predicted_class
