from abc import ABC, abstractmethod


class Backend(ABC):
    """
    Abstract base class for bucket storage backends.
    """

    @abstractmethod
    def create_bucket(self, name: str):
        """
        Create a new bucket with the given name.
        """
        pass

    @abstractmethod
    def put(self, bucket: str, key: str, data: bytes, metadata: dict):
        """
        Store an object in the specified bucket with the given key, data, and metadata.
        """
        pass

    @abstractmethod
    def get(self, bucket: str, key: str) -> bytes:
        """
        Retrieve an object from the specified bucket using the given key.
        """
        pass

    @abstractmethod
    def list(self, bucket: str) -> list[str]:
        """
        List all object keys in the specified bucket.
        """
        pass
