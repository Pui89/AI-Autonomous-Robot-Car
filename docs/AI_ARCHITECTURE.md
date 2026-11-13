# PUI89 Compact Smart EV Architecture

**Status:** Software-only research architecture. Simulation first; no physical vehicle control or validated vehicle integration.

## Product architecture

Practical four-wheel compact electric crossover / mini-SUV concept. EV-oriented product direction only; dimensions, seat count, payload, battery, motor, inverter, charging, range and chassis remain open engineering decisions. No vehicle specifications or performance are demonstrated.

## Intelligence pipeline

Synthetic or approved inputs -> validation -> Shared AI Core Observation -> WorldState -> advisory reasoning -> ActionProposal -> human review -> Evidence Passport / FailureReport.

## Shared AI Core interface

The Compact Smart EV adapter in `pui89_car/shared_contract_adapter.py` maps the existing signal/advisory records to the canonical Shared AI Core v0.1.0 contract shapes. The project manifest and synthetic positive/negative fixtures are declared in `pui89-adapter.json`.

- Observation preserves source, modality, timestamp, quality and provenance references.
- WorldState carries evidence references, explicit unknowns and conflicts.
- ActionProposal is advisory-only, requires human approval and always sets `execution_authorized: false`.
- FailureReport records caller-supplied observed facts and response status.
- Evidence Passport records missing evidence, uncertainty, safety-gate status, pending human review and verification status.

The adapter is a serialization boundary. It does not independently verify source truth, calibration, sensor measurements or physical conditions. Central schema-fixture conformance has not yet been executed against pinned local repository checkouts; see [Shared AI Core Integration v0.1](SHARED_AI_CORE_INTEGRATION_V0.1.md).

## Initial implemented software baseline

`pui89_car/intelligence.py` provides deterministic processing for explicit boolean vehicle signals. It:
- Requires source, evidence reference, timezone-aware timestamp, freshness and good quality.
- Represents missing, stale, invalid, conflicting and unknown inputs explicitly.
- Emits evidence-linked human-facing advisories for supported signal types.
- Advises avoidance of water-covered routes; it does not infer a safe wading depth.
- Keeps collision warnings advisory-only and does not implement automatic braking.
- Provides no vehicle actuator, ECU, CAN, steering, throttle, brake or propulsion interface.

This is a software baseline, not a perception model, vehicle diagnostic integration, certified safety function or validated vehicle system.

## 24-module catalogue

See [Compact Smart EV Module Catalogue](AI_CAR_MODULE_CATALOG.md) for the proposed module list and boundaries. See [Master Engineering Specification v2.0](MASTER_ENGINEERING_SPEC_V2.md) for product, chassis, compact EV, packaging, energy-system and validation requirements.

## Architecture rules

- Reuse the canonical shared PUI89 AI Core; do not fork its contracts.
- Preserve units, timestamps, provenance, uncertainty and calibration state.
- Reject or flag invalid, stale, missing, contradictory or degraded critical inputs.
- Human driver retains control and responsibility.
- No actuator, steering, throttle, brake, ECU or vehicle-bus connection.
- Simulation and unit-test results do not establish road safety or physical performance.
- Record limitations and evidence for every advisory.
