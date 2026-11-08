import json
import os
import unittest
from pathlib import Path

from pui89_car.contracts import ActionProposal, FailureReport, Observation, WorldState
from pui89_car.shared_core_v01 import build_car_v01_records

class CarSharedCoreV01Tests(unittest.TestCase):
    def make_bundle(self, failure=None):
        obs = Observation("sim-car-001", "2026-11-06T09:00:00+00:00",
                          {"object":"synthetic obstacle"}, quality="good",
                          provenance="synthetic-fixture", integrity_ok=False)
        state = WorldState({"scene":"synthetic"}, "unknown", ("sim-car-001",), ("No real sensor data.",))
        proposal = ActionProposal("Display an advisory warning for human review",
                                  "Synthetic obstacle context requires driver review.",
                                  evidence_refs=("sim-car-001",))
        return build_car_v01_records(obs, state, proposal, failure_report=failure)

    def test_maps_observation_state_and_advisory_proposal(self):
        bundle = self.make_bundle()
        self.assertEqual(bundle["observation"]["schema_version"], "0.1.0")
        self.assertEqual(bundle["observation"]["quality"]["status"], "unknown")
        self.assertEqual(bundle["world_state"]["evidence_refs"], ["sim-car-001"])
        self.assertEqual(bundle["action_proposal"]["authority"]["mode"], "advisory_only")
        self.assertIs(bundle["action_proposal"]["authority"]["execution_authorized"], False)

    def test_optional_failure_report_maps(self):
        bundle = self.make_bundle(FailureReport("stale_input", "moderate", ("sim-car-001",)))
        self.assertEqual(bundle["failure_report"]["schema_version"], "0.1.0")
        self.assertEqual(bundle["failure_report"]["severity"], "moderate")

    def test_local_safety_gate_rejects_control_proposal(self):
        obs = Observation("sim-car-002", "2026-11-06T09:00:00+00:00", {}, provenance="synthetic")
        state = WorldState()
        proposal = ActionProposal("steer left", "avoid obstacle", evidence_refs=("sim-car-002",))
        with self.assertRaises(ValueError):
            build_car_v01_records(obs, state, proposal)

    def test_shared_core_schema_required_fields_match(self):
        core_dir = os.environ.get("PUI89_SHARED_CORE_DIR")
        if not core_dir:
            self.skipTest("Shared AI Core checkout is supplied by GitHub Actions")
        schema_dir = Path(core_dir) / "schemas" / "v0.1"
        bundle = self.make_bundle(FailureReport("stale_input", "moderate", ("sim-car-001",)))
        for key, filename in (
            ("observation","observation.schema.json"),
            ("world_state","world-state.schema.json"),
            ("action_proposal","action-proposal.schema.json"),
            ("failure_report","failure-report.schema.json"),
        ):
            schema = json.loads((schema_dir / filename).read_text(encoding="utf-8"))
            self.assertEqual(schema["properties"]["schema_version"]["const"], "0.1.0")
            self.assertTrue(set(schema["required"]).issubset(bundle[key].keys()))

if __name__ == "__main__":
    unittest.main()
