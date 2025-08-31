# Plugins Install

* `pip install mysystem` → installs only the **core system** (no backends).
* `pip install mysystem[sqlite]` → installs **core + SQLite backend deps**.
* `pip install mysystem[s3]` → installs **core + boto3**.
* `pip install mysystem[sqlite,s3]` → installs both optional deps.

## Core Loader

When a bucket is first accessed, the system instantiates the backend dynamically:

```python
from core.registry import get_backend

def load_bucket(name, config):
    backend_cls = get_backend(config["backend"])
    return backend_cls(**config["params"])
```

