import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Puerto Rico AI Olympiad", layout="wide")

# Load scores
@st.cache_data
def load_scores():
    return pd.read_csv("scores.csv")

scores_df = load_scores()

# App Title
st.title("🇵🇷 Puerto Rico National Olympiad of Artificial Intelligence")

# Scores Table
st.subheader("📊 Live Scores")
st.dataframe(scores_df, use_container_width=True)

# Page Navigation
task = st.sidebar.radio("Select Task Page", ("Task 1", "Task 2", "Task 3", "Task 4"))

task_id = task.lower().replace(" ", "")
task_file = f"{task_id}.ipynb"
task_path = Path("tasks") / task_file

st.markdown("---")
st.subheader(f"📝 {task}: Instructions & Submission")

# Download the notebook
if task_path.exists():
    with open(task_path, "rb") as f:
        st.download_button(
            label=f"📥 Download {task_file}",
            data=f,
            file_name=task_file,
            mime="application/x-ipynb+json"
        )
else:
    st.warning(f"No notebook found for {task}")

# Upload predictions
st.markdown("### ⬆️ Upload Your Prediction File (CSV)")
uploaded_file = st.file_uploader("Upload your `.csv` prediction file for this task.", type=["csv"], key=task)

if uploaded_file:
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)
    save_path = upload_dir / f"{task_id}_{uploaded_file.name}"
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"Uploaded: {uploaded_file.name}")
