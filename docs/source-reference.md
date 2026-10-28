# TriageServer — source reference

[README](../README.md) · [Operations](operations.md)

Reviewed 2026-10-28 at source commit [`d86b9e13e7a3`](https://github.com/Rabeh-LLC-KSA/TriageServer/commit/d86b9e13e7a3de917a804fd505aa66ba49ac313e). This is a static source inventory. Commands below are declared commands, not a statement that they passed. Deployment availability and provider accounts were not tested.

## package.json

Source: [package.json](../package.json).

No runtime `engines` requirement is declared in this manifest. Use the project CI/image configuration where available; record the tested runtime when reproducing older applications.

| Script | Declared behavior |
|---|---|
| `start` | `nodemon ./bin/www` |

Scripts containing `--write`, `--fix`, `migrate`, `eject`, or publication/deployment commands can change files, data, or external systems. Read the manifest before running them.

## Application entry points

- [app.js](../app.js)

## HTTP routing sources

- [routes/index.js](../routes/index.js)
- [routes/users.js](../routes/users.js)

## Tests present

No application test files matching the conventional test locations were found in the reviewed tree. Absence here is a coverage gap, not evidence that behavior is correct.

## Configuration register

No environment-variable register could be derived from the reviewed configuration files. This does not prove that no external configuration is required; inspect the entry points and consumer applications.

## Route declaration index

The paths below are **local declarations**, not complete URLs. Parent groups, `/api` registration, mounted Express routers, resource expansion, middleware, and macros alter the final route. This static index does not infer authentication guarantees or response schemas. For Laravel, run `php artisan route:list --except-vendor` after setup; inspect controller/request/resource classes for payloads and authorization.

| Source | Declaration | Local path |
|---|---|---|
| [routes/index.js](../routes/index.js) | `get` | `/` |
| [routes/index.js](../routes/index.js) | `get` | `/area` |
| [routes/index.js](../routes/index.js) | `get` | `/path` |
| [routes/users.js](../routes/users.js) | `get` | `/` |

## Review findings and limits

- The manifest does not declare pg, nodemon, lazy, or xml2js although the runtime/start/import scripts reference them. A clean npm install is insufficient to reproduce all features.
- PostgreSQL connection details are embedded in source and no environment template is provided. Move configuration out of code before deployment; do not reuse historical embedded credentials.
- No lockfile, automated tests, or supported runtime pin is present. This is a historical prototype, not a verified production service.

This documentation review does not certify production readiness, financial controls, regulatory approval, security, or test coverage. Resolve the recorded gaps with code changes and operational evidence.
