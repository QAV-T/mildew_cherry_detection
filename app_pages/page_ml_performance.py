import streamlit as st
import joblib
import matplotlib.pyplot as plt

def page_ml_performance_fn():
    st.header("ML Performance")
    
    # Load evaluation metrics
    evaluation = joblib.load("models/evaluation.pkl")
    
    st.subheader("Test Evaluation Metrics")
    st.write(f'Test Loss: {evaluation[0]}')
    st.write(f'Test Accuracy: {evaluation[1] * 100:.2f}%')
    
    st.subheader("Model Training Losses")
    st.image("models/model_training_losses.png", caption='Training and Validation Loss')
    
    st.subheader("Model Training Accuracy")
    st.image("models/model_training_acc.png", caption='Training and Validation Accuracy')
