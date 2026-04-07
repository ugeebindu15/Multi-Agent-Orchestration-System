from github import Github, GithubException
from dotenv import load_dotenv
from state import AgentState
import os
import re
import base64

load_dotenv()

gh = Github(os.getenv("GITHUB_TOKEN"))

def pr_opener_agent(state: AgentState) -> AgentState:
    print("🚀 PR Opener Agent running...")

    repo = gh.get_repo(os.getenv("GITHUB_REPO"))

    # 1. Create a new branch from main
    branch_name = f"fix/issue-{state['issue_number']}-auto"
    main_branch = repo.get_branch("main")

    try:
        repo.create_git_ref(
            ref=f"refs/heads/{branch_name}",
            sha=main_branch.commit.sha
        )
        print(f" Created branch: {branch_name}")
    except GithubException as e:
        print(f"⚠️ Branch may already exist: {e}")

    # 2. Commit the patch file
    patch_filename, patch_code = extract_file_content(state["patch"])
    commit_file(repo, branch_name, patch_filename, patch_code,
                f"fix: auto-fix for issue #{state['issue_number']}")

    # 3. Commit the test file
    test_filename, test_code = extract_file_content(state["tests"])
    commit_file(repo, branch_name, test_filename, test_code,
                f"test: add tests for issue #{state['issue_number']} fix")

    # 4. Open the Pull Request
    pr = repo.create_pull(
        title=f"[Auto-Fix] {state['issue_title']}",
        body=build_pr_body(state),
        head=branch_name,
        base="main"
    )

    print(f" Pull Request opened: {pr.html_url}")

    return {
        **state,
        "pr_url": pr.html_url
    }


def extract_file_content(agent_output: str) -> tuple[str, str]:
    """
    Extracts filename and code from agent output.
    Expected format:
    FILE: filename.py
```python
    <code>
```
    """
    # Extract filename
    filename_match = re.search(r"FILE:\s*(\S+)", agent_output)
    filename = filename_match.group(1) if filename_match else "fix.py"

    # Extract code block
    code_match = re.search(r"```python\n(.*?)```", agent_output, re.DOTALL)
    code = code_match.group(1).strip() if code_match else agent_output

    return filename, code


def commit_file(repo, branch: str, filename: str,
                content: str, message: str):
    """
    Creates or updates a file in the repo on the given branch.
    """
    try:
        # Check if file already exists
        existing = repo.get_contents(filename, ref=branch)
        repo.update_file(
            path=filename,
            message=message,
            content=content,
            sha=existing.sha,
            branch=branch
        )
        print(f" Updated: {filename}")
    except GithubException:
        # File doesn't exist yet — create it
        repo.create_file(
            path=filename,
            message=message,
            content=content,
            branch=branch
        )
        print(f" Created: {filename}")


def build_pr_body(state: AgentState) -> str:
    """
    Builds a clean, professional PR description.
    """
    return f"""
##  Auto-Generated Fix

**Closes #{state['issue_number']}**

### Issue
{state['issue_title']}

{state['issue_body']}

### Fix Plan
{state['plan']}

### Changes
- Applied code fix based on issue analysis
- Added unit tests covering happy path, edge case, and regression

---
*This PR was generated automatically by the Multi-Agent Orchestration System*
"""