import streamlit as st

def page_project_summary_fn():
    st.header("Project Summary")
    
    st.write("### General Information")
    st.info(
        f"Powdery mildew is a widespread fungal disease that significantly impacts various crops, including cherry trees. "
        f"Manual detection of this disease is impractical due to the vast number of trees in a typical cherry orchard, "
        f"making an automated solution highly desirable.\n\n"
        f"This project aims to address this challenge by developing a machine learning model capable of analyzing cherry leaf images "
        f"to determine if they are healthy or infected with powdery mildew. By leveraging deep learning techniques, "
        f"we aim to create an efficient and scalable solution that can support early detection and disease management in agriculture."
    )
    
    st.write("### Project Dataset")
    st.info(
        f"The dataset used in this project consists of images of cherry leaves provided by **Farmy & Foods**. "
        f"These images were meticulously collected and labeled to ensure the accuracy and reliability of the model during training."
    )

    st.write("### Key Project Phases")
    st.success(
        f"The project was carried out through several key phases:\n\n"
        f"1. **Data Collection and Preprocessing**: Gathering and preparing a comprehensive dataset of cherry leaf images.\n\n"
        f"2. **Data Augmentation**: Applying various techniques to artificially expand the dataset and improve model robustness.\n\n"
        f"3. **Model Architecture Design**: Designing a convolutional neural network (CNN) tailored to the specific needs of this classification task.\n\n"
        f"4. **Model Training and Evaluation**: Training the model to achieve high accuracy, with an eventual test accuracy of 98%.\n\n"
        f"5. **Web Application Deployment**: Implementing the trained model into a user-friendly web application using Streamlit."
    )
    
    st.write("### Future Improvements")
    st.info(
        f"Future enhancements could involve training the model on larger and more diverse datasets, exploring advanced neural network architectures, "
        f"and integrating real-time image analysis capabilities to further increase the model's practical utility in agricultural settings."
    )
    
    st.write(
        f"For more detailed information about this project, please visit "
        f"[Project Repository](https://github.com/QAV-T/mildew_cherry_detection)."
    )
