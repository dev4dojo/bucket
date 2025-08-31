# Plug-in Discovery

Explicit registration: Backend registers itself in a registry dictionary.

Each backend calls this on import:

```python
# backends/sqlite_backend.py
from core.registry import register_backend
from core.backend_interface import Backend

class SQLiteBackend(Backend):
    # implement methods...
    pass

register_backend("sqlite", SQLiteBackend)
```
