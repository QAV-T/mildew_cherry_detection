import streamlit as st

def page_project_summary_fn():
    st.header("Project Summary")
    st.write("""
    ## Project Summary
    This project involves building a convolutional neural network (CNN) to classify cherry leaves as healthy or infected with mildew.
    The main steps included:
    
    - Data Collection and Preprocessing
    - Data Augmentation
    - Model Architecture Design
    - Model Training and Evaluation
    - Deployment of a Web Application using Streamlit
    
    The model achieved a test accuracy of X% and demonstrates the potential of deep learning in agricultural applications.
    Future improvements can include training with larger datasets and implementing more advanced architectures.
    """)
