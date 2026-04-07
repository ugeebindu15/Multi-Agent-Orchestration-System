from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from state import AgentState

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def test_writer_agent(state: AgentState) -> AgentState:
    print(" Test Writer Agent running...")

    prompt = f"""
You are a senior software engineer writing unit tests.

A GitHub issue was fixed:

Issue Title: {state['issue_title']}
Issue Description: {state['issue_body']}

The following code fix was applied:
{state['patch']}

Your task:
Write comprehensive unit tests that verify this fix works correctly.

Rules:
- Use Python's built-in unittest framework
- Write at least 3 test cases:
    1. Happy path — fix works as expected
    2. Edge case — boundary condition
    3. Regression test — the original bug no longer occurs
- Add a comment above each test explaining what it verifies
- Format your response as:

FILE: test_fix.py
```python
<complete test code here>
```
"""

    response = llm.invoke(prompt)
    tests = response.content

    print(f" Tests generated:\n{tests[:300]}...")

    return {
        **state,
        "tests": tests
    }