import streamlit as st

def page_project_hypothesis_fn():
    st.header("Project Hypothesis")
    
    st.write("""
    The primary hypothesis of this project is that a machine learning model, specifically a Convolutional Neural Network (CNN), 
    can be trained to accurately classify cherry leaf images as either healthy or infected with powdery mildew. By leveraging 
    advanced image recognition techniques, the model will be able to detect subtle visual cues indicative of mildew infection, 
    such as white, milky, or light gray spots, that may not be easily distinguishable by the human eye, especially in the early stages of infection.
    """)

    st.write("""
    ## Hypothesis
    1. **Distinctive Features of Infected Leaves**: We hypothesize that cherry leaves infected with powdery mildew exhibit unique 
    visual characteristics that differentiate them from healthy leaves. These characteristics, including specific coloration 
    patterns and textures, can be captured and analyzed by a CNN-based model, allowing it to effectively distinguish between 
    healthy and infected leaves.

    2. **Efficiency in Detection**: The machine learning program is expected to significantly accelerate the cherry leaf examination process. 
    By automating the detection of powdery mildew, the model can save substantial amounts of time, effort, and money compared to manual inspection. 
    With an anticipated accuracy of about 99%, the model could reduce the time and resources required for inspections by at least 90%.

    3. **Reduction of Human Error**: Manual inspections of cherry leaves are prone to human errors, such as overlooking early signs of infection. 
    The model is designed to minimize these errors by consistently applying the same detection criteria, leading to more reliable and accurate results. 
    This could be particularly valuable in large-scale operations where the volume of leaves to be inspected is high.

    4. **Early Detection and Prevention**: Detecting powdery mildew at an early stage is crucial for preventing the spread of the disease 
    to a large number of trees. The model is hypothesized to be more effective than human inspectors at identifying the early signs of infection, 
    thus enabling timely intervention. This early detection could lead to more effective treatment and management strategies, ultimately protecting 
    crop yields and quality.

    5. **Business Impact**: By integrating this machine learning program into their operations, agricultural businesses can improve their 
    crop management practices. The ability to quickly and accurately identify infected leaves allows for faster response times, reducing the 
    risk of widespread infection and potentially leading to significant cost savings.
    """)

    # st.success("""
    # The overarching goal of this project is to develop a reliable, efficient, and scalable solution that supports farmers and agricultural 
    # businesses in maintaining healthy crops and optimizing their production processes. The success of this machine learning model would represent 
    # a significant advancement in the application of AI in agriculture, demonstrating the potential of technology to enhance traditional farming practices.
    # """)
