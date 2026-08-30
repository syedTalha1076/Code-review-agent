from src.state import CodeReviewState
from src.llm import llm


def quality_checker(state: CodeReviewState) -> CodeReviewState:

    prompt = f"""
You are a senior software architect.

Review this Pull Request for code quality.

CODE:
{state["code_diff"]}

CODE ANALYSIS:
{state["code_analysis"]}

Check:

- Readability
- Maintainability
- Naming
- Code duplication
- SOLID principles
- Error handling
- Performance
- Python best practices
- Function design
- Separation of concerns

For every issue provide:

Issue:
Explanation:
Recommendation:

If there are no major quality problems, return:

No major quality issues found.
"""

    response = llm.invoke(prompt)

    return {
        "quality_issues": response.content
    }