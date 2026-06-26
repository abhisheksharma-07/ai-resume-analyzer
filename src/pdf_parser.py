import pdfplumber


def extract_text_from_pdf(uploaded_resume):
    """
    Extract text from an uploaded PDF file.
    Parameters:
    uploaded_file: PDF file received from Streamlit file uploader.
    Returns: Extracted text from all pages of the PDF.
    """
    extracted_text = ""
    with pdfplumber.open(uploaded_resume) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + "\n"

    return extracted_text
    