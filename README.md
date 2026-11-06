# PUI89 AI Robot Car

**Repository:** `Pui89/ai-robot-car`  
**Project type:** Advanced AI-enabled car and robotics concept; software-first, simulation-first  
**Status:** Early-stage concept and engineering foundation — not a built, tested, autonomous, or road-certified vehicle.

## Mission

Develop a safety-first intelligent car platform for environmental awareness, hazard detection, vehicle-health monitoring, predictive maintenance, and explainable driver assistance. A human driver remains responsible for vehicle control. No autonomous driving or physical actuation is enabled in this initial project.

## PUI89 engineering rules

- **Strict zero-cost:** no paid APIs, subscriptions, cloud GPU, paid datasets, or services that can create charges.
- **Simulation first:** no commands to physical vehicles, steering, throttle, brakes, propulsion, or batteries.
- **Safety before features:** fail-safe behavior, human override, uncertainty reporting, and hazard analysis are mandatory.
- **Evidence before claims:** distinguish implemented, simulated, proposed, and independently validated capabilities.
- **Shared AI Core:** reuse PUI89 contracts and safety/evidence components; do not create duplicate core systems.
- **Security by default:** least privilege, dependency and secret checks, protected branches, and review before release.
- **No unsupported autonomous-driving, performance, or road-safety claims.**

## Initial capability areas

1. Environmental perception and hazard-awareness research.
2. Driver-assistance concepts with clear, prioritized human-facing warnings.
3. Vehicle health monitoring for battery, electrical, thermal, and component anomalies.
4. Road, weather, visibility, and nearby-object context where lawful data or simulation supports it.
5. Predictive maintenance with traceable evidence and uncertainty.
6. Safety supervision, stale-data detection, conflict handling, and conservative degradation.

## Development stages

1. Define requirements, hazards, operating boundaries, and shared AI Core interfaces.
2. Build software-only data contracts and deterministic baseline logic.
3. Create synthetic/simulation scenarios; do not connect to a real car.
4. Add evaluation, robustness, security, and regression tests.
5. Consider hardware only after documented safety reviews, legal review, and qualified engineering validation.

## Repository map

- `docs/PROJECT_PLAN.md` — scope, architecture, and staged roadmap.
- `docs/SAFETY_CASE.md` — hazards, safeguards, and validation boundaries.
- `SECURITY.md` — vulnerability reporting and security policy.
- `tests/` — software-only tests (to be implemented).
- `.github/workflows/quality.yml` — dependency-light automated checks.

## Current truth

This repository is an initial software and research scaffold. It does not contain a functioning car, validated perception model, real-time vehicle integration, or certified safety system. All outputs are advisory prototypes until independently validated.

## License

No license has been selected yet. Unless and until a license is added, standard copyright restrictions apply; do not assume this repository is open source.
