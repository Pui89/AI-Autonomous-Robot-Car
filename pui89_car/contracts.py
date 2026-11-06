"""Temporary local contracts; canonical shared PUI89 AI Core remains authoritative."""
from dataclasses import dataclass, field
from typing import Any, Mapping, Optional

@dataclass(frozen=True)
class Observation:
    source: str
    timestamp: str
    value: Any
    units: Optional[str] = None
    quality: str = "unknown"
    confidence: Optional[float] = None
    provenance: str = "unspecified"
    integrity_ok: bool = False

@dataclass(frozen=True)
class WorldState:
    state: Mapping[str, Any] = field(default_factory=dict)
    uncertainty: str = "unknown"
    evidence_refs: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()

@dataclass(frozen=True)
class ActionProposal:
    proposal: str
    rationale: str
    evidence_refs: tuple[str, ...] = ()
    confidence: Optional[float] = None
    human_approval_required: bool = True
    authority: str = "advisory_only"

@dataclass(frozen=True)
class FailureReport:
    failure_mode: str
    severity: str
    evidence_refs: tuple[str, ...] = ()
    containment: str = "stop_processing_and_escalate"
    recovery_recommendation: str = "human_review_required"
