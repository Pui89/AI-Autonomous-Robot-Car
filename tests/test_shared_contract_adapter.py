import unittest
from datetime import datetime, timezone

from pui89_car.intelligence import VehicleAdvisory, VehicleSignal
from pui89_car.shared_contract_adapter import (
    advisory_to_action_proposal,
    advisory_to_evidence_passport,
    advisories_to_world_state,
    failure_to_report,
    signal_to_observation,
)


class SharedContractAdapterTests(unittest.TestCase):
    def setUp(self):
        self.timestamp = "2026-11-13T00:00:00Z"
        self.signal = VehicleSignal(
            name="water_on_route", value=True, source="synthetic-scenario",
            observed_at=self.timestamp, evidence_ref="synthetic://car/flood-01",
        )
        self.advisory = VehicleAdvisory(
            code="water_on_route", priority="urgent_review",
            message="Water is reported on the intended route.",
            recommendation="Avoid crossing the water-covered route.",
            evidence_refs=("synthetic://car/flood-01",),
        )

    def test_signal_maps_to_observation_with_provenance(self):
        result = signal_to_observation(
            self.signal, observation_id="obs-1", modality="other",
            source_type="simulation", recorded_at=self.timestamp,
        )
        self.assertEqual(result["schema_version"], "0.1.0")
        self.assertEqual(result["source"]["source_type"], "simulation")
        self.assertEqual(result["provenance"]["dataset_or_file"], self.signal.evidence_ref)
        self.assertEqual(result["quality"]["status"], "usable")

    def test_observation_rejects_timezone_naive_timestamp(self):
        invalid = VehicleSignal(
            name="water_on_route", value=True, source="synthetic",
            observed_at="2026-11-13T00:00:00", evidence_ref="synthetic://car/naive",
        )
        with self.assertRaisesRegex(ValueError, "timezone"):
            signal_to_observation(
                invalid, observation_id="obs-invalid", modality="other",
                source_type="simulation", recorded_at=self.timestamp,
            )

    def test_observation_rejects_missing_provenance(self):
        invalid = VehicleSignal(
            name="water_on_route", value=True, source="",
            observed_at=self.timestamp, evidence_ref="",
        )
        with self.assertRaisesRegex(ValueError, "source"):
            signal_to_observation(
                invalid, observation_id="obs-invalid", modality="other",
                source_type="simulation", recorded_at=self.timestamp,
            )

    def test_observation_rejects_non_boolean_value(self):
        invalid = VehicleSignal(
            name="water_on_route", value="safe", source="synthetic",
            observed_at=self.timestamp, evidence_ref="synthetic://car/invalid",
        )
        with self.assertRaisesRegex(ValueError, "boolean"):
            signal_to_observation(
                invalid, observation_id="obs-invalid", modality="other",
                source_type="simulation", recorded_at=self.timestamp,
            )

    def test_degraded_quality_is_not_serialized_as_usable(self):
        degraded = VehicleSignal(
            name="water_on_route", value=True, source="synthetic",
            observed_at=self.timestamp, evidence_ref="synthetic://car/degraded",
            quality="degraded",
        )
        result = signal_to_observation(
            degraded, observation_id="obs-degraded", modality="other",
            source_type="simulation", recorded_at=self.timestamp,
        )
        self.assertEqual(result["quality"]["status"], "degraded")

    def test_unknown_signal_is_not_promoted_to_positive(self):
        unknown = VehicleAdvisory(
            code="water_on_route_unknown", priority="unknown",
            message="Water depth is unknown.",
            recommendation="Treat this condition as unknown.",
        )
        state = advisories_to_world_state((unknown,), state_id="state-1", updated_at=self.timestamp)
        self.assertEqual(len(state["unknowns"]), 1)
        self.assertEqual(state["evidence_refs"], [])

    def test_conflicting_signal_remains_unknown_in_world_state(self):
        conflict = VehicleAdvisory(
            code="water_on_route_conflicting", priority="unknown",
            message="Conflicting water signals.",
            recommendation="Treat this condition as unknown.",
        )
        state = advisories_to_world_state((conflict,), state_id="state-conflict", updated_at=self.timestamp)
        self.assertEqual(len(state["conflicts"]), 1)
        self.assertEqual(len(state["unknowns"]), 1)

    def test_proposal_is_never_executable(self):
        result = advisory_to_action_proposal(
            self.advisory, proposal_id="proposal-1",
            created_at=self.timestamp, world_state_ref="state-1",
        )
        self.assertEqual(result["authority"]["mode"], "advisory_only")
        self.assertIs(result["authority"]["human_approval_required"], True)
        self.assertIs(result["authority"]["execution_authorized"], False)
        self.assertNotIn("actuator_command", result)

    def test_failure_report_requires_caller_supplied_evidence(self):
        result = failure_to_report(
            failure_id="failure-1", occurred_at=self.timestamp,
            component="signal-ingestion", severity="unknown",
            summary="Input provenance missing", observed_result="Advisory withheld",
            evidence_refs=[],
        )
        self.assertEqual(result["response_status"], "open")
        self.assertEqual(result["evidence_refs"], [])

    def test_evidence_passport_keeps_review_pending_and_execution_disabled(self):
        result = advisory_to_evidence_passport(
            self.advisory, passport_id="passport-1", created_at=self.timestamp,
        )
        self.assertEqual(result["human_review"]["status"], "not_reviewed")
        self.assertEqual(result["verification"]["status"], "not_tested")
        self.assertIs(result["execution_authorized"], False)


if __name__ == "__main__":
    unittest.main()
