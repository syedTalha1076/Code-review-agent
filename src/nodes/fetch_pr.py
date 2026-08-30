from src.state import CodeReviewState


def fetch_pr(state: CodeReviewState) -> CodeReviewState:

    """
    Fetch Pull Request information.

    Currently using dummy data.
    Later this function will use GitHub API.
    """

    return {

        "pr_title": "Fix user login authentication",

        "pr_description": """
        This Pull Request modifies the user login
        authentication system.
        """,

        "changed_files": [
            "auth.py",
            "database.py"
        ],

        "code_diff": """
        def login(username, password):

            query = f"SELECT * FROM users WHERE username='{username}'"

            user = database.execute(query)

            if user:
                return True

            return False
        """
    }