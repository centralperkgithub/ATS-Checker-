#  Resume ATS Tracking System with Google Gemini Pro

## 🔗 LinkedIn Post

[![LinkedIn Logo](https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/linkedin.svg){:width="20"}](https://www.linkedin.com/posts/dhirendra-singh-b5b947243_ats-resume-expert-activity-7284284721218424832-JLYo?utm_source=share&)


## 🌐 Live Demo

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Resume%20ATS%20Checker-green?logo=streamlit)](https://true-resume-ats-checker.streamlit.app/)



A **large language model (LLM)-powered recruitment assistant** that evaluates resumes against job descriptions, identifies missing skills, and generates concise candidate summaries.  
This project integrates **Google Gemini Pro** with a streamlined **ATS-like workflow** to improve hiring efficiency and ensure qualified candidates are not overlooked.

---

## 📌 Overview

Traditional Applicant Tracking Systems (ATS) often filter out resumes before they reach recruiters, mainly due to keyword mismatches or formatting issues.  
This project solves that by leveraging **Google Gemini Pro** to:

- Parse resumes in real-time
- Compare them with job descriptions
- Highlight missing skills or keywords
- Provide a quick, professional candidate summary

The result is a **data-driven, LLM-assisted resume analysis tool** that benefits both recruiters and job seekers.

---

## 🚀 Key Features

- **🔍 Resume–Job Description Matching**  
  Calculates a match score and highlights strengths.
  
- **📑 Missing Keywords Detection**  
  Identifies crucial job-specific terms absent from the resume.
  
- **📝 Automated Profile Summarization**  
  Generates a professional summary of the candidate for quick review.
  
- **💻 Interactive Web Interface**  
  Built with **Streamlit** for ease of use—no complex setup required.

---

## 🛠️ Technology Stack

| Category            | Technology Used                  |
|---------------------|----------------------------------|
| Programming Language| Python                           |
| Frontend Framework  | Streamlit                        |
| AI Model            | Google Gemini Pro API            |
| Development Tools   | Jupyter Notebook, Python Scripts |
| Environment Config  | `.env` file for API key storage  |
| License             | MIT                              |

---

## 📊 How It Works

**Input** — Paste a job description and upload or paste a candidate resume.

**Processing** — The system uses Google Gemini Pro to parse and analyze the content.

**Output** —
- Match score between job description and resume
- List of missing keywords
- Professional profile summary

## 🆕 Updates & Improvements

- **PDF Text Extraction**  
  - Replaced **PDF2Image** with **pdfminer.six** for extracting text from PDF resumes.  
  - Removed dependency on **Poppler**, enabling smooth operation on any device via the provided URL without requiring local installations.
