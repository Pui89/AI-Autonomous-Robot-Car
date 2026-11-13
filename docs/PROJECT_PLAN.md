# Project Plan — PUI89 AI Robot Car

## Product definition

A future AI-enabled car assistance and robotics research platform. Begin with software, synthetic data, and simulation. This repository is not a functioning vehicle, autonomous-driving system, or road-certified product.

## Compact Smart Car powertrain strategy (2026–2027)

**Preferred initial study: compact full hybrid (HEV).** This is a design direction only; no vehicle, drivetrain, supplier, fuel-economy result or road validation is claimed.

1. Start with a compact, human-driver-first vehicle concept and evaluate full HEV as the preferred first powertrain.
2. Keep the PUI89 AI Core propulsion-neutral so it can support petrol-only, HEV, PHEV and BEV vehicles.
3. Use versioned, read-only vehicle-context adapters. Powertrain telemetry must not create a separate AI stack or grant physical authority.
4. Prefer full HEV over mild hybrid when meaningful electric-motor assistance is a requirement, but make any final selection using specific vehicle specifications, local serviceability, lifecycle cost and independent evidence.
5. Do not require external charging for the initial HEV concept. PHEV/BEV support remains an architectural compatibility goal, not a committed product variant.

**Safety boundary:** no ECU/CAN connection, steering, throttle, braking, propulsion, battery-management or charging control. AI outputs remain advisory and the human driver retains control.

**Next gate:** define a vendor-neutral vehicle-context schema and synthetic conformance fixtures for engine, motor, battery, fuel, energy-flow and fault-status observations. Validate units, timestamps, provenance, freshness, uncertainty and missing/conflicting data before considering any real vehicle interface.

## Fire and flood resilience — safety requirements

PUI89 should design for **early hazard awareness, avoidance, occupant protection and safe emergency response**. Do not describe the vehicle as fireproof, floodproof, amphibious or safe to drive through floodwater. These are proposed requirements; no physical protection, detection accuracy or certification is currently demonstrated.

### Flood risk
- Use available weather, road and water-depth information to warn about flood-prone routes and advise the driver to avoid flooded roads. If depth, current, road condition or route passability is unknown, show **unknown — do not enter**, not a guessed safe depth.
- Do not promise a universal safe wading depth. Actual limits depend on the exact vehicle, intake, electrical components, battery location, sealing, water flow and manufacturer guidance.
- If water rises around the vehicle, prioritize stopping only where safe, evacuation to higher ground when possible, and emergency services. Never instruct occupants to drive through moving or rising water.
- After suspected water ingress or submersion, do not restart or charge the vehicle; arrange qualified inspection and recovery. Treat hybrid high-voltage components as hazardous.
- Any future water-ingress protection target must be defined by component, exposure, duration, water conditions and a recognized test method; publish results only after independent testing.

### Fire and thermal-event risk
- Monitor only documented, supported signals for abnormal temperature, smoke/fire alerts, battery or electrical fault indications. Mark unavailable signals clearly; do not imply AI can detect every fire.
- Provide clear warnings and an emergency stop/evacuation advisory. If fire, smoke or a thermal event is suspected, occupants should leave the vehicle, move away, avoid opening a hot battery compartment or touching high-voltage parts, and call emergency services.
- Do not tell occupants to fight a vehicle or traction-battery fire. Follow emergency-service and vehicle-manufacturer guidance.
- Require professionally engineered separation, protection, venting/pressure management and thermal-event propagation assessment for any future battery or fuel-system design. No fire-containment performance is claimed.
- HEV adds both fuel-system and high-voltage hazards; safety cases must cover petrol leaks, electrical isolation, battery thermal events and post-crash response.

### AI and verification boundary
- AI is advisory only: no automatic steering, throttle, braking, propulsion, high-voltage isolation, battery-management or fire-suppression actuation.
- Unknown, stale, conflicting or failed sensor inputs must trigger an explicit uncertainty warning and conservative advice.
- Next software gate: create synthetic scenarios for rising water, unknown depth, fast-moving water, sensor loss, smoke/temperature alerts, battery faults, post-crash states and false alarms. Synthetic tests verify logic only, not physical protection.
- Physical validation requires qualified automotive/fire-safety engineering, controlled laboratory testing, applicable regulations and independent certification before any resilience claim.

