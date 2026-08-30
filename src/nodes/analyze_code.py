from src.state import CodeReviewState
from src.llm import llm


def analyze_code(state: CodeReviewState) -> CodeReviewState:

    prompt = f"""
You are a senior software engineer.

Analyze this GitHub Pull Request.

PR TITLE:
{state["pr_title"]}

PR DESCRIPTION:
{state["pr_description"]}

CHANGED FILES:
{state["changed_files"]}

CODE DIFF:
{state["code_diff"]}

Analyze:

1. What the code is trying to do
2. Important functions
3. Potential bugs
4. Security concerns
5. Code quality concerns
6. Important edge cases

Do not invent information.
Base your analysis only on the provided code.
"""

    response = llm.invoke(prompt)

    return {
        "code_analysis": response.content
    }