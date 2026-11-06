import unittest
from datetime import datetime, timezone
from pui89_car.contracts import ActionProposal, Observation
from pui89_car.safety import is_fresh, validate_observation, validate_proposal

class SafetyTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 11, 6, 9, 0, 0, tzinfo=timezone.utc)
    def test_fresh_time(self):
        self.assertTrue(is_fresh("2026-11-06T09:00:00+00:00", 10, self.now))
    def test_old_time_rejected(self):
        self.assertFalse(is_fresh("2026-11-06T08:00:00+00:00", 10, self.now))
    def test_timezone_missing_rejected(self):
        self.assertFalse(is_fresh("2026-11-06T09:00:00", 10, self.now))
    def test_bad_time_rejected(self):
        self.assertFalse(is_fresh("not-a-time", 10, self.now))
    def test_unverified_input_rejected(self):
        item = Observation("sim", "2026-11-06T09:00:00+00:00", 1, quality="good", provenance="synthetic")
        ok, reason = validate_observation(item)
        self.assertFalse(ok)
        self.assertEqual(reason, "integrity_not_verified")
    def test_proposal_without_evidence_rejected(self):
        self.assertFalse(validate_proposal(ActionProposal("display alert", "reason"))[0])
    def test_non_advisory_authority_rejected(self):
        item = ActionProposal("display alert", "reason", evidence_refs=("x",), authority="vehicle_control")
        self.assertFalse(validate_proposal(item)[0])
    def test_physical_control_wording_rejected(self):
        item = ActionProposal("steer left", "avoid obstacle", evidence_refs=("x",))
        self.assertFalse(validate_proposal(item)[0])

if __name__ == "__main__":
    unittest.main()
