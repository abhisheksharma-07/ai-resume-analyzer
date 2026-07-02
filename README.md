# AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python**, **Streamlit**, and **Google Gemini**. The application compares a candidate's resume against a job description, generates an ATS compatibility score, identifies matching and missing skills, highlights strengths, provides improvement recommendations, and exports the analysis as a Markdown report.

The project emphasizes both **Artificial Intelligence** and **Software Engineering** best practices by following a modular architecture, validating AI responses, handling errors gracefully, and optimizing performance through caching.


# Features

* Upload resumes in PDF format.
* Analyze resumes using Google's Gemini 2.5 Flash.
* Compare resumes against any job description.
* Generate an ATS Match Score (0–100).
* Display an overall recommendation level.
* Identify matching skills.
* Identify missing skills.
* Highlight candidate strengths.
* Generate practical improvement recommendations.
* Validate whether the uploaded document is a professional resume before analysis.
* Validate AI-generated JSON responses before displaying results.
* Cache PDF extraction and repeated AI analyses for improved performance.
* Export the complete analysis as a Markdown report.
* Interactive dashboard built with Streamlit.


# Tech Stack

| Category              | Technology              |
| --------------------- | ----------------------- |
| Language              | Python                  |
| Web Framework         | Streamlit               |
| AI Model              | Google Gemini 2.5 Flash |
| PDF Processing        | pdfplumber              |
| Environment Variables | python-dotenv           |
| JSON Handling         | json                    |
| Version Control       | Git & GitHub            |


# Project Structure

```text
Resume-Analyzer/
│
├── app.py
├── requirements.txt
│
├── src/
│   ├── analyzer.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── pdf_parser.py
│   ├── prompts.py
│   ├── report_generator.py
│   ├── ui.py
│   ├── ui_messages.py
│   └── validators.py
│
├── sample_resume.pdf
├── README.md
└── .env
```


# Architecture

```text
                 Resume PDF
                      │
                      ▼
              PDF Text Extraction
                      │
                      ▼
            Resume Text Cleaning
                      │
                      ▼
        Gemini Prompt Construction
                      │
                      ▼
        Google Gemini Resume Analysis
                      │
                      ▼
          JSON Response Validation
                      │
                      ▼
        Resume Validation Check
                      │
                      ▼
         Streamlit Dashboard UI
                      │
                      ▼
          Markdown Report Export
```

# How It Works

1. Upload a resume in PDF format.
2. Extract text using **pdfplumber**.
3. Clean the extracted text before analysis.
4. Enter a job description.
5. Generate a structured prompt.
6. Send the prompt to **Google Gemini**.
7. Validate whether the uploaded document is a resume.
8. Generate structured JSON containing:
   * ATS Score
   * Recommendation Level
   * Overall Summary
   * Matching Skills
   * Missing Skills
   * Strengths
   * Recommendations
9. Validate the returned JSON.
10. Display results in an interactive dashboard.
11. Download the complete analysis as a Markdown report.


# Key Engineering Decisions

This project was designed with software engineering best practices rather than being a simple AI demo.

### Clean Architecture

* Modular project structure.
* Separation of concerns.
* Reusable helper functions.
* Single Responsibility Principle (SRP).

### AI Engineering

* Prompt engineering for structured responses.
* JSON-only AI output.
* AI response validation before rendering.
* Resume classification to reject unsupported documents.

### Error Handling

* Custom exception handling.
* Required field validation.
* ATS score validation.
* List validation.
* Invalid document detection.

### Performance Optimization

* Cached PDF extraction.
* Cached Gemini responses for repeated analyses.
* Optimized PDF text processing.


# Skills Demonstrated

* Python
* Streamlit
* Google Gemini API
* Prompt Engineering
* JSON Processing
* PDF Processing
* Exception Handling
* Modular Software Design
* Data Validation
* Performance Optimization
* Git & GitHub


# Installation

## Clone the repository

```bash
git clone <repository-url>
cd Resume-Analyzer
```
## Create a virtual environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```
## Install dependencies

```bash
pip install -r requirements.txt
```

# Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

# Run the Application

```bash
streamlit run app.py
```

# 🔮 Future Improvements

* Export reports as PDF.
* Support Microsoft Word (.docx) resumes.
* Multi-language resume analysis.
* Batch resume evaluation.
* Resume comparison across multiple candidates.
* Support multiple LLM providers.
* Cloud deployment with persistent storage.
* User authentication and profile management.
