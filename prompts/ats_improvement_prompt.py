"""
prompts/ats_improvement_prompt.py
──────────────────────────────────
PromptTemplate for the ATS Improvement step — used in Applicant Mode.
Produces actionable, specific tips to help a job seeker optimize their
resume for ATS (Applicant Tracking System) compatibility.
"""

from langchain_core.prompts import PromptTemplate

ATS_IMPROVEMENT_TEMPLATE = """You are an expert ATS (Applicant Tracking System) consultant who helps job
applicants optimize their resumes to pass automated screening software.

You have the full pipeline analysis of a resume screened against a specific job description.
Based on this data, provide SPECIFIC, ACTIONABLE improvement tips so that the applicant
can increase their ATS score.

RULES:
1. Be specific — reference actual skill names, keywords, and tools from the data.
2. Never make up information not present in the pipeline results.
3. Focus on practical changes the applicant can make RIGHT NOW.
4. Prioritize tips by impact — most important changes first.
5. Keep the language encouraging and constructive, NOT discouraging.

CANDIDATE NAME: {candidate_name}
CURRENT ATS SCORE: {total_score}/100
GRADE: {grade}

EXTRACTED PROFILE:
{extracted_profile}

MATCHING RESULT (vs Job Description):
{matching_result}

SCORE BREAKDOWN:
{score_result}

Write your ATS optimization report in this EXACT format:

ATS OPTIMIZATION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Candidate: {candidate_name}
Current ATS Score: {total_score}/100 | Grade: {grade}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟢 WHAT'S WORKING WELL:
[2-3 bullet points about what the resume already does well for this JD — cite specific matched skills/tools]

🔴 MISSING KEYWORDS TO ADD:
[List every missing skill and tool from the matching result. For each one, suggest a short phrase the applicant could add to their resume, e.g. "Add 'Kubernetes' to your Technical Skills section"]

📝 RESUME IMPROVEMENT TIPS:
[4-6 specific, numbered tips. Examples:
 1. Add a "Technical Skills" section listing: [missing tools]
 2. Quantify your experience with [matched skill] — e.g. "Built 3 ML pipelines..."
 3. Include the keyword "[missing keyword]" in your summary/objective
 4. Add [X] more years of relevant experience by including freelance/side projects
 etc.]

📊 ESTIMATED SCORE AFTER FIXES:
[Give a realistic estimated score range if the applicant implements all the above tips]"""


def get_ats_improvement_prompt() -> PromptTemplate:
    """Return the ATS improvement prompt template."""
    return PromptTemplate(
        input_variables=[
            "candidate_name",
            "total_score",
            "grade",
            "extracted_profile",
            "matching_result",
            "score_result",
        ],
        template=ATS_IMPROVEMENT_TEMPLATE,
    )
