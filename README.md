# PUI89 AI Global SUV

![PUI89 AI Global SUV concept artwork — medium-size five-door SUV with advisory-only AI awareness overlays](assets/images/pui89-ai-global-suv-concept.svg)

*Concept artwork only. It is not production CAD, a selected vehicle platform, a functioning prototype, or proof of flood, fire, crash, or autonomous-driving capability.*

**Intelligent mobility. Global-market thinking. Evidence-led safety.**

PUI89 AI Global SUV is a software-first vehicle-intelligence research concept for a **medium-size, five-door SUV**. The design direction prioritizes practical passenger and cargo space, all-weather usability, global-market adaptability and risk-aware driver support. It is not a small city car.

## Product direction

| Dimension | Current direction | Evidence boundary |
|---|---|---|
| Official project name | **PUI89 AI Global SUV** | Confirmed project identity |
| Vehicle class | Medium-size SUV, five-door | Design direction; no production vehicle selected |
| Initial powertrain study | **HEV-first** (full hybrid preferred for initial evaluation) | No supplier, drivetrain or vehicle platform selected |
| AI architecture | PUI89 Shared AI Core | Software-first; advisory only |
| Market intent | Global-market requirements and regional adaptation | No market homologation or regulatory compliance claimed |
| Environment | Flood-risk awareness, route avoidance, all-weather hazard context | No flood wading, waterproofing or fire-resistance capability claimed |
| Human authority | Human driver retains control | No autonomous steering, throttle, braking or propulsion |

## HEV-first, powertrain-neutral AI

Full Hybrid (HEV) is the preferred first powertrain architecture to study. It offers electric-motor assistance without requiring routine external plug-in charging. This is a research priority, not a final drivetrain decision or a claim of fuel-economy performance.

Keep the PUI89 AI Core independent of propulsion type. Versioned, read-only vehicle-context adapters may support petrol/ICE, HEV, PHEV and BEV information without creating separate AI stacks. Compare specific vehicles and markets using verified specifications, safety ratings, service access, warranty, lifecycle cost and independent evidence. Do not treat mild hybrid (MHEV) as equivalent to full hybrid (HEV).

## Global-market engineering

The concept should be assessed against regional differences rather than assuming one configuration fits every country:

- Climate, rainfall, heat, dust, road quality and flood exposure.
- Local regulations, homologation, crash and occupant-protection requirements.
- Fuel quality and availability, charging infrastructure and energy prices.
- Service networks, spare parts, warranty support and lifecycle cost.
- Passenger ergonomics, accessibility, child-seat compatibility and cargo needs.
- Cybersecurity, privacy, data residency and connected-vehicle requirements.

No global certification, regulatory approval, supplier agreement or market launch is claimed.

## Flood-risk awareness and fire/thermal safety

The intended AI role is **awareness and avoidance**, not proving that the vehicle can drive through floodwater.

- Identify documented flood-risk context and advise route avoidance.
- If water depth, current, road condition or passability is unknown, report **“unknown — do not enter”** rather than estimating a safe depth.
- Never recommend driving through moving or rising floodwater. After suspected water ingress or submersion, do not restart or charge; arrange qualified inspection and recovery.
- Fire, smoke, battery and thermal-event information may be surfaced only when supported by documented signals. Missing signals must be shown as unavailable; no system can claim to detect every fire.
- For suspected fire or smoke, the advisory priority is occupant evacuation, moving away from the vehicle and contacting emergency services. Do not instruct occupants to fight a vehicle or traction-battery fire.
- Any future water-ingress, fire-containment, thermal-propagation or crashworthiness claim requires qualified engineering and appropriate independent physical testing.

These are design requirements and software research topics, not validated physical capabilities.

## Perception & Task Intelligence (PTI)

**Role in this product:** provide driver-centred road and vehicle-context awareness for the SUV concept. PTI is the shared PUI89 perception-and-task framework; the capabilities below are intended research and evaluation tasks, not production vehicle features.

**Priority perception tasks**
- Check camera visibility, image quality, sensor availability and observation freshness.
- Detect and classify supported road users and scene elements, including vehicles, pedestrians, cyclists, road edges, lane markings and supported signs.
- Track relevant road users and estimate relative motion or distance only when suitable calibrated inputs and evaluation evidence exist.
- Interpret supported weather, visibility, road-surface and map context while preserving unknown or conflicting information.
- Fuse authorised read-only sensor/vehicle observations with timestamps, units, provenance and uncertainty.
- Generate explainable driver advisories for potentially hazardous or uncertain situations; abstain when evidence is insufficient.

**Task flow:** OBSERVE → PERCEIVE → ASSESS → DECIDE → RESPOND → LEARN FROM EVIDENCE. The output is advisory information for a human driver. It is not a vehicle-control command.

**First evidence gate:** permission-cleared road-scene datasets, defined classes and operating context, held-out evaluation, missed/false detection analysis, uncertainty and stale-data tests, alert-usability review, and measured resource use on the intended compute target.

**Not established:** road-tested perception, production automotive capability, autonomous driving, collision prevention, automatic steering/throttle/braking, or validated flood-wading ability. The driver remains in control; no PTI actuation path is authorised. See the [shared PTI specification](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/perception/PUI89_PERCEPTION_TASK_INTELLIGENCE_V1.0.md) (maintainer repository access required).

## PUI89 Shared AI Core

Use the shared contracts and evidence boundaries:

