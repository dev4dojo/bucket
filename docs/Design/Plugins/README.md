# Plugins Approach

## Goal

To extend the system with a plug-in approach, so that different backends (e.g., local FS, S3, SQLite, etc.) can be “plugged in” to the core only when needed, instead of being tightly coupled.

## Core Principles

- Separation of Concerns: Core system defines only the *interfaces* and *contract* for backends.
- Lazy Loading: Backend is loaded only when configured/needed.
- Extensibility: New backends can be added without modifying the core.
Pluggability
- Backend lives in its own module/package, registered through a simple plug-in mechanism.

## Core System Responsibilities

- Maintain **bucket registry**.
- Define **Backend Interface** (abstract base class or protocol).
- Manage **configuration** (e.g., backend type, connection details).
- Expose **API** to operate on buckets without knowing the underlying backend.

## Advantages

* **Isolation**: Each backend is in its own module.
* **Optional dependencies**: Install only what you need 
  * `pip install bucket[sqlite]`, `bucket[s3]`).
* **Testability**: Mock/replace backends easily.
* **Extensibility**: Third parties can add their own backends without touching core.

## Read More

- [Install](Install.md)
- [Discovery](Discovery.md)
- [Configuration](Configuration.md)

