# Cherry Leaf Health Detection

## Project Summary

This project aims to develop a machine learning model to visually differentiate between healthy cherry leaves and those affected by powdery mildew. The model will predict the health status of cherry leaves using images and will be deployed in a user-friendly dashboard for real-time predictions.

## Planning Phase

### Business Requirements

Farmy & Foods faces a challenge with powdery mildew affecting their cherry plantations. The current manual verification process is time-consuming and not feasible for large-scale operations. The IT team proposes a machine learning (ML) solution to instantly detect powdery mildew using images of cherry leaves.

**Project Goals:**
1. Conduct a study to visually differentiate a healthy cherry leaf from one affected by powdery mildew.
2. Predict whether a cherry leaf is healthy or affected by powdery mildew.

**Client Requirements:**
- A research study to visually differentiate healthy and powdery mildew-affected cherry leaves.
- A machine learning model to predict the health status of cherry leaves.
- A dashboard to display results and allow for real-time predictions.

### Dataset Content

The dataset comprises over 4,000 images of cherry leaves, split evenly between healthy leaves and those affected by powdery mildew. The images are sourced from Farmy & Foods' crops.

**Sample leaves:**

![Healthy Leaf](path_to_healthy_leaf_image)
![Mildew Leaf](path_to_mildew_leaf_image)

### Project Hypothesis

Cherry leaves affected by powdery mildew exhibit visible white streaks. Traditional data analysis and machine learning techniques will be employed to differentiate and predict the health status of the leaves.

## Data Understanding

The dataset consists of labeled images organized into two folders: "healthy" and "powder_mildew." Each folder contains 2,104 images, ensuring a balanced dataset.

### Data Preparation

Minimal data cleaning was required. The dataset was split into training (70%), validation (10%), and test (20%) sets. Data augmentation techniques were applied to the training set to improve model generalization.

## Modeling

A convolutional neural network (CNN) was trained on the dataset. The model was validated using the validation set and tested on the test set. Data augmentation techniques were employed to enhance the model's performance.

### Evaluation

The model achieved an accuracy of over 97% on the test dataset. It was also tested with new images to ensure reliability.

## Dashboard Design (Streamlit App User Interface)

### Features

The dashboard is a multi-page Streamlit application with a sidebar for navigation. It includes the following pages:

1. **Quick Project Summary:** Overview of the project and dataset.
2. **Cherry Leaf Visualizer:** Visual differentiation study results.
3. **Mildew Detector:** Interface for uploading images and getting predictions.
4. **Project Hypothesis and Validation:** Explanation of hypotheses and validation methods.
5. **ML Performance Metrics:** Technical details and performance metrics.

### Page Details

**Page 1: Quick Project Summary**
- Summary of project requirements and dataset.

**Page 2: Cherry Leaf Visualizer**
- Checkbox options to display various analyses and image montages.

**Page 3: Mildew Detector**
- File upload widget for predictions.
- Display of uploaded images, prediction statements, and results table.

**Page 4: Hypothesis and Validation**
- Detailed explanation of project hypotheses and validation methods.

**Page 5: ML Performance Metrics**
- Performance metrics and technical details.

## Deployment

### Workspace Setup
- Repository created using GitHub template.
- GitPod used for development.

### Cloning the Repository
- Instructions to clone the repository using Git.

### Creating Heroku App
- Steps to create and set up the Heroku app.

### Deploying to Heroku
- Steps to deploy the app to Heroku.

## Technologies Used

### Main Data Analysis and Machine Learning Libraries
- TensorFlow
- Keras
- Joblib
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Scikit-learn
- Jupyter Notebook

### Other Frameworks, Libraries & Programs
- Git
- GitHub
- Heroku
- GitPod

## Conclusion

This project successfully developed a machine learning model to differentiate and predict the health status of cherry leaves, achieving over 97% accuracy. The Streamlit dashboard allows for real-time predictions, providing a valuable tool for Farmy & Foods to efficiently manage their cherry plantations.

### Bugs and Fixes



### Ethical or Privacy Concerns

Data provided under an NDA should only be shared with officially involved professionals.

## Future Work

Potential extensions of this project could include:
- Enhancing the model to detect other types of plant diseases.
- Integrating the solution with IoT devices for real-time monitoring.
- Expanding the dataset to improve model robustness.

