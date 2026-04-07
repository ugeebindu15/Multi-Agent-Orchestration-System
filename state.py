from typing import TypedDict, Optional

class AgentState(TypedDict):
    # Input
    issue_number: int

    # Populated by Code Reader
    issue_title: str
    issue_body: str
    code_context: str

    # Populated by Planner
    plan: str
    complexity: str          # "simple" or "complex"

    # Populated by Code Writer
    patch: str

    # Populated by Test Writer
    tests: str

    # Populated by PR Opener
    pr_url: str