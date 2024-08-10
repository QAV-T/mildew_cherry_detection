# Cherry Leaf Health Detection

## Project Summary

This project aims to develop a machine learning model to visually differentiate between healthy cherry leaves and those affected by powdery mildew. The model will predict the health status of cherry leaves using images and will be deployed in a user-friendly dashboard for real-time predictions.
To visit this application website live on Heroku, please click on this [link](https://mildew-cherry-detection-5028c12c85c3.herokuapp.com/).

## Index

1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
    1. [First Business Requirement](#first-business-requirement)
    2. [Second Business Requirement](#second-business-requirement)
3. [Hypotheses and Validation](#hypotheses-and-validation)
    1. [Distinctive Features of Infected Leaves](#distinctive-features-of-infected-leaves)
    2. [Efficiency in Detection](#efficiency-in-detection)
    3. [Reduction of Human Error](#reduction-of-human-error)
    4. [Early Detection and Prevention](#early-detection-and-prevention)
    5. [Business Impact](#business-impact)
4. [Mapping Business Requirements to Data Visualizations and ML Tasks](#mapping-business-requirements-to-data-visualizations-and-ml-tasks)
    1. [First Business Requirement](#mapping-first-business-requirement)
    2. [Second Business Requirement](#mapping-second-business-requirement)
5. [ML Business Case](#ml-business-case)
6. [Agile Process](#agile-process)
7. [Dashboard Design](#dashboard-design-streamlit-app-user-interface)
    1. [Project Summary Page](#project-summary-page)
    2. [Cherry Leaves Visualizer Page](#cherry-leaves-visualizer-page)
    3. [Powdery Mildew Detection Page](#powdery-mildew-detection-page)
    4. [Project Hypothesis Page](#project-hypothesis-page)
    5. [ML Performance Metrics Page](#ml-performance-metrics-page)
8.  
    1. [Fixed Bugs](#fixed-bugs)
    2. [Unfixed Bugs](#unfixed-bugs)
9. [Deployment](#deployment)
    1. [GitHub](#github)
    2. [Heroku](#heroku)
10. [Technologies Used](#main-technologies-used)
    1. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
    2. [Machine Learning Frameworks and Libraries](#machine-learning-frameworks-and-libraries)
    3. [Development and Hosting](#development-and-hosting)
11. [Credits](#credits)

## Dataset Content

- The dataset is obtained from Code Institute's account on Kaggle.
- The dataset comprises over 4,000 images of cherry leaves, split evenly between healthy leaves and those affected by powdery mildew.
- The images are sourced from Farmy & Foods' crops

## Business Requirements

### First Business Requirement

Farmy & Foods faces a challenge with powdery mildew affecting their cherry plantations.
The current manual verification process is time-consuming and not feasible for large-scale operations.
The IT team proposes a machine learning (ML) solution to instantly detect powdery mildew using images of cherry leaves.

### Second Business Requirement

The client seeks to:

- Conduct a study to visually differentiate healthy cherry leaves from those infected with powdery mildew.
- Predict if a cherry leaf is healthy or contains powdery mildew.

The client requires a dashboard for:

- Visually differentiating healthy and mildew-infected cherry leaves.
- Predicting the health status of cherry leaves.

## Hypotheses and Validation

### Distinctive Features of Infected Leaves

 We hypothesize that cherry leaves infected with powdery mildew exhibit unique visual characteristics that differentiate them from healthy leaves. These characteristics, including specific coloration patterns and textures, can be captured and analyzed by a CNN-based model, allowing it to effectively distinguish between healthy and infected leaves.

### Efficiency in Detection

   The machine learning program is expected to significantly accelerate the cherry leaf examination process. By automating the detection of powdery mildew, the model can save substantial amounts of time, effort, and money compared to manual inspection. With an anticipated accuracy of about 99%, the model could reduce the time and resources required for inspections by at least 90%.

### Reduction of Human Error

   Manual inspections of cherry leaves are prone to human errors, such as overlooking early signs of infection. The model is designed to minimize these errors by consistently applying the same detection criteria, leading to more reliable and accurate results. This could be particularly valuable in large-scale operations where the volume of leaves to be inspected is high.

### Early Detection and Prevention

   Detecting powdery mildew at an early stage is crucial for preventing the spread of the disease to a large number of trees. The model is hypothesized to be more effective than human inspectors at identifying the early signs of infection, thus enabling timely intervention. This early detection could lead to more effective treatment and management strategies, ultimately protecting crop yields and quality.

### Business Impact

   By integrating this machine learning program into their operations, agricultural businesses can improve their crop management practices. The ability to quickly and accurately identify infected leaves allows for faster response times, reducing the risk of widespread infection and potentially leading to significant cost savings.

## Mapping Business Requirements to Data Visualizations and ML Tasks

### Mapping First Business Requirement

- As a user, I want to display the mean and standard deviation of images of healthy cherry leaves and of cherry leaves that contain powdery mildew so that I can optically distinguish between them.
- As a user, I want to display the difference between an average infected cherry leaf image and an average healthy cherry leaf image.
- As a user, I want to display an image montage for images of cherry leaves that are healthy and also of cherry leaves that contain powdery mildew.

### Mapping Second Business Requirement

- As a user, I want to predict if a cherry leaf is healthy or contains powdery mildew.
- As a user, I want to upload cherry leaves images into the machine learning predicting program.
- As a user, I want to download the analysis report of each prediction.

## ML Business Case

### Current Situation

Farmy and Foods currently relies on manual inspection by trained employees to distinguish between healthy and mildew-infected cherry leaves. This manual process is prone to errors and is both time-consuming and labor-intensive.

### Project Objective

The goal of this project is to develop a machine learning model that can accurately and efficiently classify cherry leaves as either "healthy" or "mildew-infected." By automating this process, the model will save the business significant time, effort, and resources.

### Model Overview

This machine learning model is a supervised binary classification system trained on images of both healthy and infected cherry leaves. It learns to differentiate between the two by identifying patterns in the images. The model applies a binary classification method to provide a prediction of either "healthy" or "mildew."

### User Requirements

The customer requires a user-friendly dashboard where they can upload both existing and new cherry leaf images for analysis. The model is expected to achieve a prediction accuracy of at least 97%.

### Future Scope

While the current focus is on cherry leaves, the model's application could be extended to detect diseases in other crops.

## Agile Process

This project was designed and developed following the Agile methodology. The tasks were organized and broken down into smaller, manageable user stories to ensure a smooth and iterative development process. From the initial planning stages to the final deployment, the project followed a structured approach that allowed for flexibility and adaptability at each phase.

To help visualize the workflow and progress, a [GitHub project](https://github.com/users/QAV-T/projects/3/views/1) was created, utilizing the Kanban board method. This approach enabled efficient tracking of tasks, ensuring that each project element was clearly defined, prioritized, and completed in an organized manner.

![Kanban Board](/readme_imgs/Kanban-board.png)  

## Dashboard Design (Streamlit App User Interface)

### Features

The dashboard is a multi-page Streamlit application with a sidebar for navigation. It includes the following pages:

### Project Summary Page

Overview of the project, which provides an overview of the project's objectives, dataset, key phases, and future improvements.
![screen-shot-from-the-summary-page](/readme_imgs/summary.png)

### Cherry Leaves Visualizer Page

- Show findings related to visually differentiating healthy and mildew-infected leaves.
- A user can also identify the average images of healthy and infected cherry leaves and consider the differences between them.
- A user can do an image montage of healthy and infected cherry leaves images.
![sample-images](/readme_imgs/sample-images.png)
![difference-avr-variability](/readme_imgs/diff-avr.png)
![difference-avr-variabilty-mildew-healthy](/readme_imgs/diff-avr-2.png)
![montage-of-mildew-leaves](/readme_imgs/montage-mildew.png)
![montage-of-healthy-leaves](/readme_imgs/montage-healthy.png)

### Powdery Mildew Detection Page

- Provide a link to download a set of cherry leaf images for live prediction.
- User Interface with a file uploader widget.
- Display the image and a prediction statement.
- A table with image names and prediction results, and a download button.
![screen-shot-detactor-page](/readme_imgs/prediction-result-1.png)
![screen-shot-detactor-page-analays](/readme_imgs/prediction-result-2.png)
![screen-shot-detactor-page-results](/readme_imgs/prediction-result-3.png)
![screen-shot-detactor-page-report](/readme_imgs/prediction-report.png)

### Project Hypothesis Page

Display project hypothesis and validation methods.
![hypothesis-page](/readme_imgs/hypothesis.png)

### ML Performance Metrics Page

Technical details and performance metrics, the page provides a visual representation of the model's performance.

- Explore the different visualizations to understand the model's training history and evaluation metrics.
- The evaluation metrics include the confusion matrix and classification report, which provide insights into the model's performance on the test data."
![data-ditribution](/readme_imgs/ml-performance.png)
![training-history](/readme_imgs/training-history.png)
![sample-cherry-image-processed](/readme_imgs/sample-cherry-image-processed.png)
![confusin-matrix](/readme_imgs/confusin_matrix.png)
![image]

## Fixed bugs

### Model Not Found Error After Deployment

**Description**: After successfully deploying the application, all pages were functioning except for the "Make Prediction" feature. When users attempted to make a prediction, an error occurred, stating that the model could not be found in the specified directory.

**Cause**: Despite verifying that the model path was correct, the issue persisted. The root cause was traced back to one of the packages listed in the requirements.txt file. This package conflicted with TensorFlow's load_model function, preventing the model from being loaded correctly.

**Solution**: The issue was resolved by reverting the requirements.txt file to the basic template version. This change removed the conflicting package, allowing TensorFlow's load_model function to operate as expected, and the "Make Prediction" feature worked correctly after deployment.

## Unfixed Bugs

This project does not include unfixed bugs.

## Deployment

### GitHub

- To kickstart the project, I forked the Code Institute's GitHub template repository titled "milestone-project-mildew-detection-in-cherry-leaves" into my own GitHub account.
- Utilizing this forked repository, I set up a Gitpod workspace to develop and manage the project efficiently.

You can visit the project's GitHub repository by clicking on this [link](https://github.com/QAV-T/mildew_cherry_detection).

### Heroku

- Log into your Heroku account and go to 'Account Settings' in the menu under your avatar.
- Scroll down to the 'API Key' and click 'Reveal'.
- Copy that API key.
- In a Gitpod terminal, run the command 'heroku_config'.
- You will be asked to paste in your API key in that Gitpod terminal.
- You can now use the Heroku CLI program. To confirm that it is working, try running the command 'heroku apps' in your Gitpod terminal.
- This Heroku API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one by clicking on 'Regenerate API Key...', which is under your API key.
- Create an new app on your Heroku account for your project.
- If a Heroku error appears telling you that the Python version is not available, it may be due to the Heroku's stack used for the application.
- To fix this, from your Gitpod terminal, log in to the Heroku command line interface, CLI, and type in the command 'heroku stack:set heroku-20 -a your-app-name' to set the stack to Heroku-20.
- Go to your Heroku app, click on 'Deploy' on the navigation bar.
- On the 'Deploy' page, scroll down until you find the 'Deployment method' on the left.
- Select GitHub as the deployment method.
- Type in your repository name and click on 'Search'. Once it is found, click on 'Connect'.
- Choose 'main' as the branch to deploy, then click on 'Deploy Branch'.
- Once your app is deployed, click on 'Open app' on the top right of your Heroku app page.

## Main Technologies Used

### Main Data Analysis and Machine Learning Libraries

- **NumPy**:
  - A fundamental library for scientific computing in Python, providing support for arrays, matrices, and many mathematical functions to operate on these data structures.
  - Version: 1.19.2
  
- **Pandas**:
  - A powerful data manipulation and analysis library that provides data structures like Series and DataFrames, which are essential for handling and analyzing structured data.
  - Version: 1.1.2
  
- **Matplotlib**:
  - A comprehensive library for creating static, animated, and interactive visualizations in Python. It is particularly useful for creating line plots, scatter plots, histograms, and bar charts.
  - Version: 3.3.1
  
- **Seaborn**:
  - Built on top of Matplotlib, Seaborn is used for making statistical graphics that are both informative and attractive. It simplifies the creation of complex plots such as heatmaps, violin plots, and more.
  - Version: 0.11.0
  
- **Plotly**:
  - An interactive graphing library that supports a wide range of chart types and provides interactive features such as zooming, hovering, and panning.
  - Version: 4.12.0

### Machine Learning Frameworks and Libraries

- **Scikit-learn**:
  - A robust machine learning library that offers simple and efficient tools for data mining and data analysis. It is built on NumPy, SciPy, and Matplotlib, and it includes a variety of algorithms for classification, regression, clustering, and dimensionality reduction.
  - Version: 0.24.2

- **TensorFlow**:
  - An open-source machine learning framework developed by Google, widely used for building and training deep learning models, particularly neural networks.
  - Version: TensorFlow CPU 2.6.0
  
- **Keras**:
  - A high-level neural networks API, written in Python, capable of running on top of TensorFlow, and used for building and training deep learning models with ease.
  - Version: 2.6.0
  
- **Altair**:
  - A declarative statistical visualization library for Python, based on Vega and Vega-Lite, that allows the creation of complex visualizations with a minimal amount of code.
  - Version: <5  

### Development and Hosting

- **Jupyte**
  - A web-based interactive computational environment that allows you to combine code, text, and images in a single document.

- **Streamlit**:
  - A rapid prototyping web framework that allows the creation of custom web apps for machine learning and data science projects. Streamlit apps are Python scripts that automatically create an interactive UI.
  - Version: 0.85.0

- **Kaggle**
  - It provides a vast repository of datasets, a supportive community, and a series of competitions that foster learning and innovation in the data science realm.

- **Heroku**
  - A cloud Platform as a Service, PaaS, that allows developers to deploy, manage, and scale their applications without having to worry about infrastructure.

### Additional Libraries

- **Protobuf**:
  - A language-neutral, platform-neutral extensible mechanism for serializing structured data. It is used for communication between applications.
  - Version: 3.20

## Credits

- [**Code Institute**](codeinstitute.net/) Learning Materials
- [**Malaria Predictor project**](https://malaria-predictor.onrender.com) A walkthrough Project.
- **Github Repository**
  - [*Malaria Predictor Github Repo*](https://github.com/QAV-T/Malaria-Detector)
  - A template [Repository](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) provided from *Code Institute*.
