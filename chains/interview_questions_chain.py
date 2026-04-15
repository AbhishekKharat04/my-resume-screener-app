"""
chains/interview_questions_chain.py
────────────────────────────────────
LCEL chain for Interview Question Predictor.
Predicts likely interview questions based on candidate analysis.
"""

from langchain_core.runnables import RunnableLambda

from chains.llm_factory import get_llm
from prompts.interview_questions_prompt import get_interview_questions_prompt


def get_interview_questions_chain():
    """
    Build and return the interview questions LCEL chain.

    Inputs:  extracted_profile, matching_result, job_description,
             total_score, grade
    Output:  str — predicted interview questions
    """
    prompt = get_interview_questions_prompt()
    llm = get_llm(temperature=0.3)

    chain = prompt | llm | RunnableLambda(lambda msg: msg.content)
    return chain
