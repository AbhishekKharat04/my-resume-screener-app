"""
chains/ats_improvement_chain.py
────────────────────────────────
LCEL chain for ATS Improvement Tips — Applicant Mode.

Chain: PromptTemplate | LLM | String output
Generates actionable resume optimization tips for job applicants.
Returns plain text (not JSON) since this is a human-readable report.
"""

from langchain_core.runnables import RunnableLambda

from chains.llm_factory import get_llm
from prompts.ats_improvement_prompt import get_ats_improvement_prompt


def get_ats_improvement_chain():
    """
    Build and return the ATS improvement LCEL chain.

    Inputs:  candidate_name, total_score, grade,
             extracted_profile, matching_result, score_result
    Output:  str — formatted ATS optimization report
    """
    prompt = get_ats_improvement_prompt()
    llm = get_llm(temperature=0.3)

    chain = prompt | llm | RunnableLambda(lambda msg: msg.content)
    return chain
