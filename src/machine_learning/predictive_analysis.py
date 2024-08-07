import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pickle_file


def resize_input_image(img):
    """
    Resize image to average image size
    """
    image_shape = load_pickle_file(
        file_name=f"models/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    return np.expand_dims(img_resized, axis=0)/255


def make_prediction(my_image):
    """
    Load and perform ML prediction over images provided
    """

    model = load_model(f'models/cherry_leaf_model.h5')
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


def plot_prediction_probabilities(prediction_prob, prediction_class):
    '''
    plot prediction probability result
    '''
    probability_per_class = pd.DataFrame(
        data=[0, 0],
        index={'healthy': 0, 'mildew': 1}.keys(),
        columns=['Probability']
    )
    probability_per_class.loc[prediction_class] = prediction_prob
    for x in probability_per_class.index.to_list():
        if x not in prediction_class:
            probability_per_class.loc[x] = 1 - prediction_prob
    probability_per_class = probability_per_class.round(3)
    probability_per_class['Diagnostic'] = probability_per_class.index

    fig = px.bar(
        probability_per_class,
        x='Diagnostic',
        y=probability_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)