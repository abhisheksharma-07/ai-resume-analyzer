# Gemini Configuration
MODEL_NAME = "gemini-2.5-flash"
GEMINI_API_KEY_ENV = "GEMINI_API_KEY"

# Streamlit Configuration
PAGE_TITLE = "AI Resume Analyzer"
PAGE_LAYOUT = "wide"
SUPPORTED_FILE_TYPES = ["pdf"]
JOB_DESCRIPTION_HEIGHT = 200

# Analysis Dictionary Keys
ATS_SCORE = "ats_score"
MATCHING_SKILLS = "matching_skills"
MISSING_SKILLS = "missing_skills"
STRENGTHS = "strengths"
RECOMMENDATIONS = "recommendations"
SUMMARY = "summary"
RECOMMENDATION_LEVEL = "recommendation_level"

# Exception Messages
GEMINI_API_KEY_NOT_FOUND_ERROR = "Gemini API key was not found."
INVALID_JSON_RESPONSE_ERROR = "Gemini returned an invalid JSON response."
MISSING_REQUIRED_FIELD_ERROR = ("Missing required analysis field")
INVALID_ATS_SCORE_TYPE_ERROR = ("ATS score must be an integer.")
INVALID_ATS_SCORE_RANGE_ERROR = ("ATS score must be between 0 and 100.")
INVALID_LIST_TYPE_ERROR = ("Analysis field must be a list.")
RESUME_ANALYSIS_FAILED_MESSAGE = "Unable to analyze the uploaded resume."
MISSING_REQUIRED_KEYS_ERROR = ("Missing required keys: {}")

# Validation
MIN_ATS_SCORE = 0
MAX_ATS_SCORE = 100

# Document Types
RESUME_DOCUMENT_TYPE = "resume"
NON_RESUME_DOCUMENT_TYPE = "non_resume"
DOCUMENT_TYPE = "document_type"
DOCUMENT_VALIDATION_MESSAGE = "document_validation_message"

# List Validation
LIST_ANALYSIS_FIELDS = [
    MATCHING_SKILLS,
    MISSING_SKILLS,
    STRENGTHS,
    RECOMMENDATIONS,
]

# ATS Score Categories
EXCELLENT_MATCH = "Excellent Match"
GOOD_MATCH = "Good Match"
NEEDS_IMPROVEMENT = "Needs Improvement"
EXCELLENT_MATCH_ICON = "🟢"
GOOD_MATCH_ICON = "🟡"
NEEDS_IMPROVEMENT_ICON = "🔴"
EXCELLENT_MATCH_DESCRIPTION = "The resume is highly aligned with the job description."
GOOD_MATCH_DESCRIPTION = "The resume matches most job requirements."
NEEDS_IMPROVEMENT_DESCRIPTION = "The resume requires significant improvements."

# Recommendation Levels
HIGHLY_RECOMMENDED = "Highly Recommended"
RECOMMENDED = "Recommended"
PARTIALLY_SUITABLE = "Partially Suitable"
NOT_RECOMMENDED = "Not Recommended"
HIGHLY_RECOMMENDED_ICON = "🟢"
RECOMMENDED_ICON = "🟡"
PARTIALLY_SUITABLE_ICON = "🟠"
NOT_RECOMMENDED_ICON = "🔴"
DEFAULT_RECOMMENDATION_ICON = "⚪"
RECOMMENDATION_LEVEL_ICONS = {
    HIGHLY_RECOMMENDED: HIGHLY_RECOMMENDED_ICON,
    RECOMMENDED: RECOMMENDED_ICON,
    PARTIALLY_SUITABLE: PARTIALLY_SUITABLE_ICON,
    NOT_RECOMMENDED: NOT_RECOMMENDED_ICON,
}

# Report Generation
MARKDOWN_REPORT_BUTTON_LABEL = "📄 Download Markdown Report"
MARKDOWN_REPORT_FILE_NAME = "resume_analysis.md"
MARKDOWN_REPORT_MIME_TYPE = "text/markdown"
