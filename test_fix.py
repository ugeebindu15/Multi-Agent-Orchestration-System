import unittest
from main import run_agent

class TestRunAgent(unittest.TestCase):
    
    # Test case 1: Happy path — fix works as expected
    # This test verifies that the function does not raise an error for a valid issue number.
    def test_run_agent_with_valid_issue_number(self):
        try:
            run_agent(1)  # Valid issue number
        except ValueError:
            self.fail("run_agent() raised ValueError unexpectedly!")

    # Test case 2: Edge case — boundary condition
    # This test verifies that the function raises a ValueError for the boundary condition of issue_number = 0.
    def test_run_agent_with_zero_issue_number(self):
        with self.assertRaises(ValueError) as context:
            run_agent(0)  # Boundary condition
        self.assertEqual(str(context.exception), "Issue number must be a positive integer greater than 0.")

    # Test case 3: Regression test — the original bug no longer occurs
    # This test verifies that the function raises a ValueError for a negative issue number, which was the original bug.
    def test_run_agent_with_negative_issue_number(self):
        with self.assertRaises(ValueError) as context:
            run_agent(-1)  # Negative issue number
        self.assertEqual(str(context.exception), "Issue number must be a positive integer greater than 0.")

if __name__ == '__main__':
    unittest.main()