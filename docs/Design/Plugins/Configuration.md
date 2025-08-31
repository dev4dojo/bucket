# Configuration

Backends are activated through config:

```yaml
buckets:
  logs:
    backend: sqlite
    params:
      db_path: "/var/data/logs.db"
  files:
    backend: s3
    params:
      bucket_name: "my-bucket"
      region: "us-east-1"
```
