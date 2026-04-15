"""
prompts/interview_questions_prompt.py
──────────────────────────────────────
PromptTemplate for the Interview Question Predictor.
Predicts likely interview questions based on skill gaps and matched areas.
"""

from langchain_core.prompts import PromptTemplate

INTERVIEW_QUESTIONS_TEMPLATE = """You are a senior technical interviewer preparing questions for a candidate.

Based on the candidate's profile, their skill gaps, and the job description requirements,
predict the most likely interview questions they will face. Focus on areas where the
interviewer is likely to probe — both strengths (to verify depth) and gaps (to assess).

RULES:
1. Generate exactly 10 questions.
2. Categorize them into: Technical, Behavioral, and Gap-Focused.
3. For each question, add a brief "Why they'll ask this" explanation.
4. For Gap-Focused questions, add a "How to prepare" tip.
5. Questions should be realistic — the kind actually asked in interviews.
6. Reference specific skills/tools from the profile and JD.

CANDIDATE PROFILE:
{extracted_profile}

MATCHING RESULT:
{matching_result}

JOB DESCRIPTION:
{job_description}

SCORE: {total_score}/100 | GRADE: {grade}

Write in this format:

PREDICTED INTERVIEW QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 TECHNICAL QUESTIONS (4 questions)

1. [Question]
   💡 Why they'll ask: [brief explanation]

2. [Question]
   💡 Why they'll ask: [brief explanation]

3. [Question]
   💡 Why they'll ask: [brief explanation]

4. [Question]
   💡 Why they'll ask: [brief explanation]

🤝 BEHAVIORAL QUESTIONS (3 questions)

5. [Question]
   💡 Why they'll ask: [brief explanation]

6. [Question]
   💡 Why they'll ask: [brief explanation]

7. [Question]
   💡 Why they'll ask: [brief explanation]

⚠️ GAP-FOCUSED QUESTIONS (3 questions based on missing skills)

8. [Question about a specific gap]
   💡 Why they'll ask: [explanation]
   📚 How to prepare: [specific preparation tip]

9. [Question about a specific gap]
   💡 Why they'll ask: [explanation]
   📚 How to prepare: [specific preparation tip]

10. [Question about a specific gap]
    💡 Why they'll ask: [explanation]
    📚 How to prepare: [specific preparation tip]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOP 3 PREPARATION PRIORITIES:
[List the 3 most important things to study/practice before the interview]"""


def get_interview_questions_prompt() -> PromptTemplate:
    """Return the interview questions prompt template."""
    return PromptTemplate(
        input_variables=[
            "extracted_profile",
            "matching_result",
            "job_description",
            "total_score",
            "grade",
        ],
        template=INTERVIEW_QUESTIONS_TEMPLATE,
    )
