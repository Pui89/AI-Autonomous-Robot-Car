# PUI89 AI Global SUV — Master Engineering Specification v2.0

**Status:** Proposed engineering baseline for software-first research and future qualified vehicle engineering.  
**Last updated:** 2026-11-13  
**Validation status:** Requirements and architecture only; no vehicle performance, physical integration, road testing, or certification is established.

## 1. Product direction

| Attribute | Baseline |
|---|---|
| Product | PUI89 AI Global SUV |
| Vehicle concept | Medium-size, five-door global-market SUV |
| Seating | Four occupants |
| Powertrain | HEV-first research priority; full HEV to be evaluated first, no production selection |
| Payload target | 450–520 kg, including occupants, cargo and carried equipment |
| Environmental strategy | Flood-risk awareness and route avoidance; no wading capability claimed |
| Market intent | Global, subject to regional engineering and type approval |
| Driving authority | Human driver |
| AI authority | Advisory and proposal-only |
| Development strategy | Software-first, simulation-first, low-resource and open-source-first |
| Design language | Deep Navy, Electric Cyan and Titanium Silver |

The 450–520 kg payload is an unvalidated design target, not a demonstrated rating. It must be reconciled with curb mass, GVWR, front/rear axle ratings, tire load ratings, suspension, brakes, center of gravity, occupant assumptions, cargo restraint and applicable regulations. Occupants count toward payload. Accessories and installed equipment also consume payload.

HEV-first is the research priority: evaluate full HEV first, while retaining powertrain-neutral AI compatibility for ICE, HEV, PHEV and BEV contexts. Final architecture selection remains subject to a documented vehicle- and market-specific trade study. Do not infer a chosen engine, motor, battery capacity, transmission, range, speed, fuel economy or charging capability.

## 2. Product principles

1. Safety before features; evidence before claims.
2. Human driver retains control and responsibility.
3. AI cannot command steering, throttle, braking, propulsion, gear selection or other vehicle actuators.
4. Safety-critical vehicle functions remain independently engineered and validated.
5. Unknown, missing, stale, conflicting or out-of-range data remains explicitly unknown or conflicting.
6. Every advisory carries rationale, supporting evidence, freshness and limitations.
7. Fail-aware behaviour reduces system capability when evidence quality degrades.
8. Do not represent simulation or software tests as physical vehicle validation.
9. Use open-source and zero-cost development paths where practical; no paid API, subscription, cloud GPU, metered service or automatic model download.
10. Review provenance, licence, security, privacy, maintenance and hardware needs before adopting any dependency, dataset or model.

## 3. Product requirements

### 3.1 Occupants and usability

- Four-seat packaging target with safe ingress/egress and clear occupant protection zones.
- Evaluate seat adjustability, visibility, reach, readability, climate comfort, noise and vibration.
- Design cargo storage around restraint, visibility, occupant protection, emergency exits and airbag deployment zones.
- Consider diverse body sizes, ages and accessibility needs without making unsupported safety or accessibility claims.
- Driver monitoring, where considered, must include privacy, consent, data minimisation and a non-punitive failure mode.

### 3.2 Payload and vehicle dynamics

- Treat 450–520 kg as a target for engineering study only.
- Define occupant, luggage, accessory, roof-load and towing assumptions separately.
- Calculate GVWR and axle loads from a defined curb-mass configuration.
- Validate tire load/speed ratings, wheel, suspension, chassis, brakes, thermal loads, stability and center of gravity.
- Evaluate full-load, partial-load and asymmetric-load cases.
- Do not publish a payload rating until qualified calculations and physical validation support it.

### 3.3 Chassis and body

Study unibody/monocoque and body-on-frame alternatives against mass, stiffness, durability, crash performance, packaging, repairability, cost and global use. Unibody is a study baseline, not a final selection. The chosen structure requires structural analysis, fatigue, corrosion, crash and durability validation.

Requirements include:
- Occupant-cell integrity and compatible restraint/airbag architecture.
- Suspension and subframe mounting strength.
- Brake sizing and thermal capacity for loaded operation.
- Stability under braking, cornering and uneven loading.
- Underbody protection without compromising crash structures or serviceability.
- Corrosion resistance and maintainability.

### 3.4 Hybrid powertrain

Evaluate HEV, PHEV and series hybrid using a documented weighted trade study. Compare energy efficiency over relevant duty cycles, mass, payload impact, packaging, thermal management, serviceability, supply chain, cost, emissions, regional fuel/charging availability and safety.

Requirements include:
- Engine, motor, inverter, transmission/generator and battery integration.
- Battery management, cell monitoring and thermal management.
- High-voltage isolation, overcurrent and short-circuit protection.
- Regenerative braking coordination with the independently engineered braking system.
- Diagnostics, fault containment and safe service isolation.
- Thermal propagation mitigation and post-crash electrical safety.
- No AI control path into powertrain or braking actuators.

### 3.5 Flood-resilient engineering

Flood resilience means designing for rain, splash, humidity, corrosion, drainage, water ingress detection and protected electrical enclosures. It does not mean amphibious operation or a validated wading depth.

