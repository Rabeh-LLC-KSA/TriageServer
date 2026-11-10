# TriageServer

<div dir="rtl">

**مع رابح الكل رابح**  
منصة متكاملة في عالم التقنية المالية حيث تلتقي الفرص بالاستثمار

</div>

**With RABEH, everyone wins**  
Your integrated platform in the world of financial technology, where opportunities meet investment.

<!-- RABEH:README:START -->
**README version:** `1.0.0` · **Last updated:** `2026-11-10`  
**Last change:** Reorganized repository guidance; added the RABEH slogan, four-pillar map, documentation version and maintenance checks.
<!-- RABEH:README:END -->

Documentation version is independent of application/package versions. [File history](https://github.com/Rabeh-LLC-KSA/TriageServer/commits/master/README.md).

## Repository role

Historical trajectory-data prototype; no established RABEH product integration.

**Website and design authority:** [`rabeh-investments-web`](https://github.com/Rabeh-LLC-KSA/rabeh-investments-web) is always RABEH’s main website and branding source. Preserve the current rabeh.sa design, Arabic RTL/English LTR behavior and existing capabilities when extending any product.

## Four pillars of RABEH

| Pillar | This repository’s role or roadmap boundary |
| --- | --- |
| 1. **Marketplace** | No established product linkage. |
| 2. **Fundraising** | No established product linkage. |
| 3. **Tokenization** | No established product linkage. |
| 4. **Exchange** | No established product linkage. |

The pillar map describes product ownership and intended integration. Repository presence alone does not establish a live financial capability. [Platform roadmap](https://github.com/Rabeh-LLC-KSA/rabeh_docs/blob/main/docs/four-pillars-roadmap-20261110.md) · [Delivery evidence](https://github.com/Rabeh-LLC-KSA/rabeh_docs/blob/main/docs/implementation-status-20261110.md).

## Guide contents

- [Start here](#start-here)
- [Setup](#setup)
- [Runtime and versions](#runtime-and-versions)
- [Commands](#commands)
- [Architecture and boundaries](#architecture-and-boundaries)
- [Verification and delivery](#verification-and-delivery)
- [Documentation and contribution](#documentation-and-contribution)
- [License](#license)
- [README maintenance](#readme-maintenance)
- [README change log](#readme-change-log)

Historical Express / EJS trajectory-data prototype with PostgreSQL queries and data-import utilities.

This public repository is a prototype, not an established RABEH investment-platform service. Runtime/import dependencies and embedded historical connection configuration require remediation before use.

| Repository fact | Value |
| --- | --- |
| Default branch | `master` |
| Documentation review | 2026-11-10 |
| Source snapshot | [`TriageServer@f18e199657bb`](https://github.com/Rabeh-LLC-KSA/TriageServer/commit/f18e199657bbd2e025325478cef20ed39a3c4311) |
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

## README maintenance

Update the affected README in the same pull request as setup, configuration, API, feature, dependency or deployment changes. Keep the slogan and all four pillar names near the top. Preserve existing technical guidance, third-party attribution and historical evidence.

Use documentation semantic versions: **patch** for corrections, **minor** for added guidance, **major** for a substantial guide restructure. The `1.0.0` baseline versions this README standard, not an application release. Use the actual edit date in `YYYY-MM-DD` and summarize the change.

From the repository root, after editing a managed README:

```bash
python3 .github/scripts/readme_quality.py --update README.md --version 1.0.1 --date 2026-11-10 --note "Describe the actual documentation change."
python3 .github/scripts/readme_quality.py --check
```

Choose the next version and actual date; replace `README.md` with a nested guide path when needed. The updater preserves prior entries. The **README Quality** workflow checks branding, pillars, version/date, change history and relative file links. Changed managed guides must increment their documentation version. The inventory and documented exclusions are in [`.github/readme-manifest.json`](.github/readme-manifest.json).

[Organization documentation standard](https://github.com/Rabeh-LLC-KSA/rabeh_docs/blob/main/docs/readme-standard.md). Application release, deployment and authenticated acceptance remain separately evidenced.

## README change log

| Version | Date | Changes |
| --- | --- | --- |
| 1.0.0 | 2026-11-10 | Reorganized repository guidance; added the RABEH slogan, four-pillar map, documentation version and maintenance checks. |
