# PUI89 Shared AI Core Integration — AI Car v0.1

**Status:** Adapter and synthetic fixtures are implemented on a review branch. Central schema-fixture conformance passed for the exact project and core commit pins recorded below. Runtime adapter tests are included in the project test suite; their GitHub Actions result must be checked separately.

## Pinned interface

- Shared contract schema version: `0.1.0`
- Project adapter manifest version: `0.2.0`
- Project adapter version: `0.1.0`
- Project ID: `pui89-ai-car`
- Canonical repository: [PUI89-Shared-AI-Core](https://github.com/Pui89/PUI89-Shared-AI-Core)
- Conformance runner: `pui89-core-conformance-cli` v`0.1.0`
- Shared AI Core source pin: `cb5fdecb12acf4d810522b6a1c86567996b99718`
- AI Car source pin checked: `47bcf06d4200bd1cba4e7fd49048e658b1b01810`

The adapter maps deterministic AI Car signal/advisory records into Observation, WorldState, ActionProposal, FailureReport and Evidence Passport. It is a serialization boundary, not a perception system or vehicle controller.

## Conformance result

**Passed — 10/10 synthetic fixtures:** five positive fixtures were accepted and five negative fixtures were correctly rejected by the central Shared AI Core v0.2 conformance CLI using the pinned v0.1.0 schemas.

The machine-readable report is retained at [reports/shared-core-conformance-2026-11-13.json](../reports/shared-core-conformance-2026-11-13.json).

The CLI records commit pins as caller-declared values; it does not independently inspect Git metadata. The repository references above were separately checked against the GitHub PR head and Shared AI Core commit before execution.

This is **schema-fixture conformance only**. It does not prove semantic correctness, runtime adapter behaviour, external evidence truth, sensor calibration, model quality, or physical safety. The CLI report therefore correctly sets `runtime_adapter_tested: false`.

## Runtime adapter safeguards

- Observation serialization rejects empty source/evidence references, invalid or timezone-naive timestamps, non-boolean values and unsupported quality labels.
- Signal quality is mapped explicitly: good → usable; degraded → degraded; invalid → invalid; unknown → unknown.
- Unknown and conflicting signal states remain explicit in WorldState.
- Every ActionProposal is advisory-only, requires human approval and sets `execution_authorized: false`.
- The Evidence Passport remains unreviewed and unverified until actual evidence is supplied.

Runtime tests cover malformed provenance, timestamps, values, degraded quality, unknown/conflicting states, failure reporting and disabled execution. GitHub Actions status is the source of truth for whether those tests passed on the current PR head.

## Safety boundary

- No actuator, ECU, CAN, steering, throttle, brake or propulsion interface is added.
- Unknown, conflicting or missing evidence is never converted into a safe road or flood assessment.
- The adapter does not independently verify source truth, sensor calibration or physical conditions.
- No autonomous-driving or physical performance claims are made.
- Hybrid subtype, chassis architecture, GVWR/GAWR, curb mass, validated payload and flood/wading limits remain unresolved or unvalidated.

No physical vehicle, sensor, model, road test, paid service or new external dependency is enabled by this integration.
