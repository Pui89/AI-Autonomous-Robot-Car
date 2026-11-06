# Security Policy

## Scope

This repository is an early-stage software research scaffold. It is not connected to a physical vehicle and must not be used as an autonomous-driving or vehicle-control system.

## Reporting a vulnerability

Do not publish exploitable details in a public issue. Use GitHub private vulnerability reporting if enabled. Otherwise contact the repository owner privately through an appropriate GitHub channel.

Include the affected component or commit, impact, reproduction conditions, and a safe minimal proof of concept. Do not include secrets, personal data, or unsafe instructions.

## Security expectations

- Never commit tokens, passwords, private keys, or personal data.
- Review dependencies, licenses, and provenance before adoption.
- Validate external and simulated inputs.
- Use least-privilege permissions and protect the default branch.
- Require review and passing checks before merging where settings permit.
- Treat model-generated content as untrusted input.
- No physical vehicle, actuator, or road testing is in scope.
