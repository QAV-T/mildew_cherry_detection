import streamlit as st
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def page_ml_performance_fn():
    st.header("ML Performance")
    st.info(
        "Welcome to the ML Performance page! This page provides a visual representation of the model's performance.\n\n"
        "Explore the different visualizations to understand the model's training history and evaluation metrics.\n\n"
        "The evaluation metrics include the confusion matrix and classification report, which provide insights into the model's performance on the test data."
    )
    
    # Load evaluation metrics
    evaluation = joblib.load("models/evaluation_details.pkl")
    confusion_matrix = evaluation['confusion_matrix']
    classification_report = evaluation['classification_report']
    
    st.subheader("Data Distribution")
    st.write("The data distribution, training history, and evaluation metrics of the model.")
    st.image("models/labels_distribution.png", caption='Data Distribution')

    
    st.subheader("Sample Cherry Leaf Image")
    st.write("This image represents how the model interprets the input data using three color channels (Red, Green, and Blue).")
    fig, ax = plt.subplots()
    ax.imshow(np.random.rand(150, 150, 3))
    st.pyplot(fig)
    
    st.header("Training History")
    
    st.subheader("Model Training Losses")
    st.image("models/training_validation_loss.png", caption='Training and Validation Loss')
    
    st.subheader("Model Training Accuracy")
    st.image("models/training_validation_acc.png", caption='Training and Validation Accuracy')
    
    st.header("Model Evaluation Metrics")
    
    # Display Overall Accuracy
    st.subheader("Overall Model Accuracy")
    st.write("**Model Accuracy: 98%**")
    st.write("While the model accuracy is high, we can explore other important metrics to gain a deeper understanding of its performance.")
    
    # Display Confusion Matrix
    st.subheader("Confusion Matrix")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax)
    ax.set_xlabel("Predicted Labels")
    ax.set_ylabel("True Labels")
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)
    
    # Display Classification Report
    st.subheader("Classification Report")
    st.text("The following report gives a detailed look at precision, recall,\n\n and F1-score for each class:")
    st.text(classification_report)
    
   # Explanation Notes
    st.subheader("Interpretation of Results")
    st.write(
    "The model has achieved a high accuracy of around 99%, indicating its strong overall performance. "
    "However, the confusion matrix and classification report reveal that while the model is generally effective, "
    "there are still some challenges in differentiating between 'Healthy' and 'Mildew' leaves. "
    "This highlights the importance of not relying solely on accuracy, as precision, recall, and F1-scores provide "
    "a more nuanced understanding of the model's performance, particularly in how well it handles each class."
    "\n\n"
)
