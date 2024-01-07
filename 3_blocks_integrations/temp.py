from prefect.blocks.core import Block
import requests
import datetime


class GitHubIssues(Block):
    """
    Interact with GitHub's API to get issues of a given repository.
    Get the most recently commented issue.

    Attributes:
        username (str): The username of the repository's owner.
        repo (str): The name of the repository.
        state (str): The state of the issues to return. Can be either 'open', 'closed', or 'all'. Default is 'open'.

    Examples:
        ```python
        from my_library import GitHubIssues

        github_issues_block = GitHubIssues.load("my-block-name")
        issues = github_issues_block.get_issues()
        ```
    """

    username: str
    repo: str
    state: str = "open"
    _block_type_name = "GitHub Issues"
    _block_schema_capabilities = ["get_issues", "get_most_recently_commented_issue"]
    _logo_url = "https://static.vecteezy.com/system/resources/previews/014/802/399/original/daily-flow-issues-organization-realization-flat-color-icon-icon-banner-template-free-vector.jpg"

    def _construct_url(self) -> str:
        return f"https://api.github.com/repos/{self.username}/{self.repo}/issues?state={self.state}"

    def get_issues(self) -> list:
        url = self._construct_url()
        response = requests.get(url)
        response.raise_for_status()  # Will raise an exception if the status code is not 200
        return response.json()

    def get_most_recently_commented_issue(self) -> dict:
        issues = self.get_issues()
        most_recent_issue = max(
            issues,
            key=lambda issue: datetime.fromisoformat(issue["updated_at"].rstrip("Z")),
        )
        return most_recent_issue


# from prefect import flow, task
# from prefect.blocks.system import JSON


# # my_new_block = JSON(value={"the_answer": 42})
# # my_new_block.save("taylor-pacc-json-block", overwrite=True)

# @task
# def load_block():
#     jb = JSON.load("taylor-pacc-json-block")
#     my_dict = jb.value

#     print(my_dict)


# @flow(log_prints=True)
# def load_block_flow():
#     load_block()


# if __name__ == "__main__":
#     load_block_flow()