## Intended capability areas

- Environmental perception and hazard awareness.
- Driver-assistance concepts with clear, prioritized human-facing warnings.
- Vehicle-health monitoring models for battery, electrical, thermal, and component anomalies.
- Road/weather/visibility context when supported by lawful, documented data.
- Predictive maintenance with evidence and uncertainty.
- Human-supervised decision support; no direct vehicle-control authority in the initial scope.

## Shared PUI89 AI Core

Reuse canonical PUI89 components and contracts; do not fork or duplicate shared infrastructure.

- `Observation`: source, timestamp, value, quality, confidence, provenance.
- `WorldState`: modeled state, freshness, uncertainty, and limitations.
- `ActionProposal`: advisory proposal, rationale, evidence, and authority boundary.
- `FailureReport`: failure mode, severity, evidence, containment, and recovery recommendation.

Cross-cutting requirements: evidence integrity, uncertainty propagation, calibration records, missing/noisy/stale/conflicting input handling, safety gates, human override, reproducible benchmarks, and clear implemented/simulated/proposed/validated labels.

## Initial software architecture

1. Synthetic input and scenario adapters.
2. Schema, range, timestamp, freshness, and provenance validation.
3. Transparent baseline state estimation.
4. Explainable hazard reasoning.
5. Safety supervisor that blocks unsupported proposals.
6. Human-facing advisory output.
7. Scenario replay, metrics, regression, and evidence reporting.

No physical vehicle, CAN bus, ECU, steering, throttle, brake, or propulsion connection is permitted in the initial phase.

## Safety and security principles

- Human driver retains control and responsibility.
- No direct actuation path from an AI model.
- Unknown, stale, invalid, or conflicting observations remain explicitly unknown or conflicting.
- Every warning must preserve rationale and supporting evidence.
- Confidence scores are not proof of correctness.
- Threat model software inputs, dependencies, credentials, unauthorized changes, and update integrity.
- Battery, electrical, thermal, fire, crashworthiness, and water-ingress requirements need qualified physical engineering and independent testing; software cannot establish resistance or certification.
- Never claim autonomous capability, collision prevention, roadworthiness, an IP rating, or regulatory compliance without suitable evidence.

## Strict zero-cost policy

Default to Git, Python standard library, synthetic fixtures, and GitHub features already available at no charge. Do not use paid APIs, subscriptions, cloud GPUs, paid datasets, or metered services. Before adding any package, model, dataset, or tool, check its license, provenance, hardware requirements, privacy terms, and potential billing triggers. Prefer no additional dependencies.

## Roadmap

### Phase 0 — foundation
- [x] Establish project scope and safety boundaries.
- [x] Document architecture and staged development.
- [ ] Align interface versions with canonical PUI89 AI Core.

### Phase 1 — software contracts
- [ ] Define typed observation, world-state, proposal, and failure-report schemas.
- [ ] Add deterministic validation and safety-gate tests.
- [ ] Test stale, missing, malformed, and conflicting inputs.

### Phase 2 — simulation and evaluation
- [ ] Build synthetic driving scenarios without real-road deployment.
- [ ] Add repeatable hazard scenario replay.
- [ ] Measure missed events, false alarms, latency, and uncertainty behavior.
- [ ] Preserve benchmark configuration and evidence artifacts.

### Phase 3 — research prototypes
- [ ] Evaluate perception methods only with legally usable, documented datasets.
- [ ] Compare against transparent baselines.
- [ ] Publish limitations and failure analysis.

### Phase 4 — independent review
- [ ] Qualified automotive, electrical, battery, cybersecurity, and functional-safety review.
- [ ] Legal and regulatory review for intended markets.
- [ ] Controlled validation before any hardware integration.

## Definition of done

A feature requires requirements, tests, traceable evidence, known limitations, security review, and documented failure behavior. Hardware and road-safety claims require appropriate independent validation.
