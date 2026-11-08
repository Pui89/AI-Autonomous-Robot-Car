"""Bridge PUI89 Car local dataclasses to Shared AI Core v0.1 contracts."""
from __future__ import annotations
from datetime import datetime

from .contracts import Observation, WorldState, ActionProposal, FailureReport
from .safety import validate_proposal

SCHEMA_VERSION = "0.1.0"
MODALITIES = {"rgb", "depth", "thermal", "audio", "lidar", "radar", "imu", "gps", "xray", "chemical", "text", "other"}
SOURCE_TYPES = {"sensor", "human", "dataset", "simulation", "software", "external"}

def _timestamp(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("timestamp must be a non-empty ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp must be valid ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    return value

def build_car_v01_records(observation: Observation, world_state: WorldState,
                          proposal: ActionProposal, *, source_type="simulation",
                          modality="other", recorded_at=None,
                          failure_report: FailureReport | None = None):
    if not isinstance(observation, Observation) or not isinstance(world_state, WorldState) or not isinstance(proposal, ActionProposal):
        raise ValueError("observation, world_state and proposal must use PUI89 Car contract types")
    observed_at = _timestamp(observation.timestamp)
    recorded_at = _timestamp(recorded_at or observed_at)
    if source_type not in SOURCE_TYPES or modality not in MODALITIES:
        raise ValueError("unsupported source_type or modality")
    valid, reason = validate_proposal(proposal)
    if not valid:
        raise ValueError(f"proposal rejected by local safety gate: {reason}")
    if not proposal.evidence_refs:
        raise ValueError("proposal evidence references are required")

    quality_status = "unknown"
    if observation.integrity_ok:
        quality_status = {"good": "usable", "degraded": "degraded", "invalid": "invalid"}.get(observation.quality, "unknown")
    observation_record = {
        "schema_version": SCHEMA_VERSION,
        "observation_id": observation.source,
        "observed_at": observed_at,
        "source": {"source_id": observation.source, "source_type": source_type, "device_or_system": "PUI89 AI Car local contract"},
        "modality": modality,
        "payload": {"value": observation.value, "unit": observation.units, "provenance_label": observation.provenance},
        "quality": {"status": quality_status, "notes": "Integrity and quality are preserved from the project contract; no external sensor validation is implied."},
        "uncertainty": {"description": "Project confidence and provenance are not independently calibrated by this mapping."},
        "provenance": {"recorded_at": recorded_at, "dataset_or_file": observation.provenance},
    }
    state_record = {
        "schema_version": SCHEMA_VERSION,
        "state_id": "car-world-state:" + observation.source,
        "updated_at": recorded_at,
        "evidence_refs": list(dict.fromkeys(world_state.evidence_refs or proposal.evidence_refs)),
        "entities": [{
            "entity_id": observation.source,
            "category": "vehicle_context",
            "state": dict(world_state.state),
            "evidence_refs": list(dict.fromkeys(world_state.evidence_refs or proposal.evidence_refs)),
        }],
        "unknowns": [world_state.uncertainty] + list(world_state.limitations),
        "notes": "Software contract representation only; not vehicle-control authority.",
    }
    action_record = {
        "schema_version": SCHEMA_VERSION,
        "proposal_id": "car-advisory:" + observation.source,
        "created_at": recorded_at,
        "objective": "Present a bounded vehicle-context advisory for human review.",
        "world_state_ref": state_record["state_id"],
        "actions": [{
            "action_id": "review:" + observation.source,
            "description": proposal.proposal,
            "risk_level": "unknown",
            "preconditions": ["Review the supporting evidence and limitations.", "Keep the human driver in control."],
            "expected_effect": proposal.rationale,
            "hazards": ["Unverified observations may be stale, incomplete or incorrect."],
            "evidence_refs": list(proposal.evidence_refs),
        }],
        "authority": {"mode": "advisory_only", "human_approval_required": True, "execution_authorized": False},
        "uncertainties": list(world_state.limitations) + [world_state.uncertainty],
    }
    result = {"observation": observation_record, "world_state": state_record, "action_proposal": action_record}
    if failure_report is not None:
        if not isinstance(failure_report, FailureReport):
            raise ValueError("failure_report must use PUI89 Car FailureReport")
        severity = failure_report.severity if failure_report.severity in {"informational", "low", "moderate", "high", "critical", "unknown"} else "unknown"
        result["failure_report"] = {
            "schema_version": SCHEMA_VERSION,
            "failure_id": "car-failure:" + failure_report.failure_mode,
            "occurred_at": recorded_at,
            "system_or_component": "PUI89 AI Car software contract",
            "severity": severity,
            "summary": failure_report.failure_mode,
            "observed_result": failure_report.containment,
            "expected_result": "Fail safely and require human review.",
            "evidence_refs": list(failure_report.evidence_refs),
            "response_status": "open",
            "corrective_actions": [failure_report.recovery_recommendation],
        }
    return result
