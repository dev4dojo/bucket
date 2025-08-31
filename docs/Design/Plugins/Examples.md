# Example Backends

## SQLite

```python
# mysystem/backends/sqlite_backend.py
import sqlite3
from mysystem.core.backend_interface import Backend
from mysystem.core.registry import register_backend

class SQLiteBackend(Backend):
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self._init_schema()

    def _init_schema(self):
        c = self.conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS objects "
                  "(bucket TEXT, key TEXT, data BLOB, metadata TEXT)")
        self.conn.commit()

    def create_bucket(self, name: str): pass  # no-op for SQLite
    
    def put_object(self, bucket: str, key: str, data: bytes, metadata: dict):
        self.conn.execute(
            "INSERT INTO objects VALUES (?,?,?,?)",
            (bucket, key, data, str(metadata))
        )
        self.conn.commit()

    def get_object(self, bucket: str, key: str) -> bytes:
        row = self.conn.execute(
            "SELECT data FROM objects WHERE bucket=? AND key=?",
            (bucket, key)
        ).fetchone()
        return row[0] if row else None

    def list_objects(self, bucket: str) -> list[str]:
        return [
            r[0] for r in self.conn.execute(
                "SELECT key FROM objects WHERE bucket=?", (bucket,)
            )
        ]

register_backend("sqlite", SQLiteBackend)
```
