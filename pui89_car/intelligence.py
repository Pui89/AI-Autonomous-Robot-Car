"""Deterministic, software-only PUI89 vehicle advisory baseline.

This module consumes explicit boolean signals. It is not a perception model,
vehicle controller, safety-certified system, or substitute for driver judgment.
No actuator interfaces are provided.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Iterable, Optional


REQUIRED_SIGNALS = (
    "road_hazard",
    "water_on_route",
    "collision_risk",
    "battery_anomaly",
    "thermal_anomaly",
    "tire_anomaly",
    "brake_fault",
    "sensor_obstruction",
)

_SIGNAL_ADVICE = {
    "road_hazard": (
        "road_hazard_observed",
        "review",
        "A road hazard was reported by an input signal.",
        "Review the evidence and road conditions; the human driver remains responsible for the driving decision.",
    ),
    "water_on_route": (
        "water_on_route",
        "urgent_review",
        "Water is reported on the intended route.",
        "Avoid crossing the water-covered route and seek an alternative. Unknown depth or current must never be treated as safe.",
    ),
    "collision_risk": (
        "collision_risk",
        "urgent_review",
        "A potential collision-risk condition was reported.",
        "Alert the driver to assess the situation and respond using normal vehicle controls. No automatic braking is performed.",
    ),
    "battery_anomaly": (
        "battery_anomaly",
        "review",
        "A battery-system anomaly was reported.",
        "Follow the vehicle manufacturer's warning guidance and arrange qualified inspection.",
    ),
    "thermal_anomaly": (
        "thermal_anomaly",
        "urgent_review",
        "A thermal anomaly was reported by a vehicle signal.",
        "Follow the vehicle manufacturer's warning guidance, seek a safe place to stop when appropriate, and arrange qualified inspection.",
    ),
    "tire_anomaly": (
        "tire_anomaly",
        "review",
        "A tire pressure or temperature anomaly was reported.",
        "Assess the warning and tire condition safely; arrange inspection and do not assume the reading is calibrated.",
    ),
    "brake_fault": (
        "brake_system_fault",
        "urgent_review",
        "A brake-system fault was reported.",
        "Treat the vehicle warning as safety-critical and follow the manufacturer's instructions; obtain qualified service.",
    ),
    "sensor_obstruction": (
        "sensor_obstruction",
        "review",
        "A sensor obstruction or degraded sensor condition was reported.",
        "Treat affected perception outputs as unavailable until the sensor condition is checked.",
    ),
    "visibility_degraded": (
        "visibility_degraded",
        "review",
        "Reduced visibility was reported.",
        "Assess visibility and road conditions; follow applicable rules and do not rely on unavailable perception.",
    ),
    "engine_fault": (
        "engine_fault",
        "review",
        "An engine-system fault was reported.",
        "Follow the vehicle manufacturer's warning guidance and arrange qualified inspection.",
    ),
    "transmission_fault": (
        "transmission_fault",
        "review",
        "A transmission-system fault was reported.",
        "Follow the vehicle manufacturer's warning guidance and arrange qualified inspection.",
    ),
    "hybrid_system_fault": (
        "hybrid_system_fault",
        "urgent_review",
        "A hybrid-system fault was reported.",
        "Follow the vehicle manufacturer's hybrid-system safety guidance and arrange qualified service.",
    ),
    "driver_fatigue": (
        "driver_fatigue",
        "review",
        "A driver-monitoring input reported a possible fatigue condition.",
        "The driver should assess their condition and take a break when safe. This signal is advisory and may be incorrect.",
    ),
    "occupant_restraint_fault": (
        "occupant_restraint_fault",
        "urgent_review",
        "An occupant-restraint system fault was reported.",
        "Check the vehicle's restraint-system warning and arrange qualified service before relying on the system.",
    ),
    "payload_overload": (
        "payload_overload",
        "review",
        "A payload or load-distribution warning was reported.",
        "Recheck the load against the vehicle's certified limits. This software does not measure or certify payload.",
    ),
}


@dataclass(frozen=True)
class VehicleSignal:
    """One explicit, evidence-linked signal; value None means unknown."""

    name: str
    value: Optional[bool]
    source: str
    observed_at: str
    evidence_ref: str
    quality: str = "good"


@dataclass(frozen=True)
class VehicleAdvisory:
    """Human-facing advisory; never an actuator instruction."""

    code: str
    priority: str
    message: str
    recommendation: str
    evidence_refs: tuple[str, ...] = ()
    authority: str = "advisory_only"
    requires_human_review: bool = True

    def to_dict(self) -> dict:
        result = asdict(self)
        result["evidence_refs"] = list(self.evidence_refs)
        return result


def _parse_aware_timestamp(value: str) -> Optional[datetime]:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


def _unknown_advisory(code: str, message: str, evidence_refs: tuple[str, ...] = ()) -> VehicleAdvisory:
    return VehicleAdvisory(
        code=code,
        priority="unknown",
        message=message,
        recommendation="Treat this condition as unknown; do not rely on an AI conclusion and request human or qualified review.",
        evidence_refs=evidence_refs,
    )


def evaluate_vehicle_signals(
    signals: Iterable[VehicleSignal],
    *,
    now: Optional[datetime] = None,
    max_age_seconds: int = 10,
    required_signals: tuple[str, ...] = REQUIRED_SIGNALS,
) -> tuple[VehicleAdvisory, ...]:
    """Convert trusted explicit signals into deterministic advisory records.

    Signals are accepted only when they have a source, evidence reference,
    timezone-aware fresh timestamp, boolean-or-unknown value and good quality.
    Missing required signals, duplicates and invalid signals remain unknown.
    This function does not infer sensor measurements or issue vehicle commands.
    """
    if max_age_seconds < 0:
        raise ValueError("max_age_seconds must be non-negative")
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None or current.utcoffset() is None:
        raise ValueError("now must be timezone-aware")
    current = current.astimezone(timezone.utc)

    items = tuple(signals)
    counts = Counter(item.name for item in items if isinstance(item, VehicleSignal))
    by_name = {
        item.name: item
        for item in items
        if isinstance(item, VehicleSignal) and counts[item.name] == 1
    }
    advisories: list[VehicleAdvisory] = []

    for name in sorted(set(required_signals)):
        if name not in by_name and counts.get(name, 0) == 0:
            advisories.append(_unknown_advisory(
                f"{name}_missing",
                f"Required signal '{name}' was not supplied; its state is unknown.",
            ))
        elif counts.get(name, 0) > 1:
            advisories.append(_unknown_advisory(
                f"{name}_conflicting",
                f"Multiple '{name}' signals were supplied; the state is conflicting.",
            ))

    for name in sorted(by_name):
        signal = by_name[name]
        parsed = _parse_aware_timestamp(signal.observed_at)
        if not signal.source.strip() or not signal.evidence_ref.strip():
            advisories.append(_unknown_advisory(
                f"{name}_provenance_missing",
                f"Signal '{name}' has no usable source or evidence reference.",
            ))
            continue
        if parsed is None:
            advisories.append(_unknown_advisory(
                f"{name}_timestamp_invalid",
                f"Signal '{name}' has an invalid or timezone-naive timestamp.",
                (signal.evidence_ref,),
            ))
            continue
        age = (current - parsed).total_seconds()
        if age < 0 or age > max_age_seconds:
            advisories.append(_unknown_advisory(
                f"{name}_stale",
                f"Signal '{name}' is future-dated or outside the permitted freshness window.",
                (signal.evidence_ref,),
            ))
            continue
        if signal.quality != "good":
            advisories.append(_unknown_advisory(
                f"{name}_quality_unacceptable",
                f"Signal '{name}' is not marked good quality; its state is not used.",
                (signal.evidence_ref,),
            ))
            continue
        if signal.value is not None and not isinstance(signal.value, bool):
            advisories.append(_unknown_advisory(
                f"{name}_value_invalid",
                f"Signal '{name}' is not boolean or unknown.",
                (signal.evidence_ref,),
            ))
            continue
        if signal.value is None:
            advisories.append(_unknown_advisory(
                f"{name}_unknown",
                f"Signal '{name}' explicitly reports an unknown state.",
                (signal.evidence_ref,),
            ))
            continue
        if signal.value is False:
            continue
        template = _SIGNAL_ADVICE.get(name)
        if template is None:
            advisories.append(_unknown_advisory(
                f"{name}_unsupported",
                f"Signal '{name}' has no approved advisory mapping.",
                (signal.evidence_ref,),
            ))
            continue
        code, priority, message, recommendation = template
        advisories.append(VehicleAdvisory(
            code=code,
            priority=priority,
            message=message,
            recommendation=recommendation,
            evidence_refs=(signal.evidence_ref,),
        ))

    return tuple(sorted(advisories, key=lambda item: (item.priority, item.code, item.evidence_refs)))
