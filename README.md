# Resume To Job Matcher Streamlit App
This is a Simple NLP project using spaCy library of python that matches resumes sent and saved in a json file with job opportunities

## 🔍 Overview

This project allows you to match **job opportunities to resumes** using **spaCy embeddings** and **vector similarity**.

Using `spaCy`'s `en_core_web_lg` language model, this app embeds **key words** from resumes and job descriptions. You can:

- Select a **job** and view **top 3 matching resumes**
- The matching is calculated using **Euclidean distance** between vector means of keywords.

## 📁 Folder Structure

```plaintext
├── resumes.json
├── job_opportunities.json
└── main.py
````

This app loads the related job opportunities from a locally saved json file called `job_opportunities.json` and the same happens for resumes from `resumes.json`

## 🏃‍♂️‍➡️ How to run

To run the script locally on your device, you have to install python and pip and install streamlit, spaCy and numpy through pip package manager.

Assuming you have **python** installed on your device :

```shell
pip install streamlit spacy numpy
```

and run the python script via streamlit using :

```shell
streamlit run main.py
```
