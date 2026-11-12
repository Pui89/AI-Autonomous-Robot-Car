# PUI89 AI Car — 24-Module Intelligence Catalogue

**Status:** Proposed module catalogue and implementation roadmap.  
**Authority:** Advisory-only; human driver retains control.  
**Implementation truth:** Listing a module does not mean it exists or has been validated.

## Module catalogue

| ID | Module | Inputs (when available) | Advisory output | Key failure cases |
|---|---|---|---|---|
| AI-CAR-01 | Road Perception | RGB/depth/radar observations | Road/obstacle observations | Occlusion, glare, blur, stale frames |
| AI-CAR-02 | Flood Intelligence | Camera, approved water sensors, map context | Water hazard, unknown depth, route-avoidance warning | Reflection, uncertain depth, moving water |
| AI-CAR-03 | Weather Intelligence | Rain/ambient sensors, approved weather context | Rain, visibility and weather context | Missing/stale weather data |
| AI-CAR-04 | Collision Intelligence | Tracked objects and vehicle context | Potential collision-risk advisory | Incorrect motion estimate, missed object |
| AI-CAR-05 | Battery Intelligence | Validated BMS signals | Battery status/anomaly advisory | Missing, implausible or stale BMS values |
| AI-CAR-06 | Thermal Intelligence | Battery/motor/inverter/engine temperatures | Thermal anomaly advisory | Sensor drift, missing sensor |
| AI-CAR-07 | Predictive Maintenance | DTCs, service history, validated trends | Inspection recommendation | Sparse history, domain shift |
| AI-CAR-08 | Emergency Intelligence | Validated crash/event indicators | Human escalation and event summary | False event, connectivity loss |
| AI-CAR-09 | Navigation Intelligence | Approved map/route context | Route hazard and alternative context | Stale map, unavailable route |
| AI-CAR-10 | Road Memory | Time-bounded road observations | Privacy-conscious road context | Stale or mislocated memory |
| AI-CAR-11 | Driver Assistance | Approved advisories | Prioritised driver alerts | Alert fatigue, distraction |
| AI-CAR-12 | Sensor Fusion | Timestamped multi-source observations | Fused state with disagreement retained | Clock skew, calibration mismatch |
| AI-CAR-13 | 360° Surround Awareness | Surround cameras/radar/ultrasonic where available | Blind-zone/parking awareness | Occlusion, sensor obstruction |
| AI-CAR-14 | Driver Monitoring | In-cabin observations with consent | Fatigue/distraction prompt | Privacy issue, false inference |
| AI-CAR-15 | Tire Intelligence | TPMS and validated wheel data | Pressure/temperature/anomaly warning | Missing or uncalibrated readings |
| AI-CAR-16 | Vehicle Health Intelligence | Validated engine, transmission, brake, electrical and hybrid diagnostics | Whole-vehicle health summary | Incomplete diagnostic coverage |
| AI-CAR-17 | Fault Diagnosis & Recovery | Failure reports, DTCs, health state | Fault isolation and service guidance | Ambiguous cause, cascading fault |
| AI-CAR-18 | Payload Intelligence | Validated load sensors or declared load data | Load distribution/overload advisory | Unmeasured cargo, sensor error |
| AI-CAR-19 | Cybersecurity Monitoring | Approved security and integrity events | Security alert and evidence record | False positives, missing logs |
| AI-CAR-20 | Software Update Integrity | Signed package metadata and update state | Integrity/rollback status | Invalid signature, interrupted update |
| AI-CAR-21 | Occupant Safety Monitoring | Available restraint/seatbelt status | Occupant protection status | Unavailable or privacy-restricted signals |
| AI-CAR-22 | Post-Crash Assistance | Validated crash indicators and user confirmation | Emergency escalation support | False crash event, no connectivity |
| AI-CAR-23 | Global Road Context | Market-specific, licensed road-rule/map data | Regional context and rule reminders | Outdated jurisdiction data |
| AI-CAR-24 | Energy Efficiency Intelligence | Validated energy/fuel and trip context | Energy-use insights | Inaccurate consumption data |

## Common module interface

Each module should:
1. Accept versioned, typed observations only.
2. Preserve source, timestamp, units, provenance and calibration status.
3. Reject or flag missing, malformed, stale, out-of-range and conflicting inputs.
4. Return unknown when evidence is insufficient.
5. Include evidence references and limitations in every advisory.
6. Emit a FailureReport for module errors or unsafe data conditions.
7. Never issue actuator commands.
8. Be evaluated using deterministic fixtures before model-based inference is considered.

## Suggested priority

- **P0 foundation:** AI-CAR-16 Vehicle Health, AI-CAR-17 Fault Diagnosis, shared contract alignment, evidence/uncertainty and advisory safety gate.
- **P1 safety context:** AI-CAR-01 Road, AI-CAR-02 Flood, AI-CAR-03 Weather, AI-CAR-04 Collision, AI-CAR-05 Battery, AI-CAR-06 Thermal, AI-CAR-11 Driver Assistance, AI-CAR-12 Sensor Fusion, AI-CAR-15 Tire, AI-CAR-18 Payload, AI-CAR-19 Cybersecurity.
- **P2 expansion:** AI-CAR-07 Predictive Maintenance, AI-CAR-08 Emergency, AI-CAR-09 Navigation, AI-CAR-10 Road Memory, AI-CAR-13 360° Awareness, AI-CAR-14 Driver Monitoring, AI-CAR-20 Update Integrity, AI-CAR-21 Occupant Safety, AI-CAR-22 Post-Crash, AI-CAR-23 Global Road Context, AI-CAR-24 Energy Efficiency.

Priorities are sequencing recommendations, not readiness ratings.
