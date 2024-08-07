import streamlit as st
import joblib
import matplotlib.pyplot as plt
import numpy as np
import os

def page_ml_performance_fn():

    st.header("ML Performance")
    st.info(
        f"Welcome to the ML Performance page! This page provides a visual representation of the model's performance.\n\n"
        f"Explore the different visualizations to understand the model's training history and evaluation metrics.\n\n"
    )
    
    # # Load evaluation metrics
    # evaluation = joblib.load("models/evaluation.pkl")
    
    st.subheader("Data Distribution")
    st.image("models/labels_distribution.png", caption='Data Distribution')
    
    st.subheader("Sample Cherry Leaf Image")
    fig, ax = plt.subplots()
    ax.imshow(np.random.rand(150, 150, 3))
    st.pyplot(fig)
    
    st.header("Training History")
    
    st.subheader("Model Training Losses")
    st.image("models/training_validation_loss.png", caption='Training and Validation Loss')
    
    st.subheader("Model Training Accuracy")
    st.image("models/training_validation_acc.png", caption='Training and Validation Accuracy')
    
    

       
      
    
    # st.subheader("Test Evaluation Metrics")
    # evaluation = joblib.load("models/evaluation.pkl")  # Define the evaluation variable
    # st.write(f'Test Loss: {evaluation[0]:.4f}')
    # st.write(f'Test Accuracy: {evaluation[1] * 100:.2f}%')
    

