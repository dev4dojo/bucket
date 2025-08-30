### Metadata Engine

- **Storage**: SQLite database (`objects` table).
- **Schema**:

```sql
CREATE TABLE objects (
    id TEXT NOT NULL,               -- SHA1 of file
    timestamp DATETIME NOT NULL,    -- enrichment time
    metadata JSON NOT NULL CHECK (json_valid(metadata)),
    PRIMARY KEY (id, timestamp)
);
```

## Rules

- Append-only: no overwrites.
- Metadata stored as full JSON snapshot.
- `id` + `timestamp` ensure uniqueness.
- `metadata` may include:
    - Core fields: `size`, `mime`, `created_at`
    - Bucket-specific fields: user-defined
    - Provenance: `source` (stored inside JSON, not as extra column)

## Metadata Enrichment Model

* New metadata entries **never overwrite** old ones.
* If incoming metadata differs from latest snapshot → **insert new row**.
* If identical → ignored.
* Result: multiple records per file ID, one per enrichment.

### Example

```json
[
  {
    "id": "abcd1234...",
    "timestamp": "2025-08-28T10:00:00Z",
    "metadata": {
      "size": 123456,
      "mime": "application/pdf",
      "author": "Alice",
      "source": "import"
    }
  },
  {
    "id": "abcd1234...",
    "timestamp": "2025-09-01T12:15:00Z",
    "metadata": {
      "size": 123456,
      "mime": "application/pdf",
      "author": "Bob",
      "source": "manual_edit"
    }
  }
]
```

## Querying Modes

1. **Latest snapshot per object** (default view):

   ```sql
   SELECT * FROM objects o
   WHERE timestamp = (
       SELECT MAX(timestamp) FROM objects WHERE id = o.id
   );
   ```

2. **History for single object**:

   ```sql
   SELECT * FROM objects
   WHERE id = :sha1
   ORDER BY timestamp;
   ```

3. **Conflict detection (objects with multiple versions)**:

   ```sql
   SELECT id, COUNT(*) as versions
   FROM objects
   GROUP BY id
   HAVING versions > 1;
   ```

