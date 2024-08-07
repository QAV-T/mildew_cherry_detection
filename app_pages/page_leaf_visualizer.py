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
    
    # Placeholder visualization
    if st.checkbox("Sample Cherry Leaf Image"):
        fig, ax = plt.subplots()
        ax.imshow(np.random.rand(150, 150, 3))  # Random image as a placeholder
        st.pyplot(fig)
    
    if st.checkbox("Difference between average and variability image"):
        st.subheader("Healthy Leaf")
        st.image("models/avg_var_healthy.png", caption='Healthy Leaf-Average and Variability')
        st.subheader("Mildew Leaf")
        st.image("models/avg_var_mildew.png", caption='Mildew Leaf-Average and Variability')
    
    if st.checkbox("Data Distribution"):
        st.image("models/labels_distribution.png", caption='Data Distribution')
        
    
    if st.checkbox("Image Montage"):
        st.subheader("Create Montage")
        my_data_dir = 'inputs/datasets'
        labels = os.listdir(my_data_dir+ '/val')
        label_to_display = st.selectbox("Select Label", options=labels, index=0)
        if st.button("Create Montage"):      
          image_montage(dir_path= my_data_dir + '/val',
                      label_to_display=label_to_display,
                      nrows=8, ncols=3, figsize=(10,25))
        st.write("---")
        
        # Generate and save the montage
        # montage_save_path = 'models/image_montage.png'
        # if not os.path.exists('models'):
        #     os.makedirs('models')
        
        # image_montage(dir_path='inputs/datasets/train', label_to_display=label, nrows=3, ncols=3, figsize=(10, 15), size=(100, 100), save_path=montage_save_path)
        
        # st.image(montage_save_path, caption=f'{label} Leaf Montage')
        
def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10), size=(100, 100)):
    sns.set_style("white")
    labels = os.listdir(dir_path)
    
    if label_to_display in labels:
        images_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(f"Decrease nrows or ncols to create your montage. \n"
                  f"There are {len(images_list)} in your subset. "
                  f"You requested a montage with {nrows * ncols} spaces")
            return

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
        
        
        