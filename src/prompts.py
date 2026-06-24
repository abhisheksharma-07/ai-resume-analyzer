RESUME_ANALYSIS_PROMPT = """
You are an experienced technical recruiter.
Analyze the following resume against the provided job description.
Resume:
{resume_text}

Job Description:
{job_description}

Provide:
1. Overall assessment
2. Key strengths
3. Missing skills
4. Improvement recommendations

Keep the response concise and professional.
"""
