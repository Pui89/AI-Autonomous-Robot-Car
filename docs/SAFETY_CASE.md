# Initial Safety Case — PUI89 AI Global SUV

**Status:** Preliminary design record only. Not a certification, safety approval or proof of vehicle safety.

## Safety objective

The initial system provides software-only advisory outputs for a medium-size SUV concept. It must not command steering, throttle, brakes, propulsion, high-voltage isolation or any physical vehicle actuator.

## Initial hazard register

| Hazard | Example cause | Initial control | Evidence required |
|---|---|---|---|
| Missed road hazard | Occlusion, poor visibility, model error | State limitations; avoid complete-detection claims | Labeled scenario tests and missed-event analysis |
| False warning | Noise, reflections, poor thresholds | Prioritize alerts and track confidence | False-alarm analysis by scenario |
| Flood exposure | Incomplete map, unknown depth, fast current | Advise avoidance; unknown means do not enter | Scenario tests; physical capability not inferred |
| Stale input | Frozen or delayed sensor/data feed | Timestamp/freshness checks; mark unknown | Stale-data and time-drift tests |
| Sensor disagreement | Calibration drift or conflicting sources | Preserve disagreement; do not hide conflicts | Conflict-injection tests |
| Fire/thermal event | Smoke, overheating, battery/electrical fault | Relay supported signals; advise evacuation and emergency services | Signal coverage and false-negative analysis |
| Driver distraction | Excessive or ambiguous alerts | Clear, prioritized, human-centered advisory design | Human-factors review |
| Unsafe automation | AI output treated as control command | No actuator interfaces or control authority | Architecture and interface inspection |
| Battery/electrical event | Short circuit, damaged cell, overheating | No hardware control; qualified engineering required | Independent analysis and controlled tests |
| Global-market mismatch | Local rules, climate or service assumptions wrong | Jurisdiction-specific requirements review | Market/regulatory evidence |
| Cyberattack/tampering | Malicious input, dependency compromise | Input validation, least privilege, protected changes | Security tests and audit evidence |
| Power/software failure | Power loss, restart, partial update | Conservative software failure state; no control authority | Fault-injection and recovery tests |

## Mandatory constraints

1. Human driver retains control and responsibility.
2. No direct steering, throttle, braking, ignition, propulsion, battery-management or high-voltage isolation command path.
3. Missing, invalid, stale or contradictory data must be represented explicitly.
4. Advisory outputs must retain rationale and evidence.
5. Model confidence is not proof of correctness.
6. Never claim road safety, crashworthiness, flood wading, waterproofing, fire resistance, an IP rating, global homologation or regulatory compliance without suitable independent evidence.
7. Hardware integration requires qualified engineering, safety, cybersecurity and legal review.

## Release gate

Do not describe the concept as autonomous, road-ready, collision-proof, floodproof, fireproof or certified. A release candidate requires documented hazards, passing regression tests, reproducible evidence, security review and independent domain-expert assessment.
