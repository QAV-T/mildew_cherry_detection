import streamlit as st
import pandas as pd
from src.data_management import load_pickle_file


def load_test_evaluation():
    st.dataframe(pd.DataFrame(
        load_pickle_file(f'models/evaluation.pk1'), index=['Loss', 'Accuracy']))
