# Create a new Python file named main.py and implement the main function

def main(issue_number):
    """
    Main function to process the issue number.
    
    :param issue_number: The issue number to process.
    :raises ValueError: If the issue number is invalid or negative.
    """
    # Add error handling for invalid or negative issue numbers
    if issue_number <= 0:
        raise ValueError("Issue number must be a positive integer.")

    # Placeholder for further processing of the issue number
    print(f"Processing issue number: {issue_number}")

# Write a simple test case to verify the error handling
if __name__ == "__main__":
    try:
        # Test with an invalid issue number
        main(-1)
    except ValueError as e:
        print(e)  # Expected output: "Issue number must be a positive integer."

    try:
        # Test with a valid issue number
        main(5)  # Expected output: "Processing issue number: 5"
    except ValueError as e:
        print(e)