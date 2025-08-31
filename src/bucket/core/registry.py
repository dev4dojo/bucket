BACKENDS = {}


def register_backend(name: str, backend_cls):
    """
    Register a backend class with a given name.
    """
    BACKENDS[name] = backend_cls


def get_backend(name: str):
    """
    Retrieve a backend class by its registered name.
    """
    return BACKENDS[name]
