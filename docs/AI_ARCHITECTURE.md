# PUI89 AI Global SUV Architecture

**Status:** Software-only research architecture. Simulation first; no physical vehicle control or validated vehicle integration.

## Product architecture

Medium-size, five-door global-market SUV concept with HEV-first powertrain research. Passenger/cargo packaging, chassis, dimensions, mass, occupant capacity and hybrid subtype remain open engineering studies. No numerical vehicle specification is approved by this architecture document.

## Intelligence pipeline

Synthetic or approved inputs -> validation -> Shared AI Core Observation -> WorldState -> advisory reasoning -> ActionProposal -> human review -> Evidence Passport / FailureReport.

## Shared AI Core interface

The vehicle adapter maps signal/advisory records to canonical Shared AI Core contracts.

- Observation preserves source, modality, timestamp, quality and provenance references.
- WorldState carries evidence references, explicit unknowns and conflicts.
- ActionProposal is advisory-only, requires human review and always sets `execution_authorized: false`.
- FailureReport records observed facts, response status and recovery context.
- Evidence Passport records missing evidence, uncertainty, safety-gate status, pending human review and verification status.

The adapter is a serialization boundary. It does not independently verify source truth, calibration, sensor measurements or physical conditions. Central schema-fixture conformance must be executed against pinned local repository checkouts before claiming integration conformance.

## Global-market context layer

Regional context is an input to requirements and advisory configuration, not a basis for silently changing safety thresholds. Record the jurisdiction, data source, version, timestamp and evidence for local road rules, weather, flood warnings, fuel/energy availability and regulatory requirements. Missing or stale context must be explicit.

## Flood-risk awareness

The software may surface documented flood exposure and recommend route avoidance. Unknown water depth, current, road condition or passability must remain unknown and trigger conservative advice. No safe wading depth, waterproofing or flood-driving capability is inferred.

## Fire and thermal awareness

The software may relay supported smoke, temperature, battery or electrical fault signals. It cannot claim complete fire detection or fire resistance. Suspected fire/smoke advisories prioritize occupant evacuation and emergency services. Physical fire containment and thermal propagation require separate engineering and testing.

## Initial software baseline

The deterministic signal-to-advisory baseline:
- Validates source, evidence reference, timezone-aware timestamp, freshness and quality.
- Represents missing, stale, invalid, conflicting and unknown inputs explicitly.
- Emits evidence-linked human-facing advisories for supported signal types.
- Advises avoidance of water-covered routes; it does not infer a safe wading depth.
- Keeps collision warnings advisory-only and does not implement automatic braking.
- Provides no actuator, ECU, CAN, steering, throttle, brake or propulsion interface.

This is not a perception model, vehicle diagnostic integration, certified safety function or validated vehicle system.

## Architecture rules

- Reuse the canonical shared PUI89 AI Core; do not fork its contracts.
- Preserve units, timestamps, provenance, uncertainty and calibration state.
- Reject or flag invalid, stale, missing, contradictory or degraded critical inputs.
- Human driver retains control and responsibility.
- No actuator, steering, throttle, brake, ECU or vehicle-bus connection.
- Simulation and unit-test results do not establish road safety or physical performance.
- Record limitations and evidence for every advisory.
