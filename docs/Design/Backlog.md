# Backlog

- Snowflake ID implementation (Python codec).
- Producer API (`append`, `commit`, `rollover`).
- Consumer API (`fetch_after`, `list_segments`).
- Matching consumer design spec (like this, but focused on read patterns and offset management)?
- Consumer Offset Tracker spec: so each consumer knows where it left off, independently of others)
- Global catalog: cross-bucket indexing & search.
- Distributed synchronization: merge metadata across nodes.
- Version labeling: ability to “approve” or “pin” a specific metadata snapshot.
- Compact backends: small files grouped into archives.
