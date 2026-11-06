# Initial Safety Case — PUI89 AI Robot Car

**Status:** Preliminary design record only. Not a certification, safety approval, or proof of vehicle safety.

## Safety objective

The initial prototype provides software-only advisory outputs. It must not command steering, throttle, brakes, propulsion, or any physical vehicle actuator.

## Initial hazard register

| Hazard | Example cause | Initial control | Evidence required |
|---|---|---|---|
| Missed hazard | Occlusion, poor visibility, model error | State limitations; avoid claims of complete detection | Labeled scenario tests and missed-event analysis |
| False warning | Noise, reflections, poor thresholds | Prioritize alerts and track confidence | False-alarm analysis by scenario |
| Stale input | Frozen or delayed sensor data | Timestamp/freshness checks; mark state unknown | Stale-data and time-drift tests |
| Sensor disagreement | Calibration drift or conflicting sources | Preserve disagreement; do not hide conflicts | Conflict-injection tests |
| Driver distraction | Excessive or ambiguous alerts | Clear, prioritized, human-centered advisory design | Human-factors review |
| Unsafe automation | AI output treated as control command | No actuator interfaces or control authority | Architecture and interface inspection |
| Battery/electrical event | Short circuit, overheating, damaged cell | No hardware control; qualified electrical/battery engineering required | Independent analysis and controlled tests |
| Fire/water/crash hazard | Environmental or impact exposure | Physical design and materials validation required | Appropriate independent physical tests |
| Cyberattack/tampering | Malicious input, dependency compromise | Input validation, least privilege, protected changes | Security tests and audit evidence |
| Power/software failure | Power loss, restart, partial update | Conservative software failure state; no control authority | Fault-injection and recovery tests |

## Mandatory constraints

1. A human driver retains control and responsibility.
2. No direct steering, throttle, braking, ignition, or propulsion command path.
3. Missing, invalid, stale, or contradictory data must be represented explicitly.
4. Advisory outputs must retain rationale and evidence.
5. Model confidence is not proof of correctness.
6. Never claim road safety, crashworthiness, waterproofing, fire resistance, an IP rating, or regulatory compliance without suitable independent evidence.
7. Hardware integration requires qualified engineering, safety, cybersecurity, and legal review.

## Release gate

Do not describe the prototype as autonomous, road-ready, collision-proof, waterproof, fireproof, or certified. A release candidate requires documented hazards, passing regression tests, reproducible evidence, security review, and independent domain-expert assessment.
