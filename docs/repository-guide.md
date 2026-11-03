# TriageServer — repository guide

[README](../README.md) · [Documentation index](README.md)

Reviewed 2026-11-03 against [`b30cba01fd25e99a0f34be1437d20e4eb9a8c4e4`](https://github.com/Rabeh-LLC-KSA/TriageServer/commit/b30cba01fd25e99a0f34be1437d20e4eb9a8c4e4). This guide records source evidence; it does not certify a running environment.

## Responsibilities

Historical Express / EJS trajectory-data prototype with PostgreSQL queries and data-import utilities.

This public repository is a prototype, not an established RABEH investment-platform service. Runtime/import dependencies and embedded historical connection configuration require remediation before use.

## Source map

| Path | Responsibility | Tracked files beneath path |
| --- | --- | --- |
| [routes](../routes) | HTTP and console entry points | 2 |
| [public](../public) | Public static assets | 212 |

## Configuration

No root environment example/configuration key inventory is established by the inspected files. Do not invent provider values or copy production credentials into local setup. Review the source map and consumer environment when applicable.

Names do not determine secrecy by themselves: some public site keys are publishable, while API/signing credentials are not. `NEXT_PUBLIC_*`, Nuxt public runtime values and mobile-bundled values can be read by users. Logs and examples must remain redacted.

## Interfaces and data

Use the route/component/source directories above to trace the interface. This repository does not establish a standalone database schema unless a schema/migration directory is explicitly present.

## Integration and change control

Trace each endpoint/provider from configuration to the transport/client call site. Record which repository owns the contract, authentication method, timeout/retry policy and failure handling. Keep server secrets outside frontend bundles and preserve locale-aware navigation.

## Automated checks

No application test source was found under the conventional test directories in this snapshot. Do not label a placeholder `test` script, build, formatter, or dependency install as regression coverage.

## Delivery workflow

No GitHub Actions workflow is tracked in this snapshot. Document the real deployment owner and procedure before claiming automated delivery.

## Troubleshooting and runbook

| Symptom | Investigation / next action |
| --- | --- |
| Install or boot failure | Compare the declared engine, lockfile, framework version, generated files and shared-source paths. Capture a redacted error and exact commit. |
| Authentication / permission failure | Check the intended environment, token issuer/audience, role/permission checks and expired/revoked sessions. Do not bypass authorization to make a check pass. |
| Data or external-provider failure | Confirm configured endpoints, isolated credentials, queue/worker state, callback verification, retry/idempotency handling and provider sandbox availability. |
| Build succeeds but UI/API fails | Verify a real route/user journey and its backend response; record browser/device, locale, HTTP status and deployment revision. |
| Regression after release | Compare the deployed revision/artifact and configuration, retain logs, and roll back via the existing release process. Restore data only through a verified recovery plan. |

## Documentation review evidence

This review inspected repository trees, entry/manifest/configuration files, workflows and existing guides. Markdown links, code fences, configuration-name listings and documented command names are checked separately from application execution. No live payment, signature, SMS/email delivery, database reset or credential validation is part of a documentation review. Record any actual CI runs in the change request and central publication report.
