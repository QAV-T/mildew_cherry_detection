import streamlit as st

def page_project_hypothesis_fn():
    st.header("Project Hypothesis")
    st.write("""
    ## Hypothesis
    The hypothesis of this project is to develop a machine learning model that can accurately classify
    cherry leaf images as either healthy or infected with mildew. By leveraging convolutional neural networks (CNNs),
    we aim to achieve high accuracy in detecting the presence of mildew on cherry leaves, which can help in early detection
    and treatment to improve crop yield and quality.
    """)
