"""
prompts/resume_rewriter_prompt.py
──────────────────────────────────
PromptTemplate for the AI Resume Rewriter.
Takes weak/missing sections and rewrites them to be ATS-optimized.
"""

from langchain_core.prompts import PromptTemplate

RESUME_REWRITER_TEMPLATE = """You are an expert resume writer and ATS optimization specialist.

You have a candidate's current resume and the analysis of how it matches against a specific
job description. Your job is to REWRITE and OPTIMIZE the resume to maximize ATS compatibility.

RULES:
1. Keep all TRUTHFUL information from the original resume — never fabricate experience.
2. Restructure and reword to incorporate missing keywords naturally.
3. Use strong action verbs and quantified achievements.
4. Format for ATS readability (clean sections, no tables/graphics).
5. Add a targeted Professional Summary at the top.
6. Ensure the Technical Skills section includes ALL matched + missing keywords.

ORIGINAL RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

EXTRACTED PROFILE:
{extracted_profile}

MATCHING RESULT:
{matching_result}

SCORE: {total_score}/100 | GRADE: {grade}

Write the OPTIMIZED resume in this format:

═══════════════════════════════════════
OPTIMIZED RESUME (ATS-Friendly Version)
═══════════════════════════════════════

[CANDIDATE NAME]
[Contact info from original — keep as-is]

━━━ PROFESSIONAL SUMMARY ━━━
[3-4 sentences targeting this specific role. Incorporate key matched AND missing skills naturally.]

━━━ TECHNICAL SKILLS ━━━
[Organized by category. Include ALL relevant skills — both matched and missing ones the candidate can legitimately claim]

━━━ PROFESSIONAL EXPERIENCE ━━━
[Rewrite each role with:
 - Strong action verbs (Developed, Architected, Deployed, Optimized...)
 - Quantified achievements (increased X by Y%, reduced Z by W%)
 - Keywords from the JD woven naturally into descriptions]

━━━ EDUCATION ━━━
[Keep as-is from original]

━━━ CERTIFICATIONS / PROJECTS ━━━
[If applicable, highlight relevant ones]

After the resume, add:
━━━ CHANGES MADE ━━━
[Bullet list of specific changes you made and why]"""


def get_resume_rewriter_prompt() -> PromptTemplate:
    """Return the resume rewriter prompt template."""
    return PromptTemplate(
        input_variables=[
            "resume_text",
            "job_description",
            "extracted_profile",
            "matching_result",
            "total_score",
            "grade",
        ],
        template=RESUME_REWRITER_TEMPLATE,
    )
