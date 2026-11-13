# PUI89 Compact Smart EV: Spatial Intelligence integration profile

This project now has a project-specific spatial integration profile at
`INTEGRATION_PROFILE.json`.

## Intended use
Advisory road-scene geometry, obstacle-relative position and scene-change evidence.

## Planned tasks
- 3D obstacle position and approximate dimensions
- Road-scene geometry and temporal change (after timestamps are validated)
- Spatial evidence references for human review

## Safety boundaries
- No road-boundary inference or collision prediction is implemented.
- No braking, steering, throttle or autonomous driving authority.
- Vehicle dynamics, weather, calibration and road testing remain unvalidated.

## Shared implementation dependency
The common software interfaces are being developed in the
[PUI89 Shared AI Core Spatial Intelligence PR #26](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/26).
That pull request is still a draft and has not been merged. This file records
the project-specific integration contract; it does not mean the project
currently imports or executes the shared spatial module.

Before runtime integration, require lawful sensor/data provenance, calibrated
coordinate frames, synchronized timestamps, sensor-health checks, uncertainty
handling, synthetic fault tests and project-specific human-review gates.
No physical actuation is enabled.

**Current evidence status:** profile documentation added; runtime adapter,
real sensor integration, accuracy, field performance and safety validation
remain pending. No hardware or paid service is required for this documentation
stage.
