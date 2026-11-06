"""Conservative advisory-only gates for software tests."""
from datetime import datetime, timezone
from .contracts import ActionProposal, Observation

BLOCKED_WORDS = ("steer", "steering", "throttle", "accelerate", "brake", "propulsion", "ignition", "actuator")

def is_fresh(timestamp: str, max_age_seconds: int, now=None) -> bool:
    try:
        parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            return False
        current = now or datetime.now(timezone.utc)
        age = (current - parsed).total_seconds()
        return 0 <= age <= max_age_seconds
    except (TypeError, ValueError):
        return False

def validate_observation(item: Observation, max_age_seconds: int = 10) -> tuple[bool, str]:
    if not item.source.strip():
        return False, "missing_source"
    if not item.integrity_ok:
        return False, "integrity_not_verified"
    if item.quality not in {"good", "degraded"}:
        return False, "quality_not_acceptable"
    if not item.provenance.strip() or item.provenance == "unspecified":
        return False, "provenance_missing"
    if item.confidence is not None and not 0.0 <= item.confidence <= 1.0:
        return False, "confidence_out_of_range"
    if not is_fresh(item.timestamp, max_age_seconds):
        return False, "timestamp_invalid_or_stale"
    return True, "accepted_for_advisory_processing_only"

def validate_proposal(item: ActionProposal) -> tuple[bool, str]:
    if item.authority != "advisory_only":
        return False, "non_advisory_authority_rejected"
    if not item.human_approval_required:
        return False, "human_approval_required"
    if not item.evidence_refs:
        return False, "evidence_required"
    combined = (item.proposal + " " + item.rationale).lower()
    if any(word in combined for word in BLOCKED_WORDS):
        return False, "physical_vehicle_control_prohibited"
    if item.confidence is not None and not 0.0 <= item.confidence <= 1.0:
        return False, "confidence_out_of_range"
    return True, "advisory_proposal_accepted"
