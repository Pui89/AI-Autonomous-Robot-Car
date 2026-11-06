# PUI89 AI Robot Car

![PUI89 AI Car — Vehicle Intelligence Concept](docs/images/pui89-ai-car-concept.svg)

**Repository:** `Pui89/ai-robot-car`  
**Project type:** Advanced AI-enabled vehicle intelligence and robotics research; software-first, simulation-first.  
**Status:** Early-stage software scaffold. Not a built, road-tested, autonomous, or road-certified vehicle.

## Design concept

The concept uses a premium electric crossover form in PUI89 deep navy and electric cyan. The illustrative sensor layout communicates a future perception envelope (camera, radar, lidar and proximity sensing), while the software architecture remains human-driver-first: AI produces evidence-linked advisories, not steering, throttle or braking commands.

**The artwork is a design visualization, not a production CAD model, bill of materials, verified sensor layout, built prototype, or performance claim.** Sensor selection and physical packaging remain future engineering work.

## Mission

Develop a safety-first vehicle intelligence platform for environmental awareness, hazard detection, vehicle-health monitoring, predictive maintenance, and explainable driver assistance. A human driver remains responsible for vehicle control. This repository has no physical vehicle integration or actuator authority.

## PUI89 engineering rules

- **Strict zero-cost:** no paid APIs, subscriptions, cloud GPUs, paid datasets, metered services, or unexpected billing.
- **Simulation first:** no physical vehicle, ECU, vehicle-bus or actuator connections.
- **Safety before features:** uncertainty, human review, conservative failure handling and hazard analysis are mandatory.
- **Evidence before claims:** distinguish proposed, implemented, simulation-tested, bench-tested and independently validated capabilities.
- **Shared AI Core:** reuse canonical PUI89 contracts and services; local compatibility types are temporary and must not become a competing core.
- **Security by default:** least privilege, dependency/provenance review, protected changes and no secrets in source.
- **No unsupported autonomous-driving, roadworthiness, waterproofing, fire-resistance or safety claims.**

## Capability research areas

1. Environmental perception and hazard-awareness research.
2. Human-facing driver-assistance concepts.
3. Vehicle-health and predictive-maintenance research.
4. Road, weather and visibility context using documented lawful data or simulation.
5. Agentic analysis with evidence and human oversight.
6. SHIELD risk monitoring, stale-data handling and conservative degradation.

## Working concept architecture

`Observation → WorldState → Hazard Analysis → Safety Gate → Human-facing Advisory → Evidence Record`

- Inputs must preserve source, timestamp, quality, confidence, provenance and freshness.
- Missing, stale, conflicting or out-of-range inputs must not be silently treated as facts.
- Uncertainty must propagate to the advisory output.
- Every advisory should carry its rationale, evidence references, limitations and escalation path.
- The AI layer has no direct authority over steering, throttle, braking or propulsion.

## Development stages

1. Define requirements, hazards, operating boundaries and shared AI Core interfaces.
2. Build software-only contracts and deterministic safety gates.
3. Create synthetic scenarios and simulation adapters.
4. Add evaluation, robustness, security and regression tests.
5. Consider hardware only after qualified engineering, safety, cybersecurity and legal review.

## Repository map

- `docs/PROJECT_PLAN.md` — scope and staged roadmap.
- `docs/AI_ARCHITECTURE.md` — software architecture and data flow.
- `docs/AGENTIC_AI_SYSTEM.md` — agent roles and authority boundaries.
- `docs/UNIVERSAL_SHIELD.md` — cross-project safety and resilience standard.
- `docs/AUTONOMOUS_SIMULATION.md` — simulation-only research plan.
- `docs/PREDICTIVE_MAINTENANCE.md` — health and maintenance research.
- `docs/SAFETY_CASE.md` — hazards and safeguards.
- `docs/THREAT_MODEL.md` and `SECURITY.md` — security risks and reporting.
- `docs/AI_BENCHMARKS.md` — reproducible evaluation protocol.
- `docs/IMPLEMENTATION_STATUS.md` — implemented, missing and next work.
- `pui89_car/` — dependency-free local compatibility prototype and safety gates.
- `tests/` — standard-library unit tests.
- `.github/workflows/quality.yml` — automated documentation, test and compile checks.

## Free AI and advanced engineering resources

See [PUI89 Free AI & Advanced Engineering Stack](docs/FREE_AI_TECH_STACK.md). Every tool, model, dataset and hosted feature requires exact licence, provenance, hardware and cost review before adoption. Free software does not guarantee free model weights, compute, datasets or commercial rights.

## Current truth

This repository contains research documentation and an initial software-only contract/safety prototype. It does not contain a functioning car, validated perception model, real-time vehicle integration, autonomous driving capability, or certified safety system. The local contract types are provisional until aligned with the canonical shared PUI89 AI Core.

## PUI89 portfolio links

