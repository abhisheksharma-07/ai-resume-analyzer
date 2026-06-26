# Gemini Configuration
MODEL_NAME = "gemini-2.5-flash"
GEMINI_API_KEY_ENV = "GEMINI_API_KEY"

# Streamlit Configuration
PAGE_TITLE = "AI Resume Analyzer"
PAGE_LAYOUT = "wide"
SUPPORTED_FILE_TYPES = ["pdf"]
JOB_DESCRIPTION_HEIGHT = 200
RESUME_TEXT_HEIGHT = 300

# Analysis Dictionary Keys
ATS_SCORE = "ats_score"
MATCHING_SKILLS = "matching_skills"
MISSING_SKILLS = "missing_skills"
STRENGTHS = "strengths"
RECOMMENDATIONS = "recommendations"

# Exception Messages
GEMINI_API_KEY_NOT_FOUND_ERROR = "Gemini API key was not found."
INVALID_JSON_RESPONSE_ERROR = "Gemini returned an invalid JSON response."
MISSING_REQUIRED_FIELD_ERROR = ("Missing required analysis field")
INVALID_ATS_SCORE_TYPE_ERROR = ("ATS score must be an integer.")
INVALID_ATS_SCORE_RANGE_ERROR = ("ATS score must be between 0 and 100.")
INVALID_LIST_TYPE_ERROR = ("Analysis field must be a list.")
RESUME_ANALYSIS_FAILED_MESSAGE = "Unable to analyze the uploaded resume."

# Validation
MIN_ATS_SCORE = 0
MAX_ATS_SCORE = 100

# Required Analysis Keys
REQUIRED_ANALYSIS_KEYS = [
    ATS_SCORE,
    MATCHING_SKILLS,
    MISSING_SKILLS,
    STRENGTHS,
    RECOMMENDATIONS,
]

# List Validation
LIST_ANALYSIS_FIELDS = [
    MATCHING_SKILLS,
    MISSING_SKILLS,
    STRENGTHS,
    RECOMMENDATIONS,
]
