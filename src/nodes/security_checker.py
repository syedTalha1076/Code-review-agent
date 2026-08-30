from src.state import CodeReviewState
from src.llm import llm


def security_checker(state: CodeReviewState) -> CodeReviewState:

    prompt = f"""
You are an expert cybersecurity engineer.

Analyze the Pull Request for security vulnerabilities.

CODE:
{state["code_diff"]}

CODE ANALYSIS:
{state["code_analysis"]}

Look for:

- SQL Injection
- Command Injection
- Authentication vulnerabilities
- Authorization vulnerabilities
- Hardcoded secrets
- API key exposure
- Sensitive data exposure
- Unsafe input handling
- Path traversal
- XSS
- Insecure dependencies
- Weak cryptography
- Improper password handling

For every issue provide:

Severity:
File:
Vulnerability:
Explanation:
Suggested Fix:

Use severity:

CRITICAL
HIGH
MEDIUM
LOW

If no security issues are found, return:

No security issues found.
"""

    response = llm.invoke(prompt)

    return {
        "security_issues": response.content
    }