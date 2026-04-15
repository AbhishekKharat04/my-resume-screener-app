"""
chains/cover_letter_chain.py
─────────────────────────────
LCEL chain for AI Cover Letter Generator.
Generates a tailored cover letter from resume + JD analysis.
"""

from langchain_core.runnables import RunnableLambda

from chains.llm_factory import get_llm
from prompts.cover_letter_prompt import get_cover_letter_prompt


def get_cover_letter_chain():
    """
    Build and return the cover letter LCEL chain.

    Inputs:  candidate_name, total_score, extracted_profile,
             matching_result, job_description
    Output:  str — formatted cover letter
    """
    prompt = get_cover_letter_prompt()
    llm = get_llm(temperature=0.4)

    chain = prompt | llm | RunnableLambda(lambda msg: msg.content)
    return chain
