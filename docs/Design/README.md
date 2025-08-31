# Overview

This system manages files on a local filesystem using the **bucket abstraction**. Each bucket is a self-contained unit consisting of:

* **Bucket backend** — handles file storage (`get`, `put`, `delete`, `exists`).
* **Metadata engine** — tracks metadata for stored files in an append-only model.
* **(Optional) Metadata validator** — enforces schema rules externally.

Goals:

* Deduplicate files via SHA1 identifiers.
* Store and enrich metadata without overwriting history.
* Support heterogeneous metadata across buckets.
* Enable flexible backends (plain files, archives, custom storage).

## Design Principles

- **Buckets are self-contained** (backend + SQLite + optional schema).
- **File identity = SHA1**, immutable, deduplication by design.
- **Metadata is JSON-only** (flexible, schema-driven externally).
- **Enrichment is append-only**, no overwrites.
- **Validation decoupled**: handled by optional component, not core.
- **Source info lives inside metadata**, not separate columns.
- **Backend API is minimal**: `get/put/delete/exists`.

