# Usage

```python
from mysystem.core.loader import load_bucket
import mysystem.backends.sqlite_backend   # must import to register backend

config = {
    "backend": "sqlite",
    "params": {"db_path": "/tmp/test.db"}
}

bucket = load_bucket(config)
bucket.put_object("mybucket", "file1.txt", b"hello", {"author": "me"})
print(bucket.list_objects("mybucket"))
```
