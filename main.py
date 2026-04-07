import argparse

def run_agent(issue_number: int):
    # Added error handling for invalid issue numbers
    if issue_number <= 0:
        raise ValueError("Issue number must be a positive integer.")

    # Existing code...
    print(f"\n{'='*50}")
    print(f"🤖 Multi-Agent System Starting")
    print(f"📌 Target Issue: #{issue_number}")
    print(f"{'='*50}\n")

    # Initialize the state — only issue_number is known at start
    initial_state: AgentState = {
        "issue_number": issue_number,
        # Other fields...
    }

    # Run the graph
    final_state = graph.invoke(initial_state)

    # Print results
    print(f"\n{'='*50}")
    print(f" Multi-Agent System Complete!")
    print(f"{'='*50}")
    print(f" Issue:      #{final_state['issue_number']} — {final_state['issue_title']}")
    print(f" Complexity: {final_state['complexity']}")
    print(f" PR URL:     {final_state['pr_url']}")
    print(f"{'='*50}\n")

    return final_state


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Multi-Agent GitHub Issue Fixer"
    )
    parser.add_argument(
        "--issue",
        type=int,
        required=True,
        help="GitHub issue number to fix"
    )
    args = parser.parse_args()
    run_agent(args.issue)