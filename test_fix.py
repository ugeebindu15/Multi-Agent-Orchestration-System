import unittest
from main import run_agent

class TestRunAgent(unittest.TestCase):

    def setUp(self):
        # Mocking the graph.invoke function to return a predictable result
        self.original_graph_invoke = graph.invoke
        graph.invoke = lambda state: {
            "issue_number": state["issue_number"],
            "issue_title": "Sample Issue Title",
            "complexity": "Medium",
            "pr_url": "http://example.com/pr/123"
        }

    def tearDown(self):
        # Restore the original graph.invoke function
        graph.invoke = self.original_graph_invoke

    # Test case 1: Happy path — fix works as expected
    def test_run_agent_with_valid_issue_number(self):
        """Test that run_agent works correctly with a valid issue number."""
        issue_number = 42
        final_state = run_agent(issue_number)
        self.assertEqual(final_state["issue_number"], issue_number)
        self.assertEqual(final_state["issue_title"], "Sample Issue Title")
        self.assertEqual(final_state["complexity"], "Medium")
        self.assertEqual(final_state["pr_url"], "http://example.com/pr/123")

    # Test case 2: Edge case — boundary condition
    def test_run_agent_with_issue_number_one(self):
        """Test that run_agent works correctly with the smallest valid issue number."""
        issue_number = 1
        final_state = run_agent(issue_number)
        self.assertEqual(final_state["issue_number"], issue_number)
        self.assertEqual(final_state["issue_title"], "Sample Issue Title")
        self.assertEqual(final_state["complexity"], "Medium")
        self.assertEqual(final_state["pr_url"], "http://example.com/pr/123")

    # Test case 3: Regression test — the original bug no longer occurs
    def test_run_agent_with_invalid_issue_number(self):
        """Test that run_agent raises ValueError for invalid issue numbers."""
        with self.assertRaises(ValueError) as context:
            run_agent(0)
        self.assertEqual(str(context.exception), "Issue number must be a positive integer.")

        with self.assertRaises(ValueError) as context:
            run_agent(-5)
        self.assertEqual(str(context.exception), "Issue number must be a positive integer.")

if __name__ == '__main__':
    unittest.main()