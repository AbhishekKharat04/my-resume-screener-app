"""
prompts/cover_letter_prompt.py
───────────────────────────────
PromptTemplate for the AI Cover Letter Generator.
Generates a tailored, professional cover letter from resume + JD.
"""

from langchain_core.prompts import PromptTemplate

COVER_LETTER_TEMPLATE = """You are a professional career coach who writes compelling cover letters.

Using the candidate's profile and the job description, write a personalized, professional
cover letter that highlights the candidate's strongest qualifications for this specific role.

RULES:
1. Keep it 250-350 words (concise but substantive).
2. Reference SPECIFIC skills and experiences from the candidate's profile.
3. Address specific requirements from the job description.
4. Use a confident, professional tone — not generic or robotic.
5. Include a strong opening hook that shows genuine interest.
6. End with a clear call to action.
7. Never fabricate experience — only use data from the extracted profile.

CANDIDATE NAME: {candidate_name}
ATS SCORE: {total_score}/100

EXTRACTED PROFILE:
{extracted_profile}

MATCHING RESULT:
{matching_result}

JOB DESCRIPTION:
{job_description}

Write the cover letter in this format:

Dear Hiring Manager,

[Opening paragraph — hook + why you're excited about this role]

[Middle paragraph 1 — your strongest relevant experience and skills, with specifics]

[Middle paragraph 2 — additional qualifications, address key JD requirements]

[Closing paragraph — enthusiasm + call to action]

Sincerely,
{candidate_name}"""


def get_cover_letter_prompt() -> PromptTemplate:
    """Return the cover letter prompt template."""
    return PromptTemplate(
        input_variables=[
            "candidate_name",
            "total_score",
            "extracted_profile",
            "matching_result",
            "job_description",
        ],
        template=COVER_LETTER_TEMPLATE,
    )
