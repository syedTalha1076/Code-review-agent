from src.state import CodeReviewState
from src.llm import llm


def generate_report(state: CodeReviewState) -> CodeReviewState:

    prompt = f"""
Create a professional GitHub Pull Request code review.

PR TITLE:
{state["pr_title"]}

CONSOLIDATED FINDINGS:
{state["final_review"]}

Generate the final report using this structure:

# Code Review

## Summary

Briefly explain what the Pull Request does.

## Critical Issues

List critical problems.

## Bugs

List bugs.

## Security Issues

List security vulnerabilities.

## Code Quality

List code quality concerns.

## Recommended Changes

Give practical recommendations.

## Overall Verdict

Choose exactly one:

APPROVE
REQUEST CHANGES
NEEDS DISCUSSION

Important:

- Do not invent issues.
- Keep the review concise but useful.
- Explain why each important issue matters.
"""

    response = llm.invoke(prompt)

    return {
        "final_review": response.content
    }