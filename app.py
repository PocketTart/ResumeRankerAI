import streamlit as st
import pandas as pd
import os
import tempfile
from tools.extract_text import extract_text_from_pdf
from tools.nlp_matcher import match_resume_to_jd
from agents.jd_agent import extract_skills_from_jd
from agents.screening_agent import evaluate_resume
from utils.leaderboard import build_leaderboard

# --- Page Config ---
st.set_page_config(page_title="ResumeRanker AI", layout="centered")
st.markdown("""
    <style>
        .main { background-color: #f9f9f9; }
        .stApp {
            padding: 1rem;
            font-family: 'Segoe UI', sans-serif;
        }
        .stDownloadButton {
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("ResumeRanker AI")
st.subheader("Automated Resume Screening and Ranking System")

st.markdown("---")

# --- Upload Section ---
st.header("Step 1: Upload Files")
jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])
resume_files = st.file_uploader("Upload Resumes (PDFs)", type=["pdf"], accept_multiple_files=True)

# --- Main Processing ---
if jd_file and resume_files:
    with st.spinner("Extracting job description..."):
        jd_text = extract_text_from_pdf(jd_file)
        jd_skills = extract_skills_from_jd(jd_text)

    resume_data = []
    with st.spinner("Processing resumes..."):
        for resume_file in resume_files:
            name = os.path.splitext(resume_file.name)[0]
            resume_text = extract_text_from_pdf(resume_file)
            score = match_resume_to_jd(jd_skills, resume_text)
            feedback = evaluate_resume(jd_text, resume_text)
            resume_data.append({
                "Name": name,
                "Score": score,
                "Feedback": feedback
            })

    leaderboard_df = build_leaderboard(resume_data)

    st.markdown("---")
    st.header("Step 2: Leaderboard")
    st.success("Resumes processed successfully. Sorted by best match:")

    st.dataframe(leaderboard_df, use_container_width=True)

    # --- CSV Download ---
    output_path = os.path.join(tempfile.gettempdir(), "leaderboard.csv")
    leaderboard_df.to_csv(output_path, index=False)

    with open(output_path, "rb") as f:
        st.download_button(
            label="Download Leaderboard as CSV",
            data=f,
            file_name="leaderboard.csv",
            mime="text/csv",
        )

else:
    st.info("Please upload a job description and at least one resume to get started.")
