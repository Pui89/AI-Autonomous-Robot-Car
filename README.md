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

## Hardware & Materials Sourcing

PUI89 uses a traceable sourcing workflow for materials, mechanical parts, sensors, compute, power and control components. See the [bilingual Hardware & Materials Sourcing guide](https://pui89.github.io/materials.html) for the process covering exact manufacturer/model identification, Thailand and international supplier discovery, country-of-origin evidence, dated pricing and availability, lead times, shipping, compatibility checks and verification gates. Product-specific candidates are added only when supported by evidence; research candidates are not purchases or validated hardware.

### Prototype materials & cost snapshot

**Planning allowance for one research prototype: ฿13,500–69,000.** This is a preliminary estimate from the [PUI89 project-specific BOM](https://pui89.github.io/materials.html#project-boms), not a supplier quotation or verified current market price.

Software-first driver-awareness research using removable, non-invasive sensors and read-only vehicle data.

| Main item | Prototype quantity | Purpose |
|---|---:|---|
| Forward RGB camera | 1 | Road observation |
| Rear/side RGB cameras | 2 | Rear and side observation |
| GNSS receiver + IMU | 1 each | Position and motion context |
| Passive OBD-II interface | 1 | Read-only vehicle data |
| Edge compute | 1 shared | Reuse shared unit first |
| Protected power, fuses and mounts | 1 set | Safe, non-invasive installation |

**Special engineering / purchase gate:** Keep the system advisory-only and non-invasive. Do not connect to steering, throttle, braking or other vehicle actuation. Confirm camera placement, driver distraction, electrical protection, vehicle warranty and legal requirements before testing.

**Shared engineering bench (tracked separately):** approximately ฿16,500–46,000 if the existing development computer is reused. This is a portfolio-level allowance for reusable compute, one RGB-D camera, bench power supply/multimeter, two microcontroller boards and reusable tools/wiring/adapters; it is not added to each project total. Allocate each shared item once, not once per product.

**Cost status:** exact manufacturer/model, manufacturing origin, supplier, stock, lead time and dated prices remain to be verified. Freight, insurance, duty, VAT, brokerage, local delivery, custom fabrication labour and certification are not priced here; calculate Thai landed cost only from dated quotations. Quantities are for one prototype; no purchase or supplier commitment is authorised. Software-first work can continue with available computing and appropriately licensed open-source tools before hardware procurement.

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

## Six Core Intelligence Groups — Product Allocation

PUI89 uses six shared intelligence groups across its seven independent products. This product allocation is a target architecture and capability map; it does not claim that every model, sensor, integration or physical function is implemented or validated.

- Vision Intelligence — image/video understanding, detection, classification, segmentation, tracking, depth and spatial cues.
- Audio Intelligence — speech recognition, sound/event perception, speaker diarisation where justified, audio-visual association, acoustic diagnostics and speech response.
- Multimodal Intelligence — context-aware fusion of vision, audio, text, video and authorised sensor/time-series data with provenance and uncertainty.
- Robotics Intelligence — robot/environment understanding, localisation, navigation, motion planning and manipulation where the product has suitable hardware.
- Action & Reaction Intelligence — task planning, bounded proposals, event response, prediction, recovery and escalation.
- Safety & Control Intelligence — independent permissions, operating limits, verification, human approval, fault handling, safe hold and emergency-stop boundaries.

### PUI89 AI Global SUV capability allocation

- **Vision:** Road users, lanes, signs, road edges, cabin occupancy and hazard cues.
- **Audio:** Cabin speech assistant, sirens/horns, alerts and acoustic vehicle diagnostics.
- **Multimodal:** Camera/radar/vehicle signals/audio/weather/navigation context fusion.
- **Robotics:** Driver-facing route, energy and hazard advisory planning only.
- **Action & Reaction:** Collision-risk, road-hazard, flood-route and vehicle-anomaly alerts.
- **Safety & Control:** Human driver retains steering/throttle/braking; advisory-only and fail-silent.

**Integration rule:** each product uses only the modules justified by its mission, data rights, hardware, compute budget and validation evidence. Model outputs remain observations or bounded proposals. Safety policy is product-specific and independent of model confidence. Unknown, stale, conflicting or out-of-scope inputs must be surfaced rather than guessed.

**Evidence status:** proposed capability allocation unless a separate implementation record, reproducible test or domain-specific validation explicitly says otherwise. Audio models, speaker diarisation, sound classifiers, VLM/VLA policies and robotics stacks require separate provenance, licence, compute, privacy and suitability review before adoption. No automatic model download or installation is authorised.

### Six-intelligence concept visual

![PUI89 AI Global SUV six-group AI architecture concept](docs/images/suv-six-intelligence-concept.svg)

*Concept diagram only: it illustrates intended software intelligence domains, not a built product, installed model stack, integrated sensor suite or validated capability.*

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