- **Observation** — source, modality, timestamp, quality and provenance.
- **WorldState** — interpreted context, uncertainty, freshness and explicit unknowns.
- **ActionProposal** — advisory recommendation, rationale, evidence and authority boundary.
- **FailureReport** — failure mode, severity, evidence, containment and recovery information.

The AI may provide route-risk warnings, road/weather context, vehicle-health observations and explainable driver assistance. It must not command steering, throttle, braking, propulsion, high-voltage isolation or battery management.

## Development status

**Stage:** Early software and research foundation.

Existing repository materials include a deterministic signal-to-advisory baseline, initial Shared AI Core serialization adapter, synthetic contract fixtures, safety documentation and a proposed 24-module catalogue. These do not establish a functioning vehicle, validated perception model, vehicle integration, road testing or certification.

### Next engineering gates

1. Align adapter contracts with the canonical PUI89 Shared AI Core and retain conformance evidence.
2. Define medium-size SUV user, packaging, passenger, cargo and global-market requirements without presenting targets as specifications.
3. Build synthetic flood-risk, fast-moving-water, unknown-depth, smoke, thermal-event and sensor-failure scenarios.
4. Evaluate transparent baselines, false alerts, missed hazards, stale-data rejection and uncertainty behaviour.
5. Complete qualified automotive, hybrid-powertrain, battery, fire-safety, cybersecurity and regulatory reviews before any hardware integration.

## Repository map

- `docs/PROJECT_PLAN.md` — product direction and staged roadmap.
- `docs/AI_ARCHITECTURE.md` — software architecture and shared contracts.
- `docs/MASTER_ENGINEERING_SPEC_V2.md` — engineering requirements and open design decisions.
- `docs/AI_CAR_MODULE_CATALOG.md` — proposed vehicle-intelligence modules.
- `docs/SAFETY_CASE.md` — hazards, safeguards and release gates.
- `docs/THREAT_MODEL.md` and `SECURITY.md` — security risks and reporting.
- `docs/IMPLEMENTATION_STATUS.md` — implemented, missing and next work.
- `docs/AI_BENCHMARKS.md` — reproducible evaluation protocol.
- `pui89_car/` — software-only compatibility and advisory prototype.
- `tests/` — dependency-free tests and synthetic fixtures.

## Open-source-first and responsible engineering

PUI89 prioritises open-source software, transparent licensing, reproducible workflows and evidence-led collaboration. Review model, dataset, dependency and asset provenance, licences, security and hardware requirements before adoption. Do not automatically download models or install large tools. No paid APIs, metered cloud GPUs or paid subscriptions are part of the default workflow.

## Current truth and limitations

This repository is a research and software foundation. It does **not** contain a functioning SUV, selected production platform, validated drivetrain, verified sensor layout, production CAD/BOM, real-world flood or fire protection, autonomous-driving capability, road test or certified safety system. Concept art is illustrative only. All physical capabilities remain subject to engineering and independent validation.

## Project links

- [English project page](https://pui89.github.io/ai-robot-car.html)
- [Thai project page](https://pui89.github.io/ai-robot-car-th.html)
- [PUI89 portfolio](https://pui89.github.io/)
- [Website source](https://github.com/Pui89/Pui89.github.io)
- [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core)

## License

Apache License 2.0. See [LICENSE](LICENSE). Third-party images, datasets, model weights, trademarks and other assets retain their own terms and licences.

<!-- PUI89_DAILY_PROGRESS:START -->
## PUI89 project intelligence dashboard

**🟠 29% — Foundation and prototype stage** · **Evidence score:** 29/100  
**Evidence coverage:** 88% of readiness gates have non-zero credits · **Coverage-derived confidence:** High  
**Review:** 14 November 2026 05:08 (Asia/Bangkok) · **Cycle:** Daily  
**Progress:** 🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 29%

This is an evidence-weighted readiness estimate, not code completion, product certification, field validation or commercial performance. Scores do not increase with time. Credits change only after human review of traceable evidence.

| Readiness gate | Evidence credit | Visual score |
|---|---:|---|
| Purpose & requirements | 8/10 | 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜ |
| Architecture & engineering | 8/10 | 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜ |
| Working software baseline | 5/15 | 🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| Reproducible tests & evaluation | 3/15 | 🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| Integrated product prototype | 0/15 | ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| Safety & real-world validation | 1/15 | 🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| Licensing & regulatory readiness | 3/10 | 🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜ |
| Release package & support | 1/10 | 🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜ |
| **Total** | **29/100** | **🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜** |

### Monthly history (latest snapshot per month)
| Month | Score | Graph |
|---|---:|---|
| 2026-11 | 29% | 🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ |

### Shared AI Core integration
**0% verified** (0/6 integration controls). Only controls marked verified with a supporting evidence_ref count. See docs/shared-ai-core-integration.json.

### Security and repository health
🟢 No high-confidence private-key, GitHub-token or AWS-access-key patterns detected by this limited scan.

- Licence file: present
- Security policy: present
- Dependency manifests: 0 detected
- Workflow files: 3 detected
- Review details: docs/project-health-latest.json

**Next milestone:** Add traceable, reproducible evidence for: Integrated product prototype.

**Limitations:** This automated check is a first-line repository review, not a complete security audit, licence opinion, dependency vulnerability scan, branch-ruleset verification or physical safety validation. Software tests and simulations do not establish a built, certified or field-tested robot.

<!-- PUI89_DAILY_PROGRESS:END -->
