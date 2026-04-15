"""
chains/resume_rewriter_chain.py
────────────────────────────────
LCEL chain for AI Resume Rewriter.
Generates an ATS-optimized version of the candidate's resume.
"""

from langchain_core.runnables import RunnableLambda

from chains.llm_factory import get_llm
from prompts.resume_rewriter_prompt import get_resume_rewriter_prompt


def get_resume_rewriter_chain():
    """
    Build and return the resume rewriter LCEL chain.

    Inputs:  resume_text, job_description, extracted_profile,
             matching_result, total_score, grade
    Output:  str — optimized resume text
    """
    prompt = get_resume_rewriter_prompt()
    llm = get_llm(temperature=0.3)

    chain = prompt | llm | RunnableLambda(lambda msg: msg.content)
    return chain
