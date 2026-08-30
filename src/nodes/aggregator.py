from src.state import CodeReviewState
from src.llm import llm


def aggregate_findings(state: CodeReviewState) -> CodeReviewState:

    prompt = f"""
You are the lead software engineer reviewing a Pull Request.

Combine the findings from three reviewers.

========================
BUG FINDINGS
========================

{state["bugs"]}


========================
SECURITY FINDINGS
========================

{state["security_issues"]}


========================
CODE QUALITY FINDINGS
========================

{state["quality_issues"]}


Create a consolidated review.

Requirements:

1. Remove duplicate findings.
2. Do not invent new findings.
3. Prioritize security issues.
4. Organize findings by severity.

Use:

CRITICAL
HIGH
MEDIUM
LOW

For every finding include:

- Category
- Severity
- File
- Issue
- Explanation
- Recommendation
"""

    response = llm.invoke(prompt)

    return {
        "final_review": response.content
    }