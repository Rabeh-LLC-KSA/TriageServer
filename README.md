# TriageServer

## Maintenance and verification

Use the [maintenance guide](docs/maintenance.md) for change review, validation, release evidence, rollback and support handover. It supplements the setup and source reference with repository-specific checks and explicitly records what remains unverified.

A legacy Express / EJS trajectory-data prototype. It queries a PostgreSQL log table by participant identifier and time range and includes data-import utilities.

| Repository facts | Value |
|---|---|
| Organization | Rabeh-LLC-KSA |
| Default branch | `master` |
| Source review | 2026-10-28 |
| Repository state | Unarchived |

## Documentation map

| Need | Start here |
|---|---|
| Source, commands, configuration, interfaces, and checks | [Source reference](docs/source-reference.md) |
| Setup, operations, troubleshooting, and known gaps | [Operations guide](docs/operations.md) |

## Getting started

Use the [operations guide](docs/operations.md) for the actual setup path and its prerequisites. The [source reference](docs/source-reference.md) records declared scripts, configuration names, source modules, tests, and automation. Read known blockers before installing or executing historical applications.

## Important implementation notes

- The manifest does not declare pg, nodemon, lazy, or xml2js although the runtime/start/import scripts reference them. A clean npm install is insufficient to reproduce all features.
- PostgreSQL connection details are embedded in source and no environment template is provided. Move configuration out of code before deployment; do not reuse historical embedded credentials.
- No lockfile, automated tests, or supported runtime pin is present. This is a historical prototype, not a verified production service.

## Documentation and support

This README is based on the repository source reviewed on 2026-10-28. It does not assert that a deployment is live or that all integrations have been verified. Keep setup, configuration, interfaces, tests, and operations documentation in the same change as the corresponding code. Open a focused issue or pull request with reproducible evidence and redacted logs.

## License

No root license file was found in the reviewed tree. Confirm licensing with the repository owner before redistribution. Existing third-party licenses and notices remain applicable.

