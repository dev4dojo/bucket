# Bucket Backend

* **Purpose**: Store raw file content.
* **Identity**: Files are stored by **SHA1 hash** as filename.
* **Structure**: Pair-tree directory layout (scales well for many files).
* **Operations**:

  * `put(file)` → stores file under SHA1
  * `get(sha1)` → retrieves file
  * `delete(sha1)` → removes file
  * `exists(sha1)` → checks presence

- Backend type chosen at bucket creation (e.g., filesystem, archive-based).
- No tracking of backend type/config in metadata — handled by setup/runtime.
