# Multi-Agent Orchestration System

An autonomous AI system that takes a GitHub Issue as input and automatically researches the codebase, plans a fix, writes code, writes tests, and opens a Pull Request — with zero human intervention.

## Demo

Input: GitHub Issue #1 — "Fix missing error handling in main function"

Output: [Auto-generated Pull Request](https://github.com/ugeebindu15/Multi-Agent-Orchestration-System/pull/2)

## How It Works

Five specialized AI agents collaborate through a shared state object:

| Agent | Role |
|---|---|
| Code Reader | Fetches the GitHub issue and scans the repo for relevant code |
| Planner | Writes a fix plan and decides if the issue is simple or complex |
| Code Writer | Writes the actual code fix |
| Test Writer | Writes unit tests for the fix |
| PR Opener | Creates a branch, commits the files, and opens a Pull Request |

## Tech Stack

- LangGraph — agent orchestration and stateful graph
- LangChain + GPT-4o — LLM reasoning for each agent
- PyGithub — GitHub API integration
- Python 3.11

## Run Locally
```bash
git clone https://github.com/ugeebindu15/Multi-Agent-Orchestration-System.git
cd Multi-Agent-Orchestration-System
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add your keys to `.env`:
```
OPENAI_API_KEY=your-key
GITHUB_TOKEN=your-token
GITHUB_REPO=your-username/your-repo
```

Run:
```bash
python main.py --issue 1
```

## Project Structure
```
├── agents/
│   ├── code_reader.py
│   ├── planner.py
│   ├── code_writer.py
│   ├── test_writer.py
│   └── pr_opener.py
├── graph/
│   └── workflow.py
├── state.py
└── main.py
```

## Author

Himabindu Thondamanati
MS Computer Science · Cleveland State University
Databricks Certified Associate Developer
[GitHub](https://github.com/ugeebindu15)
