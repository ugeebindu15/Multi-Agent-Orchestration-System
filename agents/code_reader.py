from langchain_openai import ChatOpenAI
from github import Github
import os
from dotenv import load_dotenv
from state import AgentState

load_dotenv()

# Initialize GitHub client and LLM
gh = Github(os.getenv("GITHUB_TOKEN"))
llm = ChatOpenAI(model="gpt-4o", temperature=0)

def code_reader_agent(state: AgentState) -> AgentState:
    print(" Code Reader Agent running...")

    # 1. Fetch the GitHub issue
    repo = gh.get_repo(os.getenv("GITHUB_REPO"))
    issue = repo.get_issue(number=state["issue_number"])

    issue_title = issue.title
    issue_body = issue.body or "No description provided"

    print(f"Issue: #{state['issue_number']} — {issue_title}")

    # 2. Scan repo files and find relevant code
    relevant_code = scan_repo_for_context(repo, issue_title, issue_body)

    # 3. Write everything to shared state
    return {
        **state,
        "issue_title": issue_title,
        "issue_body": issue_body,
        "code_context": relevant_code
    }


def scan_repo_for_context(repo, issue_title: str, issue_body: str) -> str:
    """
    Scans repo files and uses LLM to identify relevant code
    based on the issue title and body.
    """
    # Collect all python files from repo
    files_content = []
    try:
        contents = repo.get_contents("")
        while contents:
            file = contents.pop(0)
            if file.type == "dir":
                contents.extend(repo.get_contents(file.path))
            elif file.name.endswith(".py") and file.size < 50000:
                code = file.decoded_content.decode("utf-8")
                files_content.append(f"### File: {file.path}\n{code}")
    except Exception as e:
        print(f"⚠️ Could not scan repo: {e}")
        return "No code context found."

    if not files_content:
        return "No Python files found in repository."

    # Combine all files
    all_code = "\n\n".join(files_content[:10])  # cap at 10 files

    # Ask LLM to extract only what's relevant
    prompt = f"""
You are a senior engineer. Given this GitHub issue:

Title: {issue_title}
Description: {issue_body}

Here is the repository code:
{all_code}

Extract ONLY the code sections most relevant to this issue.
Be concise. Return file paths and relevant code snippets only.
"""
    response = llm.invoke(prompt)
    return response.content