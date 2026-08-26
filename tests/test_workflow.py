import unittest

from hybrid_lab.workflow import HybridWorkflow


class WorkflowTest(unittest.TestCase):
    def test_routing_selects_different_paths(self):
        workflow = HybridWorkflow()
        self.assertEqual(workflow.route("출시 변경 검토"), "review")
        self.assertEqual(workflow.route("사용자 문의"), "support")
        self.assertEqual(workflow.route("안녕하세요"), "needs_input")

    def test_review_runs_parallel_roles_and_passes(self):
        result = HybridWorkflow().run("OTA 변경 검토")
        self.assertEqual({item["role"] for item in result["results"]}, {"document", "risk", "test"})
        self.assertEqual(result["evaluation"]["verdict"], "pass")
        self.assertEqual(result["required_action"], "human_review")

    def test_missing_evidence_stops_after_retry_limit(self):
        result = HybridWorkflow().run("OTA 변경 검토 증적 없음")
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["evaluation"]["verdict"], "revise")
        self.assertEqual(sum(item.startswith("evaluator=revise") for item in result["trace"]), 3)


if __name__ == "__main__":
    unittest.main()
