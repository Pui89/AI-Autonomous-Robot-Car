"""Adapter from PUI89 AI Car advisory records to Shared AI Core v0.1.0.

This module is a serialization boundary only. It does not validate external
truth, access sensors, invoke models, or authorize vehicle control.
"""
from __future__ import annotations

from typing import Any

CONTRACT_VERSION = "0.1.0"
PROJECT_ID = "pui89-ai-car"


def signal_to_observation(
    signal: Any, *, observation_id: str, modality: str,
    source_type: str, recorded_at: str,
) -> dict[str, Any]:
    """Serialize one VehicleSignal into the shared Observation vocabulary."""
    if source_type not in {"sensor", "human", "dataset", "simulation", "software", "external"}:
        raise ValueError("unsupported Shared AI Core source_type")
    if modality not in {"rgb", "depth", "thermal", "audio", "lidar", "radar", "imu", "gps", "xray", "chemical", "text", "other"}:
        raise ValueError("unsupported Shared AI Core modality")
    quality = "usable" if signal.quality == "good" else "degraded"
    return {
        "schema_version": CONTRACT_VERSION,
        "observation_id": observation_id,
        "observed_at": signal.observed_at,
        "source": {"source_id": signal.source, "source_type": source_type},
        "modality": modality,
        "payload": {"signal_name": signal.name, "value": signal.value},
        "quality": {"status": quality, "notes": "Mapped from the AI Car signal quality label; not independently calibrated."},
        "uncertainty": {"description": "Signal uncertainty is not quantified by this adapter.", "method": "not_assessed"},
        "provenance": {"recorded_at": recorded_at, "dataset_or_file": signal.evidence_ref},
    }


def advisories_to_world_state(
    advisories: tuple[Any, ...], *, state_id: str, updated_at: str,
) -> dict[str, Any]:
    """Represent advisories as a time-bounded state with explicit unknowns."""
    entities = []
    unknowns = []
    conflicts = []
    evidence_refs = set()
    for index, advisory in enumerate(advisories):
        evidence_refs.update(advisory.evidence_refs)
        is_unknown = advisory.priority == "unknown"
        entities.append({
            "entity_id": f"vehicle-advisory-{index + 1}",
            "category": "vehicle_advisory",
            "state": {
                "code": advisory.code,
                "priority": advisory.priority,
                "message": advisory.message,
                "recommendation": advisory.recommendation,
            },
            "evidence_refs": list(advisory.evidence_refs),
        })
        if is_unknown:
            unknowns.append(advisory.message)
        if "conflicting" in advisory.code:
            conflicts.append(advisory.message)
    return {
        "schema_version": CONTRACT_VERSION,
        "state_id": state_id,
        "updated_at": updated_at,
        "evidence_refs": sorted(evidence_refs),
        "entities": entities,
        "unknowns": unknowns,
        "conflicts": conflicts,
        "notes": "Advisory state only; not a vehicle-control state or validated perception result.",
    }


def advisory_to_action_proposal(
    advisory: Any, *, proposal_id: str, created_at: str, world_state_ref: str,
) -> dict[str, Any]:
    """Serialize an advisory as a non-executable human-review proposal."""
    risk = "unknown" if advisory.priority == "unknown" else (
        "high" if advisory.priority == "urgent_review" else "moderate"
    )
    return {
        "schema_version": CONTRACT_VERSION,
        "proposal_id": proposal_id,
        "created_at": created_at,
        "objective": "Present an evidence-linked vehicle advisory for human assessment.",
        "world_state_ref": world_state_ref,
        "actions": [{
            "action_id": advisory.code,
            "description": advisory.recommendation,
            "risk_level": risk,
            "preconditions": ["Human driver reviews the advisory and the original evidence."],
            "expected_effect": "Inform human judgement only; no vehicle command is generated.",
            "hazards": ["Incorrect, stale, incomplete or misleading input may produce an unsuitable advisory."],
            "evidence_refs": list(advisory.evidence_refs),
        }],
        "authority": {
            "mode": "advisory_only",
            "human_approval_required": True,
            "execution_authorized": False,
        },
        "uncertainties": ["The adapter does not independently verify source measurements or calibration."],
    }


def failure_to_report(
    *, failure_id: str, occurred_at: str, component: str, severity: str,
    summary: str, observed_result: str, evidence_refs: list[str],
    response_status: str = "open",
) -> dict[str, Any]:
    """Build an explicit shared FailureReport; callers supply observed facts."""
    return {
        "schema_version": CONTRACT_VERSION,
        "failure_id": failure_id,
        "occurred_at": occurred_at,
        "system_or_component": component,
        "severity": severity,
        "summary": summary,
        "observed_result": observed_result,
        "evidence_refs": list(evidence_refs),
        "response_status": response_status,
    }


def advisory_to_evidence_passport(
    advisory: Any, *, passport_id: str, created_at: str,
    verification_status: str = "not_tested",
) -> dict[str, Any]:
    """Create a human-reviewable Evidence Passport for one advisory."""
    status = "unknown" if advisory.priority == "unknown" else "conditional"
    return {
        "schema_version": CONTRACT_VERSION,
        "passport_id": passport_id,
        "created_at": created_at,
        "project_id": PROJECT_ID,
        "conclusion": {"statement": advisory.message, "status": status},
        "evidence": {
            "supporting_refs": list(advisory.evidence_refs),
            "conflicting_refs": [],
            "missing_items": ["Independent source verification", "Calibration evidence"],
            "provenance_status": "partial" if advisory.evidence_refs else "unknown",
        },
        "uncertainty": {
            "description": "The signal's physical truth and calibration are not independently established.",
            "assessment_method": "Deterministic adapter mapping; no probabilistic estimate.",
            "calibration_status": "not_assessed",
        },
        "safety": {
            "gate_status": "not_evaluated",
            "risk_level": "unknown" if advisory.priority == "unknown" else (
                "high" if advisory.priority == "urgent_review" else "moderate"
            ),
            "gate_notes": "Human driver remains in control; this record grants no actuation authority.",
        },
        "human_review": {"review_required": True, "status": "not_reviewed"},
        "verification": {
            "status": verification_status,
            "evidence_refs": [],
            "verification_scope": "Adapter serialization only unless separate test evidence is attached.",
        },
        "execution_authorized": False,
    }
