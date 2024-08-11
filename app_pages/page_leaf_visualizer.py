import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import itertools
import random
from tensorflow.keras.preprocessing import image
from matplotlib.image import imread
import os


def page_leaf_visualizer_fn():
    st.header("Cherry Leaf Visualizer")
    st.info(
        f"Welcome to the Cherry Leaf Visualizer page! This page provides a visual representation of the cherry leaf dataset.\n\n"
        f"The aim here is to visually differentiate a **healthy** cherry leaf from one that is **affected by powdery mildew**.\n\n"
        f"Explore the different visualizations to understand the differences between healthy and diseased leaves.\n\n"

    )

    # Placeholder visualization
    if st.checkbox("Samples Cherry Leaf Image"):
        col1, col2 = st.beta_columns(2)
        with col1:
         st.image("models/sample_healthy_leaf.png", caption='Sample Cherry healthy Leaf Image')
        with col2:
         st.image("models/sample_mildew_leaf.png", caption='Sample Cherry mildew Leaf Image')

    if st.checkbox("Difference between average and variability image"):
        st.subheader("Healthy Leaf")
        st.image("models/avg_var_healthy.png", caption='Healthy Leaf-Average and Variability')
        st.subheader("Mildew Leaf")
        st.image("models/avg_var_mildew.png", caption='Mildew Leaf-Average and Variability')

        st.warning(
            f"There is a noticeable difference in the color pigmentation between healthy and diseased leaves.\n\n"
            f"* Healthy leaves maintain a uniform green color, whereas leaves with powdery mildew show a distinct variation in hue.\n\n"
            f"* Additionally, the veins on the mildew-affected leaves are more prominent and distinct compared to those on healthy leaves."
        )

    if st.checkbox('Differences between Healthy and Powdery Mildew cherry leaves'):
        st.image("models/avg_diff.png", caption='Differences between Healthy and Powdery Mildew cherry leaves')

        st.warning(
            f"* The first pair of images shows the mean value, as explained in the second checkbox. "
            f"Regarding the difference in variability, the darker areas indicate regions where the two images "
            f"are similar, while the lighter areas highlight regions with differing variability."
        )

    if st.checkbox("Image Montage"):
        st.write("* Choose a label from the dropdown menu to create a montage of images.")
        my_data_dir = 'inputs/datasets'
        labels = os.listdir(my_data_dir + '/val')
        label_to_display = st.selectbox("Select Label", options=labels, index=0)
        if st.button("Create Montage"):
          image_montage(dir_path = my_data_dir + '/val',
                      label_to_display = label_to_display,
                      nrows=8, ncols=3, figsize=(10,25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10), size=(100, 100)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # Selects the specific category of images to be displayed
    if label_to_display in labels:

        # Ensures the montage grid size does not exceed the available images
        images_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(f"Decrease nrows or ncols to create your montage. \n"
                  f"There are {len(images_list)} in your subset. "
                  f"You requested a montage with {nrows * ncols} spaces")
            return

        # Create a figure layout and display the selected images
        plot_idx = list(itertools.product(range(nrows), range(ncols)))
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for idx, (row, col) in enumerate(plot_idx):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[idx])
            img_shape = img.shape
            axes[row, col].imshow(img)
            axes[row, col].set_title(f"{img_shape[1]}px x {img_shape[0]}px")
            axes[row, col].set_xticks([])
            axes[row, col].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        plt.show()
    else:
        print(f"The label you selected doesn't exist. Existing options are: {labels}")
