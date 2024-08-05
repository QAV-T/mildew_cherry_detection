import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns
import itertools
import random


def page_leaf_visualizer_body():
    version = 'v1'
    output_dir = f"outputs/{version}"

    st.write('### Cherry Leaf Visualizer')
    st.info(
        f"The goal is to visually distinguish between a cherry leaf that is **healthy** "
        f"  and one that is affected by **powdery mildew**."
    )

    if st.checkbox("Difference between average and variability image"):
        avg_healthy = plt.imread(f"{output_dir}/avg_var_healthy.png")
        avg_mildew = plt.imread(f"{output_dir}/avg_var_powdery_mildew.png")

        st.warning(
            f"We noticed a variation in the color pigmentation between the two types of leaves.\n\n"
            f"* The healthy leaves exhibit a consistent and even green color, while the leaves affected by powdery mildew display a different hue.\n\n"
            f"* Furthermore, the veins on the powdery mildew leaves are more pronounced and noticeable compared to those on the healthy leaves."
        )

        st.image(avg_healthy, caption="Healthy Cherry Leaf - Average and Variability")
        st.image(
            avg_mildew, caption="Powdery Mildew Cherry Leaf - Average and Variability")
        st.write('---')

    if st.checkbox('Differences between Healthy and Powdery Mildew cherry leaves'):
        avg_diff = plt.imread(f"{output_dir}/avg_diff.png")

        st.warning(
            f"* The initial pair of images depict the mean value, as clarified in the second checkbox. "
            f" Regarding the variability disparity, the darker region indicates areas where the two images "
            f" share similarities, whereas the lighter region represents areas where differences in variability exist. "
        )

        st.image(avg_diff, caption='Difference between average images')
        st.write('---')

    if st.checkbox("Image Montage"):
        st.write(
            "- To view the montage, select a label and click on **Create Montage** button")
        st.write('- To refresh the image montage, click on **Create Montage** button')
        data_dir = 'inputs/datasets/cherry-leaves/validation/'
        labels = os.listdir(data_dir)
        label_to_display = st.selectbox(
            label="Select label",
            options=labels,
            index=0
        )
        if st.button("Create Montage"):
            st.warning(
                f"**Observation**\n\n"
                f"* The average dimension of the leaf images is 256px width by 256px height\n\n"
                f"* The mildew leaves have visible white streaks on them"
                f" which differentiates them from healthy leaves"
            )
            image_montage(data_dir, label_to_display,
                          nrows=3, ncols=3, figsize=(10, 12))
            st.write('---')


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        images_list = os.listdir(dir_path+'/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            st.error(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        st.error(
            f"The label you selected doesn't exist."
            f"The existing options are: {labels}"
        )