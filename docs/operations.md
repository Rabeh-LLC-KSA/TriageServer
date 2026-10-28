# TriageServer — operations

[README](../README.md) · [Source reference](source-reference.md)

## Historical architecture

Express renders EJS templates and serves static assets. `routes/index.js` exposes `/`, a placeholder `/area`, and `/path` with `pid`, `t1`, and `t2` query parameters. The path query uses SQL parameters against the `log` table defined in `table_create.sql`. `init.js` and `python/initialize_data.py` are data-import utilities.

## Reproduction status

A clean setup is currently blocked by undeclared dependencies and embedded database configuration. The declared start command is `npm start` (`nodemon ./bin/www`), but nodemon and pg are absent from package.json. The importer also references lazy and xml2js; the Python importer requires psycopg2. Resolve and pin compatible dependencies in a separate implementation change before running the prototype.

Use only a disposable PostgreSQL database and synthetic trajectory data. Review import formats and the schema before loading data. Do not expose this prototype publicly without authentication, input validation, error handling, and a supported dependency/runtime plan. There is no verified deployment or test pipeline.

## Known gaps and cautions

- The manifest does not declare pg, nodemon, lazy, or xml2js although the runtime/start/import scripts reference them. A clean npm install is insufficient to reproduce all features.
- PostgreSQL connection details are embedded in source and no environment template is provided. Move configuration out of code before deployment; do not reuse historical embedded credentials.
- No lockfile, automated tests, or supported runtime pin is present. This is a historical prototype, not a verified production service.

## Ownership and contribution

Repository ownership is Rabeh-LLC-KSA; a named operational owner must be confirmed by maintainers. Submit a focused documentation/source change with evidence, validation results, and any deployment impact. Never paste credentials or personal customer data into issues or documentation. Preserve existing license and third-party notices; a documentation update does not grant new distribution rights.
