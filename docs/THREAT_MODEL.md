# Threat Model

Status: initial software threat model, not a completed security audit.

## Assets
Source code, repository credentials, workflow permissions, approved datasets, model files, configuration and evaluation evidence.

## Threats
Credential leakage; compromised dependencies; untrusted data/model provenance; prompt injection; spoofed, replayed, malformed, stale or corrupted observations; unauthorized repository changes; misleading evidence artifacts.

## Controls
Least privilege; no secrets in source; review dependencies and licences; validate types, ranges, sizes and timestamps; treat model output as untrusted; record commit identifiers and artifact hashes; use only available no-cost native security features.

## Response
Identify, contain, preserve evidence, revoke exposed credentials, restore trusted state, test and document lessons. Do not publish secrets or exploit details in public issues.