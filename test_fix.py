import unittest
from main import main

class TestMainFunction(unittest.TestCase):
    
    # Test case 1: Happy path — fix works as expected
    # This test verifies that the main function processes a valid issue number correctly.
    def test_valid_issue_number(self):
        try:
            main(5)  # Expected output: "Processing issue number: 5"
        except ValueError:
            self.fail("main() raised ValueError unexpectedly!")

    # Test case 2: Edge case — boundary condition
    # This test verifies that the main function raises a ValueError for the boundary condition of issue_number = 0.
    def test_issue_number_zero(self):
        with self.assertRaises(ValueError) as context:
            main(0)
        self.assertEqual(str(context.exception), "Issue number must be a positive integer.")

    # Test case 3: Regression test — the original bug no longer occurs
    # This test verifies that the main function raises a ValueError for a negative issue number, which was the original bug.
    def test_negative_issue_number(self):
        with self.assertRaises(ValueError) as context:
            main(-1)
        self.assertEqual(str(context.exception), "Issue number must be a positive integer.")

if __name__ == '__main__':
    unittest.main()