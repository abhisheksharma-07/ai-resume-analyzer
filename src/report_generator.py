from src.constants import (
    ATS_SCORE,
    MATCHING_SKILLS,
    MISSING_SKILLS,
    RECOMMENDATION_LEVEL,
    RECOMMENDATIONS,
    STRENGTHS,
    SUMMARY,
)


def _add_bullet_section(report_lines: list, heading: str, items: list):
    """
    Add a Markdown bullet section to the report.
    Parameters: 
        report_lines (list): Markdown report being built.
        heading (str): Section heading.
        items (list): Items to display as bullet points.
    Returns: None
    """
    report_lines.append(f"## {heading}")
    report_lines.append("")

    for item in items:
        report_lines.append(f"- {item}")

    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")


def generate_markdown_report(analysis_data: dict,):
    """
    Generate a Markdown report from the resume analysis.
    Parameters: analysis_data (dict): Resume analysis returned by Gemini.
    Returns: Resume analysis formatted as Markdown.
    """
    report_lines = [
        "# Resume Analysis Report",
        "",
        "## Overall Assessment",
        "",
        analysis_data[SUMMARY],
        "",
        "---",
        "",
        "## Recommendation Level",
        "",
        analysis_data[RECOMMENDATION_LEVEL],
        "",
        "---",
        "",
        "## ATS Score",
        "",
        f"{analysis_data[ATS_SCORE]}%",
        "",
        "---",
        "",
    ]
    _add_bullet_section(
        report_lines=report_lines,
        heading="Matching Skills",
        items=analysis_data[MATCHING_SKILLS],
    )
    _add_bullet_section(
        report_lines=report_lines,
        heading="Missing Skills",
        items=analysis_data[MISSING_SKILLS],
    )
    _add_bullet_section(
        report_lines=report_lines,
        heading="Strengths",
        items=analysis_data[STRENGTHS],
    )
    _add_bullet_section(
        report_lines=report_lines,
        heading="Recommendations",
        items=analysis_data[RECOMMENDATIONS],
    )
    return "\n".join(report_lines)
