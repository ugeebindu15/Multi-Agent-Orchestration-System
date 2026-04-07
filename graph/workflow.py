from langgraph.graph import StateGraph, END
from state import AgentState
from agents.code_reader import code_reader_agent
from agents.planner import planner_agent
from agents.code_writer import code_writer_agent
from agents.test_writer import test_writer_agent
from agents.pr_opener import pr_opener_agent

def route_by_complexity(state: AgentState) -> str:
    """
    Conditional routing function.
    Reads complexity from state and decides next node.
    """
    if state["complexity"] == "complex":
        print("Complex issue detected — routing to deep analysis")
        return "code_writer"  # could route to research agent in future
    else:
        print("Simple issue detected — routing directly to code writer")
        return "code_writer"

def build_workflow():
    # 1. Initialize the graph with our state schema
    workflow = StateGraph(AgentState)

    # 2. Register all agents as nodes
    workflow.add_node("code_reader", code_reader_agent)
    workflow.add_node("planner", planner_agent)
    workflow.add_node("code_writer", code_writer_agent)
    workflow.add_node("test_writer", test_writer_agent)
    workflow.add_node("pr_opener", pr_opener_agent)

    # 3. Set the entry point
    workflow.set_entry_point("code_reader")

    # 4. Add edges — define the flow
    workflow.add_edge("code_reader", "planner")

    # 5. Conditional edge after planner
    workflow.add_conditional_edges(
        "planner",                    # from this node
        route_by_complexity,          # use this function to decide
        {
            "code_writer": "code_writer"   # map return value to node
        }
    )

    # 6. Linear edges for remaining agents
    workflow.add_edge("code_writer", "test_writer")
    workflow.add_edge("test_writer", "pr_opener")
    workflow.add_edge("pr_opener", END)

    # 7. Compile and return
    return workflow.compile()


# Export the compiled graph
graph = build_workflow()