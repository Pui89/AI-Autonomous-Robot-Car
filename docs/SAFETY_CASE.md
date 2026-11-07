# Safety Case — PUI89 AI Robot Car

**Status: PROPOSED / DOCUMENTARY BASELINE ONLY.** This is an initial design safety case, not a completed vehicle hazard analysis, safety approval, certification, or evidence that a physical vehicle or safety system exists.

## 1. Intended purpose and authority boundary

PUI89 AI Robot Car is a human-driver-first vehicle-intelligence research concept. The software may explore evidence-linked driver advisories, environmental awareness, vehicle-health observations, trip preparation, parking-assistance concepts and predictive-maintenance research.

The driver remains responsible for vehicle operation. AI outputs are advisory only. This repository must not command or directly influence steering, throttle, braking, propulsion, ignition, gear selection, doors, restraints or other vehicle actuators. No direct ECU, CAN, OBD control, drive-by-wire or production vehicle connection is authorized by this document.

The concept is not an autonomous vehicle, road-ready product, certified driver-assistance system, collision-avoidance guarantee or substitute for driver training, vehicle maintenance, certified protective systems or emergency services.

**Current evidence boundary:** early software scaffold and design requirements only. No functioning vehicle, integrated vehicle sensors, road test, crash test, validated perception, vehicle-bus integration, homologation or certification is established. Vehicle architecture, mass, speed, powertrain, battery chemistry, braking system, tyres, sensor suite and operating envelope are not verified.

## 2. Non-negotiable safety principles

1. **Human driving authority:** no AI control path to steering, throttle, brakes, propulsion or other vehicle actuators.
2. **No false reassurance:** an absence of detected hazards, missing sensor data or a NORMAL software state must never mean that the road or vehicle is safe.
3. **Driver attention first:** alerts must not distract, overload, startle or encourage the driver to look away from the road. No interaction requiring prolonged visual or manual attention while driving.
4. **Uncertainty visible:** stale, missing, degraded, occluded, conflicting, uncalibrated or out-of-domain evidence is explicitly UNKNOWN/DEGRADED.
5. **Independent vehicle protections:** certified vehicle systems, driver controls and required protective devices remain independent of this AI software.
6. **Safe failure:** loss of power, software crash, restart, update, sensor or network failure cannot issue a control command or impair the original vehicle's safe operation.
7. **Evidence before claims:** no claims of collision prevention, autonomous driving, roadworthiness, crashworthiness, functional safety, cybersecurity certification, waterproofing, fire resistance or regulatory conformity without suitable independent evidence.

## 3. Vehicle-specific hazard register and required controls

| Hazard area | Foreseeable failure or harm | Required controls and evidence |
|---|---|---|
| Collision and vulnerable road users | Missed pedestrian, cyclist, motorcyclist, child, animal, stopped vehicle, obstacle or road hazard; false warning; occlusion or poor visibility | Treat outputs as advisory research only. Evaluate by scenario, road-user type, distance, speed, lighting, weather, occlusion and sensor limitations. Report false negatives and false positives with sample sizes and uncertainty. Never claim collision avoidance. |
| Driver distraction and human factors | Alert overload, confusing priority, startling sound, visual/manual interaction, automation complacency or misunderstood confidence | Define an alert hierarchy, timing, modality, acknowledgement and dismissal behavior. No urgent or complex driver interaction while moving. Conduct human-factors and distraction assessment with qualified reviewers before any in-vehicle evaluation. |
| Speed, distance and time estimates | Incorrect units, timestamps, coordinate frames, object tracking, relative speed or time-to-collision estimate creates misleading advice | Validate units, frame transforms, synchronization, calibration, latency and uncertainty. Bound each estimate to its tested conditions. Suppress or downgrade advice when assumptions fail; do not present estimates as guaranteed safe stopping distances. |
| Braking, steering and vehicle dynamics | AI advice interpreted as a command; incorrect assumptions about braking distance, tyre grip, load, road grade or vehicle response | Maintain a strict software and interface boundary: no actuator command interfaces. Any future advisory must state assumptions and must not override driver or vehicle warnings. No brake/steering control, automated intervention or performance claim. |
| Weather, road surface and visibility | Rain, standing water, flooding, mud, oil, gravel, potholes, glare, fog, darkness, heat or debris changes traction and sensing | Treat road-condition inference as uncertain. Do not infer available tyre grip or safe speed from imagery alone. Define weather/visibility test strata and out-of-domain abstention. No flood traversal or severe-weather capability claim. |
| Vehicle electrical, battery and fire | Short circuit, damaged wiring, overcurrent, overheating, charging fault, battery thermal event or unsafe accessory installation | No physical electrical or battery integration in this project stage. Future hardware requires qualified automotive electrical engineering, appropriate isolation, fusing, thermal design, EMC assessment and battery/charging validation. Never tap safety-critical circuits or alter OEM protection. No fire-resistant/fireproof claim without exact-system evidence. |
| Crash, occupants and post-crash behavior | Sensor/device detaches, becomes a projectile, obstructs airbags, seatbelts, controls or visibility; post-crash power or alert behavior is unsafe | Any future installation must be assessed for mounting retention, occupant impact, airbag deployment zones, driver sight lines, controls and emergency egress by qualified automotive specialists. No claim of crashworthiness. |
| Sensor and data integrity | Spoofed, replayed, occluded, dirty, misaligned, saturated, stale or contradictory camera/radar/lidar/GNSS/vehicle data | Track sensor identity, calibration, timestamp, quality, health, provenance and freshness. Detect plausible but corrupted data where possible. Preserve disagreement and fail to UNKNOWN/DEGRADED; test sensor dropouts, drift, replay and spoofing. |
| Cybersecurity and vehicle networks | Compromised update, malicious input, unauthorized diagnostic access, CAN/vehicle-bus injection, exposed credentials or remote access | No vehicle-network connection or remote-control capability. Future interfaces require threat modelling, authenticated access, least privilege, secure update and independent automotive cybersecurity review. Treat all external/model outputs as untrusted. |
| Privacy and location | Collection of faces, plates, voice, cabin activity, routes, home/work locations or trip histories beyond necessity | Minimize data; default to local/offline processing where feasible; provide clear notice, consent and sensing indicators; define access, retention and deletion. Do not commit personal trip, video, audio or location data to public repositories. |
| Predictive maintenance | False reassurance, incorrect fault classification, missed deterioration or inappropriate repair advice | Separate observed diagnostic codes/measurements from inferred risk. Show source, vehicle compatibility, date, uncertainty and limitations. Never suppress OEM warnings or replace qualified inspection. No predictive accuracy claims without representative validated data. |
| Power, software and update failure | Reboot, partial update, resource exhaustion, clock drift or device power fault disrupts an advisory or affects a future host interface | Keep the advisory system isolated from vehicle control. Test power loss, restart, stale state, malformed inputs, clock errors, resource exhaustion and rollback. On failure, withdraw the advisory and leave OEM vehicle functions unaffected. |

