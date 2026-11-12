# PUI89 AI Car Architecture

**Status:** Software-only research architecture. Simulation first; no physical vehicle control or validated vehicle integration.

## Product architecture

Premium four-door hybrid utility SUV concept, four occupants, 450–520 kg occupant-inclusive payload target, flood-resilient design intent and global-market engineering objective. Hybrid subtype and chassis architecture remain open trade-study decisions. These are requirements and design targets, not demonstrated vehicle specifications.

## Intelligence pipeline

Synthetic or approved inputs -> validation -> canonical PUI89 Shared AI Core contracts -> state estimation -> hazard reasoning -> advisory safety gate -> human-facing advisory -> evidence record.

## 24-module catalogue

See [AI Car Module Catalogue](AI_CAR_MODULE_CATALOG.md) for the proposed module list and boundaries. See [Master Engineering Specification v2.0](MASTER_ENGINEERING_SPEC_V2.md) for product, chassis, hybrid, flood-resilience and validation requirements.

## Initial implemented software baseline

`pui89_car/intelligence.py` provides deterministic processing for explicit boolean vehicle signals. It:
- Requires source, evidence reference, timezone-aware timestamp, freshness and good quality.
- Represents missing, stale, invalid, conflicting and unknown inputs explicitly.
- Emits evidence-linked human-facing advisories for supported signal types.
- Advises avoidance of water-covered routes; it does not infer a safe wading depth.
- Keeps collision warnings advisory-only and does not implement automatic braking.
- Provides no vehicle actuator, ECU, CAN, steering, throttle, brake or propulsion interface.

This is a software baseline, not a perception model, vehicle diagnostic integration, certified safety function or validated vehicle system.

## Architecture rules

- Reuse the canonical shared PUI89 AI Core; do not fork it.
- Preserve units, timestamps, provenance, uncertainty and calibration state.
- Reject or flag invalid, stale, missing, contradictory or degraded critical inputs.
- Human driver retains control and responsibility.
- No actuator, steering, throttle, brake, ECU or vehicle-bus connection.
- Simulation and unit-test results do not establish road safety or physical performance.
- Record limitations and evidence for every advisory.
