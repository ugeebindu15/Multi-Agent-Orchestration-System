from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from state import AgentState

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def code_writer_agent(state: AgentState) -> AgentState:
    print("Code Writer Agent running...")

    prompt = f"""
You are an expert software engineer tasked with fixing a GitHub issue.

Issue Title: {state['issue_title']}
Issue Description: {state['issue_body']}

Relevant Code Context:
{state['code_context']}

Fix Plan:
{state['plan']}

Your task:
Write the complete fixed code based on the plan above.

Rules:
- Return ONLY the fixed code, no explanations
- Include the full file content, not just the changed lines
- Add a comment above each change explaining what was fixed
- Format your response as:

FILE: <filename>
```python
<complete fixed code here>
```

If multiple files need changes, repeat the FILE: block for each one.
"""

    response = llm.invoke(prompt)
    patch = response.content

    print(f" Patch generated:\n{patch[:300]}...")  # preview first 300 chars

    return {
        **state,
        "patch": patch
    }