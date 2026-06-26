from src.constants import (
    ATS_SCORE,
    INVALID_ATS_SCORE_RANGE_ERROR,
    INVALID_ATS_SCORE_TYPE_ERROR,
    INVALID_LIST_TYPE_ERROR,
    LIST_ANALYSIS_FIELDS,
    MAX_ATS_SCORE,
    MIN_ATS_SCORE,
    MISSING_REQUIRED_FIELD_ERROR,
    REQUIRED_ANALYSIS_KEYS,
)
from src.exceptions import ResumeAnalysisError


def _validate_required_keys(analysis_data: dict):
    """
    Validate that all required analysis keys are present.
    Parameters: analysis_data (dict): Resume analysis returned by Gemini.
    Returns: None
    Raises:
        ResumeAnalysisError: Raised when one or more required keys are missing.
    """
    for required_key in REQUIRED_ANALYSIS_KEYS:
        if required_key not in analysis_data:
            raise ResumeAnalysisError(
                f"{MISSING_REQUIRED_FIELD_ERROR}: {required_key}"
            )


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
    Parameters: analysis (dict): Resume analysis returned by Gemini.
    Returns: dict: Validated resume analysis.
    Raises:
        ResumeAnalysisError: Raised when the analysis is invalid.
    """
    _validate_required_keys(
        analysis_data=analysis_data
    )
    _validate_ats_score(
        analysis_data=analysis_data
    )
    _validate_analysis_lists(
        analysis_data=analysis_data
    )
    return analysis_data