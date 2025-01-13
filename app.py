from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai
import fitz  # PyMuPDF


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text



def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Open the uploaded PDF with PyMuPDF (fitz)
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        # Extract the first page
        first_page = doc.load_page(0)

        # Convert the page to a pixmap (image)
        pix = first_page.get_pixmap()

        # Convert Pixmap to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Convert the PIL Image to a BytesIO object as JPEG
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        # Convert the image bytes to base64
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("Percentage match")

submit3 = st.button("Probability of Selection For this Role")

input_prompt1 = """
You are an experienced Technical Human Resource Manager, skilled in reviewing resumes for all career types, including HR, web developers, MERN developers, software development engineers (SDE),
data scientists, and more. Your task is to compare the provided resume with the job description for the specified role. Based on this comparison, please provide a clear evaluation of whether the
candidate's profile aligns with the job requirements. Assess the skills mentioned in the resume, highlighting any that are missing or present as required by the job description. 
Evaluate the candidate’s certifications, years of experience, project relevance, academic performance, and any other pertinent fields like soft skills or additional qualifications. 
Offer a detailed review with concise points on strengths and weaknesses, and use simple language to make your evaluation clear. create the response in clear cut points , attractive and appealing and use emojies where required.
"""

input_prompt2 = """

You are an advanced ATS (Applicant Tracking System) scanner with a strong understanding of both data science and the functionality of ATS systems. 
Your task is to analyze the provided resume against the given job description. Start by calculating the percentage match between the resume and the job description. 
After presenting the percentage match, identify the specific keywords or skills that are missing in the resume compared to the job description.
List these missing skills as precise points. Based on this, suggest the exact skills or phrases the candidate should incorporate into their resume to improve the match.
Ensure that your output is clear, concise, and easy to understand, using simple language. Additionally, 
Use emojis where appropriate to enhance the clarity and appeal of the response. The entire analysis should be delivered in a well-structured format with easy-to-follow points.
create the response in clear cut points , attractive and appealing and use emojies where required. Suggest Keywords to add in resume in points

"""
input_prompt3 = """
You are an experienced Technical Human Resource Manager, tasked with analyzing a candidate's resume against a job description. Based on this comparison, create a conclusion summary 
with clear, concise points, evaluating how well the candidate matches the job requirements. Highlight the presence or absence of required skills, certifications, relevant experience
(including the number of years), and the suitability of the candidate's projects. Evaluate the candidate's academic scores and how they align with the job description. Additionally, 
provide a probability prediction of the candidate's chance of selection for the role, presented as a percentage. Ensure the summary is easy to understand, offering a professional and 
straightforward assessment.create the response in clear cut points , attractive and appealing and use emojies where required.


"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")