Requirements:
- Assess battery, inverter, connectors, harnesses, engine air intake, exhaust, fuel system, cabin, sensors and low-voltage electronics.
- Define component-level ingress protection targets only after design and applicable standard review.
- Include water exposure inspection and service procedures.
- AI may report water hazards and route uncertainty; it must not declare an unknown water crossing safe.
- Advise route avoidance when water covers the road or depth/current cannot be reliably established.
- Validate any claimed water exposure limits through qualified physical tests.

### 3.6 Global-market engineering

Create a market-by-market compliance matrix before design freeze. Consider occupant protection, lighting, braking, emissions, electrical safety, cybersecurity, software updates, privacy, accessibility, environmental conditions, serviceability and local type approval. Standards listed in research material are candidates for applicability review, not a claim of compliance.

## 4. AI architecture — 24 modules

The 24-module catalogue is a roadmap, not a statement that all modules are implemented.

| ID | Module | Initial output |
|---|---|---|
| 01 | Road Perception | Evidence-linked road/obstacle observations |
| 02 | Flood Intelligence | Water-hazard and depth-uncertainty advisories |
| 03 | Weather Intelligence | Weather/visibility context |
| 04 | Collision Intelligence | Advisory collision-risk assessment |
| 05 | Battery Intelligence | BMS signal quality and anomaly advisories |
| 06 | Thermal Intelligence | Temperature anomaly advisories |
| 07 | Predictive Maintenance | Evidence-backed inspection recommendations |
| 08 | Emergency Intelligence | Event triage and human escalation |
| 09 | Navigation Intelligence | Route context and hazard alternatives |
| 10 | Road Memory | Time-bounded, privacy-conscious road observations |
| 11 | Driver Assistance | Prioritised human-facing alerts |
| 12 | Sensor Fusion | Provenance-preserving signal aggregation |
| 13 | 360° Surround Awareness | Surrounding-object and blind-zone advisories |
| 14 | Driver Monitoring | Fatigue/distraction research with privacy controls |
| 15 | Tire Intelligence | Pressure/temperature/anomaly advisories |
| 16 | Vehicle Health Intelligence | Whole-vehicle diagnostics and health summary |
| 17 | Fault Diagnosis & Recovery | Fault isolation guidance and safe degradation |
| 18 | Payload Intelligence | Load-distribution and overload-risk advisories |
| 19 | Cybersecurity Monitoring | Security-event and integrity alerts |
| 20 | Software Update Integrity | Update provenance, signature and rollback status |
| 21 | Occupant Safety Monitoring | Restraint/status information where lawfully available |
| 22 | Post-Crash Assistance | Crash-event triage and emergency escalation |
| 23 | Global Road Context | Market/region-specific road-rule context |
| 24 | Energy Efficiency Intelligence | Driver-facing energy-use insights |

Every module must use the canonical PUI89 Shared AI Core contracts: Observation, WorldState, ActionProposal and FailureReport. Do not create a competing local contract system. Any local compatibility adapter must be version-pinned and explicitly provisional.

## 5. Shared AI Core and data flow

Approved inputs -> schema/unit/time/provenance validation -> canonical Observation -> perception/state estimation -> WorldState -> hazard reasoning -> advisory ActionProposal -> independent advisory safety gate -> human-facing alert -> FailureReport/evidence record.

Required properties:
- Source identity, timestamp with timezone, units and provenance.
- Quality, freshness, calibration state and integrity.
- Uncertainty, unknowns, contradictions and limitations.
- Proposal expiry, rationale, evidence references and advisory-only authority.
- Failure mode, severity, detection evidence, containment and recovery guidance.
- Deterministic replay and regression tests.

## 6. Software implementation constraints

- Start with Python standard library and deterministic synthetic fixtures.
- CPU-only and offline-compatible by default.
- No automatic downloads, model weights, external data or network services.
- Any model integration requires a separate provenance/licence/security/resource review.
- No physical vehicle, CAN, ECU, OBD, steering, throttle, brake, propulsion or actuator connection in this phase.
- Keep tests reproducible and avoid claims based only on mocked values.

## 7. Verification and evidence gates

| Gate | Evidence |
|---|---|
| G0 Requirements | Approved product requirements, assumptions and hazard register |
| G1 Software contracts | Schema validation, provenance, uncertainty and safety-gate tests |
| G2 Deterministic simulation | Reproducible synthetic scenarios, false-alert/missed-event analysis |
| G3 Bench integration | Qualified sensor/compute bench evidence and fault injection |
| G4 Vehicle prototype | Controlled vehicle integration, measured data and safety review |
| G5 Engineering validation | Durability, crash, braking, thermal, water-ingress, cybersecurity and regulatory evidence |

No gate is presumed passed by this document. Physical vehicle validation requires qualified automotive engineering and appropriate independent assessment.

## 8. Key unresolved decisions

- HEV vs PHEV vs series hybrid.
- Unibody vs body-on-frame.
- Curb-mass and GVWR budget.
- Axle-load distribution and tire specifications.
- Battery chemistry, capacity, voltage and thermal architecture.
- Regional launch markets and applicable type-approval rules.
- Sensor suite and packaging.
- Quantified environmental operating envelope.
- Human-factors requirements and privacy model.

These decisions must be closed through evidence, calculations, trade studies and review—not assumptions.
