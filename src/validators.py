from src.constants import (
    ATS_SCORE,
    DOCUMENT_TYPE,
    DOCUMENT_VALIDATION_MESSAGE,
    INVALID_ATS_SCORE_RANGE_ERROR,
    INVALID_ATS_SCORE_TYPE_ERROR,
    INVALID_LIST_TYPE_ERROR,
    LIST_ANALYSIS_FIELDS,
    MATCHING_SKILLS,
    MAX_ATS_SCORE,
    MIN_ATS_SCORE,
    MISSING_REQUIRED_KEYS_ERROR,
    MISSING_SKILLS,
    RECOMMENDATION_LEVEL,
    RECOMMENDATIONS,
    RESUME_DOCUMENT_TYPE,
    STRENGTHS,
    SUMMARY,
)
from src.exceptions import ResumeAnalysisError

RESUME_REQUIRED_KEYS = [
    DOCUMENT_TYPE,
    DOCUMENT_VALIDATION_MESSAGE,
    SUMMARY,
    RECOMMENDATION_LEVEL,
    ATS_SCORE,
    MATCHING_SKILLS,
    MISSING_SKILLS,
    STRENGTHS,
    RECOMMENDATIONS,
]

NON_RESUME_REQUIRED_KEYS = [
    DOCUMENT_TYPE,
    DOCUMENT_VALIDATION_MESSAGE,
]


def _validate_required_keys(analysis_data: dict):
    """
    Validate that all required analysis keys are present.
    Parameters: analysis_data (dict): Resume analysis returned by Gemini.
    Returns: None
    Raises:
        ResumeAnalysisError: Raised when one or more required keys are missing.
    """
    document_type = analysis_data.get(DOCUMENT_TYPE)
    if document_type == RESUME_DOCUMENT_TYPE:
        required_keys = RESUME_REQUIRED_KEYS
    else:
        required_keys = NON_RESUME_REQUIRED_KEYS
    missing_keys = [key for key in required_keys if key not in analysis_data]
    if missing_keys:
        raise ResumeAnalysisError(MISSING_REQUIRED_KEYS_ERROR.format(", ".join(missing_keys)))


def _validate_ats_score(analysis_data: dict):
    """
    Validate the ATS score.
    Parameters: analysis_data (dict): Resume analysis returned by Gemini.
    Returns: None
    Raises:
        ResumeAnalysisError: Raised when the ATS score is invalid.
    """
    ats_score = analysis_data[ATS_SCORE]
    if not isinstance(ats_score, int):
        raise ResumeAnalysisError(
            INVALID_ATS_SCORE_TYPE_ERROR
        )
    if (ats_score < MIN_ATS_SCORE or ats_score > MAX_ATS_SCORE):
        raise ResumeAnalysisError(
            INVALID_ATS_SCORE_RANGE_ERROR
        )


def _validate_analysis_lists(analysis_data: dict):
    """
    Validate that all list-based analysis fields are lists.
    Parameters: analysis_data (dict): Resume analysis returned by Gemini.
    Returns: None
    Raises:
        ResumeAnalysisError: Raised when an analysis field is not a list.
    """
    for field_name in LIST_ANALYSIS_FIELDS:
        if not isinstance(
            analysis_data[field_name],
            list
        ):
            raise ResumeAnalysisError(
                f"{field_name}: {INVALID_LIST_TYPE_ERROR}"
            )


def validate_analysis(analysis_data: dict):
    """
    Validate the resume analysis returned by Gemini.
    Parameters: analysis_data (dict): Resume analysis returned by Gemini.
    Returns: dict: Validated resume analysis.
    Raises:
        ResumeAnalysisError: Raised when the analysis is invalid.
    """
    _validate_required_keys(analysis_data=analysis_data)
    if (analysis_data[DOCUMENT_TYPE] == RESUME_DOCUMENT_TYPE):
        _validate_ats_score(analysis_data=analysis_data)
        _validate_analysis_lists(analysis_data=analysis_data)
    return analysis_data
        