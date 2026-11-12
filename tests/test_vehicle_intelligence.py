import unittest
from datetime import datetime, timezone

from pui89_car.intelligence import VehicleSignal, evaluate_vehicle_signals


NOW = datetime(2026, 11, 13, 12, 0, tzinfo=timezone.utc)
STAMP = "2026-11-13T12:00:00+00:00"
REQUIRED = ("water_on_route", "collision_risk")


def signal(name, value, *, timestamp=STAMP, source="synthetic-fixture", evidence="fixture:1", quality="good"):
    return VehicleSignal(name, value, source, timestamp, evidence, quality)


class VehicleIntelligenceTests(unittest.TestCase):
    def test_water_on_route_always_advises_avoidance_without_claiming_safe_depth(self):
        result = evaluate_vehicle_signals(
            [signal("water_on_route", True)],
            now=NOW,
            required_signals=REQUIRED,
        )
        flood = next(item for item in result if item.code == "water_on_route")
        self.assertEqual(flood.priority, "urgent_review")
        self.assertIn("Unknown depth", flood.recommendation)
        self.assertEqual(flood.authority, "advisory_only")
        self.assertTrue(flood.requires_human_review)

    def test_collision_risk_is_advisory_only_and_never_automatic_braking(self):
        result = evaluate_vehicle_signals(
            [signal("collision_risk", True)],
            now=NOW,
            required_signals=REQUIRED,
        )
        collision = next(item for item in result if item.code == "collision_risk")
        self.assertIn("No automatic braking", collision.recommendation)
        self.assertEqual(collision.authority, "advisory_only")

    def test_missing_required_signal_is_explicitly_unknown(self):
        result = evaluate_vehicle_signals([], now=NOW, required_signals=REQUIRED)
        self.assertEqual({item.code for item in result}, {"water_on_route_missing", "collision_risk_missing"})
        self.assertTrue(all(item.priority == "unknown" for item in result))

    def test_stale_signal_is_not_used(self):
        result = evaluate_vehicle_signals(
            [signal("water_on_route", False, timestamp="2026-11-13T11:59:00+00:00")],
            now=NOW,
            max_age_seconds=10,
            required_signals=REQUIRED,
        )
        self.assertIn("water_on_route_stale", {item.code for item in result})

    def test_timezone_naive_timestamp_is_rejected(self):
        result = evaluate_vehicle_signals(
            [signal("water_on_route", True, timestamp="2026-11-13T12:00:00")],
            now=NOW,
            required_signals=REQUIRED,
        )
        self.assertIn("water_on_route_timestamp_invalid", {item.code for item in result})

    def test_bad_quality_signal_remains_unknown(self):
        result = evaluate_vehicle_signals(
            [signal("collision_risk", True, quality="degraded")],
            now=NOW,
            required_signals=REQUIRED,
        )
        self.assertIn("collision_risk_quality_unacceptable", {item.code for item in result})

    def test_duplicate_signal_is_conflicting(self):
        result = evaluate_vehicle_signals(
            [signal("water_on_route", True), signal("water_on_route", False)],
            now=NOW,
            required_signals=REQUIRED,
        )
        self.assertIn("water_on_route_conflicting", {item.code for item in result})
        self.assertNotIn("water_on_route", {item.code for item in result})

    def test_missing_provenance_is_not_accepted(self):
        result = evaluate_vehicle_signals(
            [signal("collision_risk", True, evidence="")],
            now=NOW,
            required_signals=REQUIRED,
        )
        self.assertIn("collision_risk_provenance_missing", {item.code for item in result})

    def test_false_signal_does_not_generate_hazard_claim(self):
        result = evaluate_vehicle_signals(
            [signal("collision_risk", False), signal("water_on_route", False)],
            now=NOW,
            required_signals=REQUIRED,
        )
        self.assertFalse(any(item.code in {"collision_risk", "water_on_route"} for item in result))

    def test_output_serializes_evidence_as_json_friendly_list(self):
        result = evaluate_vehicle_signals(
            [signal("water_on_route", True)],
            now=NOW,
            required_signals=REQUIRED,
        )
        flood = next(item for item in result if item.code == "water_on_route")
        self.assertEqual(flood.to_dict()["evidence_refs"], ["fixture:1"])


if __name__ == "__main__":
    unittest.main()
