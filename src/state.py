from typing import TypedDict


class CodeReviewState(TypedDict):

    # User input
    pr_url: str

    # PR information
    pr_title: str
    pr_description: str
    changed_files: list
    code_diff: str

    # Analysis
    code_analysis: str

    # Specialized reviews
    bugs: str
    security_issues: str
    quality_issues: str

    # Final result
    final_review: str