## 4. Required software states

- **ADVISORY_AVAILABLE:** only the specific evidence-backed advisory function is available within its tested scope.
- **LIMITED:** one or more non-critical inputs or functions are unavailable; output scope is reduced and limitations shown.
- **UNKNOWN_DEGRADED:** missing, stale, conflicting, invalid, uncalibrated or out-of-domain data prevents a reliable assessment.
- **SYSTEM_UNAVAILABLE:** software, power, timebase or integrity checks fail; no advisory is presented as current.
- **REVIEW_REQUIRED:** a human or qualified technician must review the evidence before further interpretation.

Do not use a global SAFE/ALL_CLEAR status. A software NORMAL label is not a statement about road safety, vehicle roadworthiness or the absence of hazards. No state authorizes vehicle control.

## 5. Minimum validation sequence before any in-vehicle research

1. **Scope and hazard analysis:** define vehicle class, intended use, excluded use, driver population, operating conditions, foreseeable misuse and authority boundary.
2. **Software-only contract tests:** validate units, timestamps, coordinate frames, evidence links, confidence interpretation, freshness, sensor disagreement, abstention and prohibited actuator interfaces.
3. **Synthetic and replay evaluation:** use documented, lawfully sourced scenarios; include day/night, weather, road-user classes, occlusion, rare events, sensor failures and distribution shifts. Keep synthetic results explicitly simulation-only.
4. **Data and model governance:** verify source, consent/lawful basis, licence, dataset splits, leakage controls, model and dependency provenance, privacy and reproducibility.
5. **Human-factors review:** assess alert timing, distraction, comprehension, workload, false-alarm tolerance and driver overreliance using appropriate non-driving studies first.
6. **Bench validation:** if hardware is later proposed, conduct isolated electrical, thermal, EMC, mounting, power-failure and interface tests under qualified engineering oversight.
7. **Controlled vehicle evaluation:** only after legal, insurance, automotive engineering, functional-safety and cybersecurity reviews; use a closed test facility, trained drivers, independent safety supervision and an approved test plan. No public-road testing is implied or authorized here.
8. **Evidence review:** record exact vehicle/device/software revision, test method, calibration, conditions, sample sizes, failures, metrics, limitations, reviewer and date. Publish only the verified scope.

## 6. Stop, incident and recovery requirements

Withdraw the affected advisory and require review after sensor disagreement, calibration expiry, timestamp/clock fault, repeated false alerts, unexpected output, suspected spoofing, software integrity failure, power/thermal anomaly or privacy/security incident. Do not encourage a driver to troubleshoot or interact with the system while driving. Driver safety and applicable road rules take priority; stop in a safe place when appropriate and seek qualified assistance.

Any future in-vehicle prototype requires a documented removal/isolation procedure, safe power-down, data protection, rollback and incident review. No automatic recovery or update may create vehicle-control authority.

## 7. Evidence and status vocabulary

Use **PROPOSED**, **IMPLEMENTED**, **TESTED**, **SIMULATION-ONLY**, **MEASURED**, **NOT VERIFIED** and **NOT VALIDATED** precisely. A passing software test proves only the tested software behavior. A sensor datasheet, concept image, synthetic scenario or benchmark does not prove installed-vehicle performance or road safety.

**Current conclusion:** PUI89 AI Robot Car remains a human-driver-first research concept with an early software scaffold. Vehicle integration, perception performance, driver-distraction safety, vehicle dynamics, electrical/battery safety, crashworthiness, cybersecurity assurance and road performance remain **NOT VERIFIED / NOT VALIDATED**.

_Last reviewed: 8 November 2026 (Asia/Bangkok)._
