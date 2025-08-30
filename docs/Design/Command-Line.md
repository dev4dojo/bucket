## CLI / API Design (Conceptual)

- `bucket put FILE [--metadata METADATA.json]`
  → Store file, insert base metadata snapshot.

- `bucket enrich ID METADATA.json`
  → Append new metadata snapshot if different from latest.

- `bucket get ID`
  → Retrieve file.

- `bucket meta ID [--history]`
  → Get metadata (latest by default, full history with flag).

- `bucket search QUERY`
  → Query metadata with filtering, grouping, etc.

- `bucket validate`
  → Run validator against all metadata using schema.