- **English project page:** [PUI89 AI Car](https://pui89.github.io/ai-robot-car.html)
- **Thai project page:** [PUI89 AI Car — ภาษาไทย](https://pui89.github.io/ai-robot-car-th.html)
- **PUI89 main portfolio:** [https://pui89.github.io/](https://pui89.github.io/)
- **Website source repository:** [Pui89/Pui89.github.io](https://github.com/Pui89/Pui89.github.io)
- **Motorcycle companion project:** [PUI89 AI Robot Motorcycle — EasyRide](https://github.com/Pui89/ai-robot-motorcycle)

## Hugging Face model candidates — Non-Chinese origin only

**PUI89 mandatory rule:** use only models with verified non-Chinese developer and checkpoint provenance. Unknown or unclear origin means exclude. This section is a candidate list only; no weights have been downloaded, installed, or evaluated.

| Candidate checkpoint | Research role | Status |
|---|---|---|
| [google/siglip2-base-patch16-224](https://huggingface.co/google/siglip2-base-patch16-224) | Road-scene image/text similarity research | CANDIDATE — review required |
| [facebook/dinov2-base](https://huggingface.co/facebook/dinov2-base) | Visual feature extraction for scene and change comparison | CANDIDATE — review required |
| [microsoft/Florence-2-base](https://huggingface.co/microsoft/Florence-2-base) | Offline scene description, OCR and candidate object localization | CANDIDATE — review required |
| [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) | Optional multilingual voice-interface transcription | CANDIDATE — review required |

Research/advisory perception only. These general-purpose models are not automotive-grade road perception and must not control steering, throttle, braking, propulsion or vehicle systems.

**Adoption gates:** verify the exact checkpoint's developer, origin, immutable revision, model-card and file licence, training-data disclosures, code/dependency security, file format, hardware fit and total cost before any download or execution. No paid APIs, hosted inference, cloud GPUs, automatic downloads or direct physical control. Florence-2 requires extra source review because its documented loader uses trust_remote_code=True. All models remain research-only until independently evaluated and approved.

**Shared policy:** [PUI89 Hugging Face Model Policy](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_HUGGINGFACE_MODEL_POLICY.md).

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file.

Unless a file or component states otherwise, the Apache-2.0 licence applies to the original project materials in this repository. Third-party datasets, model weights, images, trademarks and other externally sourced assets retain their own licences and terms; check their provenance before use or redistribution.

Copyright 2026 Pui89.

## Robotics foundation model candidates — Non-Chinese origin only

### Shortlisted candidate: SmolVLA

- Checkpoint: [`lerobot/smolvla_base`](https://huggingface.co/lerobot/smolvla_base)
- Publisher/developer: Hugging Face / LeRobot
- Model-card licence: Apache-2.0
- Size: 450 million parameters
- Type: Vision-Language-Action (VLA); consumes camera images, robot state and an optional language instruction, and predicts continuous action sequences.
- Status: **CANDIDATE ONLY — not downloaded, installed, tested or approved for physical deployment.**

The model card describes SmolVLA as a compact VLA designed for robot manipulation research. It still requires robot-specific demonstrations, fine-tuning and evaluation; the published training guidance uses a GPU. Its 450M parameter count does not guarantee it will run acceptably on this project's available hardware or without cost.

### Project fit and limits

- **Coconut Harvest AI:** possible simulation-only research for a robot arm's bounded grasp/reach/cut-preparation proposal. It is not validated for harvesting, outdoor conditions, people/animals nearby, coconut mass, cutting forces or the 0–30 m operating concept. Cutting and release must remain independently guarded and human-supervised.
- **Flood Rescue AI:** not suitable as boat navigation, water-current control, rescue approach or propulsion policy. Consider only if a separate manipulator is designed, and then only in a controlled simulator with bounded proposals.
- **Sentinel Multimodal Screening AI:** not a substance-identification, search, enforcement or autonomous screening model. Consider only for a future non-consequential manipulator research task, if one is defined; otherwise do not integrate.
- **AI HOME:** not a general indoor mobile-navigation or hazard-response policy. Do not use for driving wheels, stairs, doors, appliance control or emergency response. A future arm/gripper task would require separate robot-specific validation.
- **AI NOMAD:** **not recommended for quadruped locomotion, gait, balance, foothold selection or outdoor navigation.** SmolVLA's manipulation focus does not establish dog-like mobility capability.
- **AI Car:** **not suitable for vehicle control.** No steering, throttle, braking, gear, propulsion or road-decision authority.
- **AI Motorcycle / EasyRide:** **not suitable for motorcycle control.** No steering, throttle, braking, balance, motor or rider-safety authority.

### Additional candidates not approved

- **OpenVLA 7B** ([model card](https://huggingface.co/openvla/openvla-7b)): research reference only, **HOLD — LICENCE REVIEW REQUIRED**. Although the Hugging Face card labels the checkpoint MIT, the upstream OpenVLA repository warns that the pretrained weights may inherit the Llama 2 Community License. The 7B model also has substantial compute needs and documents remote custom code. Do not adopt, download or commercially use until the exact weight terms and code are reconciled.

### Robotics safety rule

A VLA predicts actions; it is not a safety controller. In PUI89 it may only produce a bounded, logged **ActionProposal** for a simulator or an independently reviewed offline experiment. It must never issue actuator commands. Require typed observations, robot-specific coordinate/action mapping, joint and workspace limits, collision checks, speed/force limits, emergency stop, watchdog, deterministic safety interlocks, human approval, and a verified safe fallback outside the model. No physical robot tests are authorized by this documentation.

