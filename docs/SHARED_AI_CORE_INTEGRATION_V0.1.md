# PUI89 Shared AI Core Integration — AI Car v0.1

**Status:** Initial adapter and synthetic contract fixtures added on a review branch. Runtime conformance against the central runner has not yet been executed.

## Pinned interface

- Shared contract schema version: `0.1.0`
- Project adapter manifest version: `0.2.0`
- Project adapter version: `0.1.0`
- Project ID: `pui89-ai-car`
- Canonical repository: [PUI89-Shared-AI-Core](https://github.com/Pui89/PUI89-Shared-AI-Core)

The adapter is intentionally dependency-free and maps the existing deterministic AI Car signal/advisory records into the five shared contract shapes: Observation, WorldState, ActionProposal, FailureReport and Evidence Passport.

## Safety boundary

- Every ActionProposal is advisory-only, requires human approval and sets `execution_authorized: false`.
- No actuator, ECU, CAN, steering, throttle, brake or propulsion interface is added.
- Unknown, conflicting or missing evidence remains explicit; the adapter does not infer water depth, road safety or sensor truth.
- The Evidence Passport remains unreviewed and unverified until actual evidence is supplied.
- The adapter does not independently validate provenance, calibration, source truth or physical conditions.

## Conformance fixtures

`pui89-adapter.json` declares one synthetic positive and one synthetic negative fixture for each of the five Shared AI Core contracts. The fixtures are deliberately labelled synthetic and contain no real vehicle or road measurements.

The central Shared AI Core v0.2 runner must be executed against exact, separately verified repository commits before claiming schema-fixture conformance. The manifest and fixtures alone do not establish a conformance pass or runtime adapter correctness.

## Verification still required

1. Run the central conformance CLI against a local checkout of both repositories and record exact verified commit SHAs.
2. Add central-validator results to CI only after the source and version pin strategy is reviewed; do not add network downloads or unpinned dependencies.
3. Expand runtime adapter tests for malformed inputs, unknown states, conflicting signals and timestamp handling.
4. Keep all vehicle outputs advisory-only; independent automotive safety engineering remains mandatory.

No physical vehicle, sensor, model, road test, paid service or external dependency is enabled by this integration.
