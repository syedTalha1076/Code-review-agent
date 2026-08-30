from src.state import CodeReviewState
from src.llm import llm


def bug_detector(state: CodeReviewState) -> CodeReviewState:

    prompt = f"""
You are a senior bug detection engineer.

Review this Pull Request and identify bugs.

CODE:
{state["code_diff"]}

CODE ANALYSIS:
{state["code_analysis"]}

Look for:

- Logic errors
- Runtime errors
- Incorrect conditions
- Edge cases
- Exception handling problems
- Data handling problems
- Null/None problems
- Incorrect API usage

For every bug provide:

Severity:
File:
Issue:
Explanation:
Suggested Fix:

Use severity:

CRITICAL
HIGH
MEDIUM
LOW

If no bugs are found, return:

No bugs found.
"""

    response = llm.invoke(prompt)

    return {
        "bugs": response.content
    }