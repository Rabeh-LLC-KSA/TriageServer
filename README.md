# TriageServer

Historical Express / EJS trajectory-data prototype with PostgreSQL queries and data-import utilities.

This public repository is a prototype, not an established RABEH investment-platform service. Runtime/import dependencies and embedded historical connection configuration require remediation before use.

| Repository fact | Value |
| --- | --- |
| Default branch | `master` |
| Documentation review | 2026-11-03 |
| Source snapshot | [`b30cba01fd25`](https://github.com/Rabeh-LLC-KSA/TriageServer/commit/b30cba01fd25e99a0f34be1437d20e4eb9a8c4e4) |
| Scope | Source/configuration review; production availability is verified separately. |

## Start here

| Task | Reference |
| --- | --- |
| Set up, configure, understand modules and interfaces | [Repository guide](docs/repository-guide.md) |
| Find every checked-in Markdown guide | [Documentation index](docs/README.md) |

## Setup

Read the implementation constraints above and [source guide](docs/repository-guide.md) before installing or starting this historical application. The manifest commands are documented below for maintainers; they are not evidence that a clean install or a deployment is ready.

```bash
git clone https://github.com/Rabeh-LLC-KSA/TriageServer.git
cd TriageServer
```

Use isolated non-production configuration. Preserve existing lockfiles, review dependency/install scripts, and resolve the documented missing dependencies before executing the service.

## Runtime and versions

These are **declared requirements**, not a claim about the versions installed on a running host.

| Component | Source declaration |
| --- | --- |
| express | ~4.12.2 |
| Node engine | Not declared in package.json |
| Manifest version | 0.0.0 |

## Commands

| Command | Manifest expansion | Effect / limit |
| --- | --- | --- |
| `npm run start` | `nodemon ./bin/www` | Declared command; not executed by this documentation review. |

## Architecture and boundaries

Routes, request handlers and data-access code belong to this implementation only. Follow the actual entry file and configuration reads; do not assume compatibility with the Laravel services or current web frontend.

## Verification and delivery

Use only the commands actually declared above and inspect the checked-in workflows in the source guide. A build is distinct from functional tests, and a passing workflow is distinct from a verified production deployment.

For releases, record the commit, checks, environment, deployment run and post-release evidence. Roll back to a known artifact/revision through the existing release process; do not reset shared branches or delete persistent data as a routine rollback.

## Documentation and contribution

Update this README and the [repository guide](docs/repository-guide.md) when setup, configuration, routes, dependencies, tests or delivery change. Keep detailed domain guides discoverable in the [index](docs/README.md). Use focused pull requests against the documented branch, preserve third-party notices, and never paste credentials, customer records or signing keys into examples.

## License

No root license file is present in this snapshot. A dependency or template license is not, by itself, a grant to redistribute the entire application; confirm terms with the repository owner.
