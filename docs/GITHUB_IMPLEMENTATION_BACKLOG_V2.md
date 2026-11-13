# PUI89 AI Global SUV — GitHub Implementation Backlog v2

**Status:** Proposed backlog. Issues have not been created automatically.  
**Working mode:** Software-first, CPU-only, open-source-first, no-cost by default.  
**Safety boundary:** No physical vehicle, CAN, ECU, steering, throttle, brake or actuator integration.

## EPIC A — Requirements and product engineering

| Key | Task | Priority | Acceptance evidence |
|---|---|---|---|
| CAR-001 | Publish master engineering specification | P0 | Product direction, assumptions, unresolved decisions and validation boundary documented |
| CAR-002 | Define chassis/payload engineering checklist | P0 | Occupant-inclusive payload, GVWR, GAWR, curb mass, tires, brakes, suspension and CG gates listed |
| CAR-003 | Evaluate full HEV first; compare ICE, HEV, PHEV and BEV | P0 | HEV/PHEV/series hybrid compared without premature selection |
| CAR-004 | Define flood-risk awareness and avoidance requirements | P0 | Component exposure map, inspection procedure and no-unverified-wading rule |
| CAR-005 | Create global compliance applicability matrix | P1 | Jurisdiction-specific applicability review plan; no blanket compliance claim |
| CAR-006 | Create inclusive cabin and cargo requirements | P1 | Ergonomics, accessibility, occupant protection and cargo restraint criteria |

## EPIC B — Shared AI Core and safety foundation

| Key | Task | Priority | Acceptance evidence |
|---|---|---|---|
| CAR-007 | Align with canonical Shared AI Core contracts | P0 | Version/commit pinned; no competing local contract definitions |
| CAR-008 | Add schema and unit validation | P0 | Invalid types/units/ranges rejected or explicitly unknown |
| CAR-009 | Add freshness and timestamp validation | P0 | Missing timezone, stale and future-dated records tested |
| CAR-010 | Add provenance and evidence references | P0 | Every accepted signal and advisory traceable to source |
| CAR-011 | Add uncertainty and abstention handling | P0 | Missing/conflicting/low-quality evidence yields unknown or abstention |
| CAR-012 | Add advisory-only authority gate | P0 | Any control authority or actuator wording rejected |
| CAR-013 | Add FailureReport and degraded-state handling | P0 | Faults create traceable reports and bounded recovery guidance |
| CAR-014 | Add deterministic replay and regression fixtures | P0 | Same input produces same advisory and evidence record |

## EPIC C — Vehicle intelligence software

| Key | Task | Priority | Acceptance evidence |
|---|---|---|---|
| CAR-015 | Implement vehicle snapshot/advisory baseline | P0 | Pure Python, no dependencies, explicit unknown handling |
| CAR-016 | Road and obstacle perception adapter interface | P1 | Typed interface only; no model weights downloaded |
| CAR-017 | Flood hazard advisory baseline | P1 | Unknown water depth never declared safe; water-covered route advises avoidance |
| CAR-018 | Weather and visibility context | P1 | Stale/missing weather remains unknown |
| CAR-019 | Collision-risk advisory interface | P1 | Evidence-linked advisory only; no braking command |
| CAR-020 | Battery and thermal diagnostic interfaces | P1 | BMS/temperature signal quality and anomaly state preserved |
| CAR-021 | Tire intelligence interface | P1 | Pressure/temperature anomaly input validated |
| CAR-022 | Whole-vehicle health summary | P1 | Engine, transmission, brake, electrical and hybrid signals separated |
| CAR-023 | Predictive maintenance evidence model | P2 | Requires longitudinal evidence; no unsupported prediction |
| CAR-024 | Emergency and post-crash event interface | P2 | Event triage, human confirmation and connectivity failure represented |
| CAR-025 | Navigation and Road Memory interfaces | P2 | Source freshness, privacy and location provenance documented |
| CAR-026 | Payload intelligence interface | P2 | Unmeasured payload explicitly unknown; no inferred certified load |

## EPIC D — Simulation, evaluation and release evidence

| Key | Task | Priority | Acceptance evidence |
|---|---|---|---|
| CAR-027 | Synthetic road/flood scenario set | P1 | Versioned fixtures with expected outcomes and limitations |
| CAR-028 | Fault injection suite | P1 | Missing, stale, contradictory, corrupt and sensor-loss cases |
| CAR-029 | Metrics and benchmark report | P1 | False alerts, missed events, latency, resource use and sample sizes |
| CAR-030 | CPU-only resource profile | P1 | Reproducible RAM/CPU/runtime report |
| CAR-031 | Security and dependency provenance review | P1 | Dependency-free baseline or reviewed provenance/licences |
| CAR-032 | Gate evidence dashboard | P2 | Proposed/implemented/simulation-tested/bench-tested/field-tested labels |

## Definition of done

A backlog item is complete only when:
- Requirement and scope are explicit.
- Code and/or documentation is committed through a reviewed pull request.
- Tests cover normal, missing, stale, invalid and failure cases as relevant.
- Evidence, limitations and known risks are recorded.
- No unsupported physical-performance claim is introduced.
- No cost, paid service, automatic download or protected default-branch write is required.

## Initial execution sequence

1. CAR-001 through CAR-006: lock the engineering baseline and open decisions.
2. CAR-007 through CAR-014: establish safe shared contracts and evidence handling.
3. CAR-015: deliver a deterministic software-only advisory baseline.
4. CAR-016 through CAR-022: add bounded module interfaces.
5. CAR-027 through CAR-031: test and document reproducibility before any model/hardware consideration.
