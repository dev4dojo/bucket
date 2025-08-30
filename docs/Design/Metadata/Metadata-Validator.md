# Metadata Validator (Optional)

- Purpose: Enforce schema rules.
- Schema files: JSON Schema stored alongside bucket (`metadata_schema.json`).
- Execution:
  * Inline (during `put`/`enrich`)
  * Or offline audit (`validate-bucket`)

## Responsibility

- Core bucket: only ensures JSON validity.
- Validator: checks semantics (required fields, types, ranges, enums).
