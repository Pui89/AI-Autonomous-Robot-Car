# Agentic AI System

Status: proposed architecture, not implemented autonomous vehicle control.

## Roles
- Perception analyst: summarizes simulated observations and quality.
- Road-context analyst: interprets simulated road, weather and visibility.
- Vehicle-health analyst: flags documented or synthetic anomalies.
- Cybersecurity analyst: checks input integrity and software events.
- SHIELD analyst: consolidates hazards and uncertainty.
- Evidence auditor: checks provenance and test records.
- Supervisor: applies deterministic policy gates and produces advisory-only output.

## Rules
Agents use typed bounded inputs and return structured proposals. Treat model output and external content as untrusted. Require evidence references, timestamps and limitations. Reject stale, conflicting, invalid or unsupported proposals. Human review is required. No agent may operate a physical vehicle.