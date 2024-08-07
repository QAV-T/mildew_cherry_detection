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
    
    
    if st.checkbox("Sample Cherry Leaf Image"):
       fig, ax = plt.subplots()
       ax.imshow(np.random.rand(150, 150, 3))
       st.pyplot(fig)
       
    if st.checkbox("Data Distribution"):
        st.image("models/labels_distribution.png", caption='Data Distribution')   