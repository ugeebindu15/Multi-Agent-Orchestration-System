import argparse

def run_agent(issue_number: int):
    # Add error handling for invalid issue numbers
    if issue_number <= 0:
        raise ValueError("Issue number must be a positive integer greater than 0.")

    # Existing code...

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