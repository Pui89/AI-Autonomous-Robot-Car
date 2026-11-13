# AI Autonomous Robot Car — Perception Accuracy Upgrade v0.1

**Status:** Requirements specified; no autonomous driving or physical navigation capability is validated.

Shared contract: [PUI89 Perception and Accuracy Standard](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/perception/PUI89_PERCEPTION_AND_ACCURACY_STANDARD_V0.1.md).

## Priority perception tasks

1. Detect and track static/dynamic obstacles, people, animals and vehicles.
2. Segment traversable ground, road edges, curbs, drop-offs and free space.
3. Estimate depth and obstacle height using calibrated depth/stereo/LiDAR evidence.
4. Classify terrain as flat, rough, loose, slippery, steep or unknown; require appropriate measurements for friction claims.
5. Build and maintain SLAM/localization with pose uncertainty and map freshness.
6. Detect wheel slip, stuck state and odometry disagreement using wheel/IMU and other suitable sensors.
7. Predict obstacle trajectories and collision risk over a declared time horizon.
8. Detect sensor blockage, localization jumps, timestamp mismatch and degraded sensor fusion.
9. Plan only within a validated vehicle envelope; stop or request help when localization/perception is inadequate.

## Evaluation

Measure detection AP/recall, free-space IoU, depth and obstacle-height error, localization drift, traversability classification, collision-avoidance false negatives, trajectory prediction error and sensor-fault detection latency. Stratify by rain, darkness, glare, dust, slopes, loose ground and partial occlusion.

**Safety boundary:** software perception and simulation do not establish safe physical navigation. Emergency stop, independent safety controls and supervised testing remain separate requirements.
