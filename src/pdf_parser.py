import pdfplumber
import streamlit as st


def _clean_resume_text(extracted_text: str):
    """
    Clean extracted resume text before sending it to Gemini.
    Parameters: extracted_text (str): Raw text extracted from the PDF.
    Returns: Cleaned resume text.
    """
    cleaned_lines = []
    for line in extracted_text.splitlines():
        line = line.strip()
        if line:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


@st.cache_data(show_spinner=False)
def extract_text_from_pdf(uploaded_resume):
    """
    Extract text from an uploaded PDF file.
    Parameters: uploaded_resume: PDF file received from Streamlit.
    Returns: Extracted text from all pages.
    """
    page_contents = []
    with pdfplumber.open(
        uploaded_resume
    ) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                page_contents.append(
                    page_text
                )
    return _clean_resume_text(
        extracted_text="\n".join(page_contents)
    )
    