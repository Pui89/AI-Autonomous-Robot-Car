# Project Plan — PUI89 Compact Smart EV

## Product definition

A future AI-enabled car assistance and robotics research platform. Begin with software, synthetic data, and simulation. This repository is not a functioning vehicle, autonomous-driving system, or road-certified product.

## Compact Smart EV design direction

- Vehicle class: practical four-wheel compact crossover / mini-SUV concept.
- Product intent: everyday usability, manageable packaging, accessible entry/exit, useful cabin and cargo layout, and space for future sensing/computing evaluation.
- Powertrain: EV-oriented concept only; battery, motor, charging and platform selection remain open research decisions.
- No fixed dimensions, seating, payload, range, water-wading, crashworthiness or production specifications are approved by this plan.
- Software-first and simulation-first; later evaluation of an existing vehicle platform requires a separate engineering, safety, cost and legal review.
- The driver remains in control. AI outputs are advisory and cannot command steering, throttle, brakes or propulsion.

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
