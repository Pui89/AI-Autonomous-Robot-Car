# PUI89 Compact Smart Car — Fire & Flood Resilience Requirements v0.1

**Status:** Proposed requirements for software research and future engineering review. No physical fire, flood, ingress, thermal, crash or occupant-protection performance is implemented, tested or certified.

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


