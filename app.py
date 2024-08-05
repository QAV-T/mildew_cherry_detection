import streamlit as st
from app_pages.multi_page import MultiPage
from app_pages.page_leaf_visualizer import page_leaf_visualizer_fn
from app_pages.page_mildew_detector import page_mildew_detector_fn
from app_pages.page_ml_performance import page_ml_performance_fn
from app_pages.page_project_hypothesis import page_project_hypothesis_fn
from app_pages.page_project_summary import page_project_summary_fn

app = MultiPage(app_name="Cherry Leaf Mildew Detection")

# Add all your applications (pages) here
app.app_page("Leaf Visualizer", page_leaf_visualizer_fn)
app.app_page("Mildew Detector", page_mildew_detector_fn)
app.app_page("ML Performance", page_ml_performance_fn)
app.app_page("Project Hypothesis", page_project_hypothesis_fn)
app.app_page("Project Summary", page_project_summary_fn)

# Run the main app
if __name__ == "__main__":
    app.run()
