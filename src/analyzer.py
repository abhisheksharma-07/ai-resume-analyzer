import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from src.prompts import RESUME_ANALYSIS_PROMPT
from src.constants import (
    GEMINI_API_KEY_ENV,
    GEMINI_API_KEY_NOT_FOUND_ERROR,
    INVALID_JSON_RESPONSE_ERROR,
    MODEL_NAME,
)
from src.exceptions import ResumeAnalysisError


load_dotenv()

def _create_analysis_prompt(resume_text: str, job_description: str):
    """
    Create the prompt for Gemini resume analysis.
    Parameters:
        resume_text (str): Extracted text from the uploaded resume.
        job_description (str): Job description entered by the user.
    Returns: Formatted prompt ready to be sent to Gemini.
    """
    return RESUME_ANALYSIS_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )


def _generate_analysis(prompt: str):
    """
    Generate resume analysis using the Gemini model.
    Parameters: prompt (str): Prompt sent to the Gemini model.
    Returns: Raw response returned by Gemini.
    """
    api_key = os.getenv(GEMINI_API_KEY_ENV)
    if not api_key:
        raise ResumeAnalysisError(GEMINI_API_KEY_NOT_FOUND_ERROR)
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text


def _clean_json_response(response_text: str):
    """
    Clean and parse the JSON response returned by Gemini.
    Parameters: response_text: Raw response returned by the Gemini model.
    Returns: dict: Parsed analysis returned as a Python dictionary.
    Raises: ResumeAnalysisError: Raised when the response cannot be parsed as valid JSON.
    """
    cleaned_response = response_text.strip()
    if cleaned_response.startswith("```json"):
        cleaned_response = cleaned_response.replace(
            "```json",
            "",
            1
        )
    if cleaned_response.endswith("```"):
        cleaned_response = cleaned_response[:-3]
    cleaned_response = cleaned_response.strip()
    try:
        return json.loads(cleaned_response)
    except json.JSONDecodeError as exception:
        raise ResumeAnalysisError(INVALID_JSON_RESPONSE_ERROR) from exception


def analyze_resume(resume_text: str, job_description: str):
    """
    Analyze a resume against a job description using Gemini.
    Parameters:
        resume_text (str): Extracted text from the uploaded resume.
        job_description (str): Job description entered by the user.
    Returns: dict: Parsed resume analysis returned as a Python dictionary.
    Raises:
        ResumeAnalysisError: Raised when resume analysis cannot be completed.
    """
    prompt = _create_analysis_prompt(
        resume_text=resume_text,
        job_description=job_description
    )
    raw_response = _generate_analysis(prompt=prompt)
    analysis_data = _clean_json_response(response_text=raw_response)
    return analysis_data
