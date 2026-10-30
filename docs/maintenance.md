# Maintenance and verification — TriageServer

Reviewed 2026-10-30 against `master` at `b563228eac64cb971df30f01994f37ed01b87565` before this repair/documentation change. This is a source and operational-evidence review; unexecuted checks below are a runbook, not passing test results.

## Start here

- [README](../README.md): purpose and documentation map.
- [Operations](operations.md): setup, configuration, troubleshooting and dependencies.
- [Source reference](source-reference.md): entry points, commands, interfaces and constraints.

## Current evidence

Historical public Express/PostgreSQL trajectory prototype. Imported packages and runtime tooling are not fully declared. Embedded database connection details must be reviewed and rotated outside Git if ever used. Do not infer deployment readiness from npm start.

## Validation runbook

Use the package manager and runtime documented in Operations, install from the reviewed lockfile where one exists, and configure sandbox endpoints. The following scripts are declared; they are not a claim that they all passed in this review.

| Script | Declared command | Purpose and limit |
|---|---|---|
| None | — | No build/test/lint command is declared. |

### Acceptance scenarios

Verify direct links and refresh, empty/loading/error states, keyboard focus, accessible control names, mobile widths, Arabic RTL/English LTR, and expected authenticated/unauthenticated behavior. Compare frontend assumptions with the owning API’s route and permission contract. Record the tested URL, commit, browser/device and result. Do not use a real payment as a smoke test.

## Release and rollback

Identify the actual deployment branch, target host/site and build-time public configuration. Confirm CI and deployment results separately. After rollout, verify the public route and affected flow; a successful build is not proof that users received it. Retain the previous compatible artifact and configuration for rollback, and recheck API compatibility after restoring it.

## Review and support handover

Include the problem and reproduction steps, affected interfaces, exact changed files, commands/results, untested areas, deployment impact and rollback steps in the PR. Update README, Operations and Source Reference when their claims change.

Record the responsible maintainer and an existing approved internal support channel in the release record; this review does not invent owners or contact addresses. Escalations should contain a redacted request/correlation ID, timestamp, environment, commit and observed versus expected behavior. Never attach tokens, customer records, private keys or unredacted provider payloads.
