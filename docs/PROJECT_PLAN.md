# Project Plan — PUI89 AI Global SUV

## Product definition

A software-first vehicle-intelligence research concept for a medium-size, five-door SUV intended to inform global-market requirements. Priorities are practical passenger and cargo utility, all-weather awareness, flood-risk avoidance and human-driver support. This repository is not a functioning vehicle, autonomous-driving system or road-certified product.

## Vehicle and powertrain strategy

**Vehicle class:** medium-size SUV. The project is no longer a compact/small city-car concept.

**Powertrain priority: HEV-first.** Full Hybrid (HEV) is the preferred first architecture to evaluate, subject to vehicle-specific, market-specific and engineering evidence. No supplier, production platform or final drivetrain has been selected.

1. Study full HEV first; use petrol/ICE as a benchmark and preserve PHEV/BEV compatibility.
2. Keep the PUI89 AI Core propulsion-neutral through versioned, read-only vehicle-context adapters.
3. Keep powertrain telemetry in adapters; do not create separate AI stacks for ICE, HEV, PHEV and BEV.
4. Distinguish full HEV from mild hybrid (MHEV); compare actual architecture, verified specifications, serviceability and lifecycle cost.
5. Do not claim fuel economy, emissions, performance, reliability or cost advantages without comparable independent evidence.

**Safety boundary:** no ECU/CAN connection, steering, throttle, braking, propulsion, battery-management or charging control. AI outputs remain advisory and the human driver retains control.

## Global-market requirements

Evaluate regional configurations independently. The global direction should consider:

- Climate, heat, humidity, dust, rainfall, road quality and flood exposure.
- Local homologation, crashworthiness, occupant protection and vehicle safety regulations.
- Fuel availability and quality, charging infrastructure and energy prices.
- Service network coverage, parts availability, warranty and lifecycle ownership cost.
- Passenger ergonomics, accessibility, child-seat compatibility and useful cargo packaging.
- Cybersecurity, privacy, connected-vehicle rules and data-residency requirements.

A global-market design intent is not evidence of approval in any country. No homologation, certification, launch or supplier agreement is claimed.

## Flood-risk awareness and avoidance

The AI role is early awareness, risk explanation and route avoidance—not flood wading.

- Use only documented road, weather, flood and water-level inputs with provenance and timestamps.
- Warn about known or likely flood exposure and recommend an alternate route where evidence supports it.
- If depth, current, road condition or passability is unknown, state **“unknown — do not enter”**; never invent a safe depth.
- Never advise driving through moving or rising water.
- If water ingress or submersion is suspected, advise occupants not to restart or charge the vehicle and to arrange qualified inspection and recovery.
- Physical sealing, water-ingress resistance and any wading limit require vehicle-specific engineering and independent testing. No such capability is currently demonstrated.

## Fire and thermal-event awareness

- Surface abnormal temperature, smoke/fire alerts or battery/electrical fault information only when supported by documented signals.
- Clearly mark unavailable, stale or conflicting signals; do not imply complete fire detection.
- For suspected fire or smoke, prioritize occupant evacuation, moving away from the vehicle and contacting emergency services.
- Do not instruct occupants to fight a vehicle or traction-battery fire or touch high-voltage components.
- Any future battery thermal propagation, fire containment, venting or post-crash protection claim requires qualified engineering and controlled independent testing.

## Shared PUI89 AI Core

Reuse canonical PUI89 components and contracts:

- `Observation`: source, modality, timestamp, quality, confidence and provenance.
- `WorldState`: modeled state, freshness, uncertainty and limitations.
- `ActionProposal`: advisory proposal, rationale, evidence and authority boundary.
- `FailureReport`: failure mode, severity, evidence, containment and recovery recommendation.

Cross-cutting requirements: evidence integrity, uncertainty propagation, calibration records, missing/noisy/stale/conflicting input handling, safety gates, human override, reproducible benchmarks and clear implemented/simulated/proposed/validated labels.

## Initial software architecture

1. Synthetic input and scenario adapters.
2. Schema, range, timestamp, freshness and provenance validation.
3. Transparent baseline state estimation.
4. Explainable road, weather, flood and vehicle-health reasoning.
5. Safety supervisor that blocks unsupported proposals.
6. Human-facing advisory output.
7. Scenario replay, metrics, regression and evidence reporting.

No physical vehicle, CAN bus, ECU, steering, throttle, brake or propulsion connection is permitted in the initial phase.

## Strict zero-cost policy

Default to Git, Python standard library, synthetic fixtures and GitHub features already available at no charge. Do not use paid APIs, subscriptions, cloud GPUs, paid datasets or metered services. Review licences, provenance, security, hardware requirements and billing triggers before adopting packages, models, datasets or tools. No automatic large downloads or installations.

## Roadmap

### Phase 0 — foundation
- [x] Establish software-first scope and human-control safety boundaries.
- [x] Document architecture and staged development.
- [ ] Align interface versions with canonical PUI89 AI Core.

### Phase 1 — requirements and contracts
- [ ] Define medium-size SUV user, packaging, passenger and cargo requirements.
- [ ] Define global-market requirement matrix and target-market assumptions.
- [ ] Define typed Observation, WorldState, ActionProposal and FailureReport schemas.
- [ ] Add deterministic validation and safety-gate tests.

### Phase 2 — synthetic scenarios and evaluation
- [ ] Build scenarios for flood-prone routes, unknown water depth, moving water and route diversion.
- [ ] Add smoke, thermal-event, battery-fault and post-crash advisory scenarios.
- [ ] Test sensor dropout, stale data, conflicting sources and false alarms.
- [ ] Measure missed events, false alerts, latency, uncertainty and reproducibility.

### Phase 3 — engineering studies
- [ ] Compare HEV architectures against ICE, PHEV and BEV using verified evidence.
- [ ] Study chassis, occupant packaging, cargo utility and regional requirements.
- [ ] Evaluate perception methods only with legally usable, documented datasets.

### Phase 4 — independent review
- [ ] Qualified automotive, hybrid-powertrain, battery, fire-safety and cybersecurity review.
- [ ] Legal and regulatory review for intended markets.
- [ ] Controlled validation before any hardware integration.

## Definition of done

A feature requires requirements, tests, traceable evidence, known limitations, security review and documented failure behaviour. Hardware, flood protection, fire resistance and road-safety claims require appropriate independent validation.
