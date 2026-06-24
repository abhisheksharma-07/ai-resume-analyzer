import os
from dotenv import load_dotenv
import google.generativeai as genai
from src.prompts import RESUME_ANALYSIS_PROMPT


load_dotenv()


def analyze_resume(resume_text: str, job_description: str):
    """
    Analyze a resume against a job description using Gemini.
    Parameters:
    resume_text (str): Extracted text from the resume.
    job_description (str): Job description entered by the user.
    Returns: Gemini-generated analysis.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )
    response = model.generate_content(prompt)

    return response.text
