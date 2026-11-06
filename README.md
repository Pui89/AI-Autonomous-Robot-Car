# PUI89 AI Robot Car

**Repository:** `Pui89/ai-robot-car`  
**Project type:** Advanced AI-enabled car intelligence and robotics research; software-first, simulation-first.  
**Status:** Early-stage software scaffold. Not a built, road-tested, autonomous, or road-certified vehicle.

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

## License

No license has been selected. Unless and until one is added, standard copyright restrictions apply; do not assume this repository is open source.
