import unittest
from pui89_car.contracts import ActionProposal, FailureReport, Observation, WorldState

class ContractTests(unittest.TestCase):
    def test_observation_defaults_unverified(self):
        item = Observation("sim", "2026-11-06T09:00:00+00:00", {"object": "car"})
        self.assertFalse(item.integrity_ok)
    def test_world_state_marks_uncertainty(self):
        self.assertEqual(WorldState().uncertainty, "unknown")
    def test_proposal_requires_human_review(self):
        item = ActionProposal("display warning", "simulated hazard", evidence_refs=("case-1",))
        self.assertTrue(item.human_approval_required)
        self.assertEqual(item.authority, "advisory_only")
    def test_failure_report_has_recovery_boundary(self):
        self.assertEqual(FailureReport("stale_input", "moderate").recovery_recommendation, "human_review_required")

if __name__ == "__main__":
    unittest.main()
