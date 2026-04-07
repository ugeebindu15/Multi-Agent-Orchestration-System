from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from state import AgentState

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def planner_agent(state: AgentState) -> AgentState:
    print(" Planner Agent running...")

    prompt = f"""
You are a senior software engineer doing code planning.

A GitHub issue has been filed:

Title: {state['issue_title']}
Description: {state['issue_body']}

Relevant code from the repository:
{state['code_context']}

Your tasks:
1. Write a clear step-by-step plan to fix this issue.
2. Classify the complexity as either "simple" or "complex".

Use this criteria:
- "simple" → single file change, straightforward fix, no architectural impact
- "complex" → multiple files, logic redesign, or significant refactoring needed

Respond in this EXACT format:
COMPLEXITY: simple|complex

PLAN:
1. ...
2. ...
3. ...
"""

    response = llm.invoke(prompt)
    content = response.content

    # Parse complexity from response
    complexity = "simple"  # default
    if "COMPLEXITY: complex" in content:
        complexity = "complex"

    # Parse plan from response
    plan_start = content.find("PLAN:")
    plan = content[plan_start:].strip() if plan_start != -1 else content

    print(f" Complexity: {complexity}")
    print(f" Plan:\n{plan}")

    return {
        **state,
        "plan": plan,
        "complexity": complexity
    }