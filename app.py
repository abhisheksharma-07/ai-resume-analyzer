import streamlit as st
from src.pdf_parser import extract_text_from_pdf
from src.analyzer import analyze_resume


def configure_page():
    """
    Configure Streamlit page settings. This function sets:
    - Page title
    - Layout
    - Browser tab name
    Returns:None
    """
    st.set_page_config(
        page_title="AI Resume Analyzer",
        layout="wide"
    )


def display_header():
    """
    Display the application title and description.
    Returns: None
    """
    st.title("AI Resume Analyzer")
    st.write(
        """
        Upload a resume and provide a job description.
        The system will analyze the resume against the job requirements
        and generate insights such as ATS score, skill gaps, and
        improvement recommendations.
        """
    )


def collect_user_input() -> tuple:
    """
    Collect user inputs from the Streamlit interface.
    Returns:
    tuple: uploaded_resume (UploadedFile | None): Uploaded PDF resume file.
            job_description (str): Job description entered by the user
    """
    uploaded_resume = st.file_uploader(
        label="Upload Resume (PDF)",
        type=["pdf"]
    )
    job_description = st.text_area(
        label="Paste Job Description",
        height=200
    )
    return uploaded_resume, job_description


def handle_analysis_request(uploaded_resume, job_description: str):
    """
    Handle Analyze button click.
    Parameters:
    uploaded_resume: Uploaded PDF file received from Streamlit.
    job_description (str): Job description entered by the user.
    Returns: None
    """
    if st.button("Analyze Resume"):
        if uploaded_resume is None:
            st.warning("Please upload a resume.")
            return
        if not job_description.strip():
            st.warning("Please enter a job description.")
            return
        resume_text = extract_text_from_pdf(uploaded_resume)
        analysis_result = analyze_resume(resume_text=resume_text, job_description=job_description)

        st.success("Resume analyzed successfully.")

        st.subheader("Analysis Result")

        st.write(analysis_result)


def main():
    """
    Main entry point of the application. This function orchestrates:
    - Page configuration
    - UI rendering
    - User input collection
    - Analysis request handling
    Returns: None
    """
    configure_page()
    display_header()
    uploaded_resume, job_description = collect_user_input()
    handle_analysis_request(
        uploaded_resume=uploaded_resume,
        job_description=job_description
    )


if __name__ == "__main__":
    main()
