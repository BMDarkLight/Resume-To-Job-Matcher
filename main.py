import streamlit as st
import spacy
import json
import numpy as np

nlp = spacy.load("en_core_web_lg")

@st.cache_data
def load_resumes():
    with open("resumes.json", "r", encoding="utf-8") as file:
        return json.load(file)

@st.cache_data
def load_job_opportunities():
    with open("job_opportunities.json", "r", encoding="utf-8") as file:
        return json.load(file)

resumes = load_resumes()
jobs = load_job_opportunities()

st.title("NLP Resume-to-Job Matcher")

selected_job_title = st.selectbox(
    "Select a Job Opportunity:",
    [job["title"] for job in jobs]
)

for job in jobs:
    if job["title"] == selected_job_title:
        st.header(f"Job Description for: {selected_job_title}")
        st.markdown(job.get("text", "No description provided."))

        job_keywords = " ".join(job.get("key_words", []))
        job_vector = nlp(job_keywords).vector

        scored_resumes = []
        for res in resumes:
            resume_keywords = " ".join(res.get("key_words", []))
            res_vector = nlp(resume_keywords).vector

            if np.linalg.norm(job_vector) == 0 or np.linalg.norm(res_vector) == 0:
                score = 0.0
            else:
                score = np.dot(job_vector, res_vector) / (np.linalg.norm(job_vector) * np.linalg.norm(res_vector))

            scored_resumes.append((res, score))

        scored_resumes.sort(key=lambda x: x[1], reverse=True)
        top_matches = scored_resumes[:3]

        st.header("✅ Top 3 Matched Resumes")
        for idx, (res, score) in enumerate(top_matches, 1):
            c = st.container(border=True)
            c.markdown(f"**{idx}. {res.get('title', 'Unknown')}**")
            c.markdown(f"- Summary: {res.get('text', '')}")
            c.markdown(f"- Similarity : {score:.1%}")