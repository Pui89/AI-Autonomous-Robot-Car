# PUI89 AI Car Architecture

Software-only research architecture. Simulation first; no physical vehicle control.

## Pipeline
Synthetic or approved inputs -> validation -> shared PUI89 contracts -> state estimation -> hazard reasoning -> safety supervisor -> human-facing advisory -> evidence record.

## Rules
- Reuse the canonical shared PUI89 AI Core; do not fork it.
- Reject invalid, stale, missing, or conflicting critical inputs.
- Preserve uncertainty and evidence provenance.
- Human driver retains control.
- No actuator, steering, throttle, brake, ECU, or vehicle-bus connection.
- Simulation results do not establish road safety.
