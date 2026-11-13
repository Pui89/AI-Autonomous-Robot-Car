# Threat Model — PUI89 AI Robot Car

**Status:** Initial software threat model with vehicle-domain extensions. This is not a completed penetration test, automotive cybersecurity assessment or vehicle safety approval.

## Assets

Source code, repository credentials, workflow permissions, approved datasets, model files, configuration, evaluation evidence, user/driver information and any future advisory-device interfaces.

## Threat actors and trust boundaries

Potential sources include malicious or compromised dependencies, untrusted datasets/models, hostile or malformed external inputs, unauthorized repository contributors, compromised developer accounts, malicious update artifacts, nearby wireless attackers and (only if a future vehicle interface is separately approved) compromised diagnostic or vehicle-network endpoints.

The current project has no established physical vehicle integration or vehicle-network connection. Do not imply that CAN, OBD, ECU, GNSS or sensor interfaces are currently connected.

## Threats and required controls

| Threat | Required control |
|---|---|
| Credential leakage or unauthorized repository change | Least privilege, protected default branch, reviewed changes, secret scanning, credential revocation and evidence preservation. |
| Malicious dependency, action, model or update | Verify publisher, source, revision, licence, integrity and transitive dependencies; pin reviewed versions; no automatic trust in model output. |
| Spoofed, replayed, malformed, stale or corrupted observation | Validate schema, size, units, timestamps, source identity, freshness and provenance; include negative and fault-injection tests. |
| Sensor deception, occlusion, drift or conflicting evidence | Preserve source-specific evidence and disagreement; detect known integrity failures; abstain or mark UNKNOWN/DEGRADED rather than fabricate certainty. |
| Misleading driver advisory or prompt injection | Treat external text/model output as untrusted; require structured evidence and policy checks; do not let prompts alter the human-driver authority boundary. |
| Driver distraction or alert manipulation | Prevent unreviewed high-priority alerts; test alert rate, comprehension and failure behavior; no complex interaction while driving. |
| Unauthorized vehicle-network or actuator access | No vehicle-network or actuator interface in the current scope. Any future proposal requires separate authorization, threat analysis and qualified automotive cybersecurity review; never expose steering, throttle or braking commands. |
| Location, video, plate, voice or cabin-data exposure | Minimize collection; prefer local processing; restrict access; define consent, retention and deletion; keep personal data out of public repositories and logs. |
| Power, update or software failure | Test integrity checks, restart, stale-state clearing, rollback and unavailable-state behavior. Ensure the advisory component cannot affect OEM vehicle functions. |

## Incident response

Identify the affected revision and scope; contain by disabling or removing the advisory component where safe; preserve non-sensitive evidence; revoke exposed credentials; restore a trusted revision; verify tests and integrity; document user/privacy impact and lessons. Do not publish secrets, personal vehicle data or exploit details in public issues.

## Vehicle-domain release gate

Before any in-vehicle evaluation, require documented vehicle/interface scope, legal and insurance review, qualified automotive engineering review, cybersecurity threat analysis, privacy review, human-factors assessment, electrical/EMC and mounting checks, approved test facility and independent safety supervision. No public-road testing, vehicle-network connection or actuator control is authorized by this threat model.

_Last reviewed: 8 November 2026 (Asia/Bangkok)._
