import streamlit as st
from src.pdf_parser import extract_text_from_pdf
from src.analyzer import analyze_resume
from src.ui import display_analysis_dashboard
from src.validators import validate_analysis
from src.exceptions import ResumeAnalysisError
from src.constants import (
    JOB_DESCRIPTION_HEIGHT,
    PAGE_LAYOUT,
    PAGE_TITLE,
    RESUME_ANALYSIS_FAILED_MESSAGE,
    RESUME_TEXT_HEIGHT,
    SUPPORTED_FILE_TYPES,
)
from src.ui_messages import (
    ANALYSIS_RESULT_HEADER,
    ANALYZE_BUTTON_TEXT,
    APP_DESCRIPTION,
    EXTRACTED_TEXT_HEADER,
    JOB_DESCRIPTION_LABEL,
    JOB_DESCRIPTION_WARNING,
    RESUME_CONTENT_LABEL,
    RESUME_PROCESSED_SUCCESS,
    UPLOAD_RESUME_LABEL,
    UPLOAD_WARNING,
)


def configure_page():
    """
    Configure Streamlit page settings. This function sets:
    - Page title
    - Layout
    - Browser tab name
    Returns:None
    """
    st.set_page_config(
        page_title=PAGE_TITLE,
        layout=PAGE_LAYOUT
    )


def display_header():
    """
    Display the application title and description.
    Returns: None
    """
    st.title(PAGE_TITLE)
    st.write(APP_DESCRIPTION)


def collect_user_input() -> tuple:
    """
    Collect user inputs from the Streamlit interface.
    Returns:
    tuple: uploaded_resume (UploadedFile | None): Uploaded PDF resume file.
            job_description (str): Job description entered by the user
    """
    uploaded_resume = st.file_uploader(
    label=UPLOAD_RESUME_LABEL,
    type=SUPPORTED_FILE_TYPES
    )
    job_description = st.text_area(
        label=JOB_DESCRIPTION_LABEL,
        height=JOB_DESCRIPTION_HEIGHT
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
    if st.button(ANALYZE_BUTTON_TEXT):
        if uploaded_resume is None:
            st.warning(UPLOAD_WARNING)
            return
        if not job_description.strip():
            st.warning(JOB_DESCRIPTION_WARNING)
            return
        try:
            resume_text = extract_text_from_pdf(uploaded_resume=uploaded_resume)
            analysis_data = analyze_resume(
                resume_text=resume_text,
                job_description=job_description
            )
            analysis_data = validate_analysis(analysis_data=analysis_data)
            st.success(RESUME_PROCESSED_SUCCESS)
            display_analysis_dashboard(analysis=analysis_data)

        except ResumeAnalysisError as exception:
            st.error(
                f"{RESUME_ANALYSIS_FAILED_MESSAGE}\n\nReason: {exception}"
            )


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
