RESUME_ANALYSIS_PROMPT = """
You are an experienced Technical Recruiter and ATS (Applicant Tracking System).

Analyze the candidate's resume against the provided job description.

Resume:
{resume_text}

Job Description:
{job_description}

Instructions:

1. Analyze ONLY the information present in the resume.
2. Compare it with the provided job description.
3. Do NOT assume or invent any skills.
4. Calculate an ATS Match Score between 0 and 100.
5. Keep recommendations concise and practical.
6. Return ONLY valid JSON.
7. Do NOT wrap the JSON inside markdown.
8. Do NOT write any explanation before or after the JSON.

Return the response in the following format:

{{
    "ats_score": 85,
    "matching_skills": [
        "Python",
        "SQL"
    ],
    "missing_skills": [
        "AWS",
        "Docker"
    ],
    "strengths": [
        "Automation experience",
        "Problem solving"
    ],
    "recommendations": [
        "Highlight project achievements",
        "Add cloud experience"
    ]
}}
"""