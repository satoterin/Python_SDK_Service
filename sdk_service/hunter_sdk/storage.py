class InMemoryStorage:
    """In-memory storage for data."""

    def __init__(self) -> None:
        self._storage: dict[str, dict] = {}

    def create(self, key: str, store: dict) -> None:
        """Create a new entry in storage."""
        self._storage[key] = store

    def read(self, key: str) -> dict:
        """Read an entry from storage."""
        return self._storage.get(key, {})

    def update(self, key: str, store: dict) -> None:
        """Update an existing entry in storage."""
        self._storage[key] = store

    def delete(self, key: str) -> None:
        """Delete an entry from storage."""
        self._storage.pop(key, None)

    def view_storage(self) -> dict:
        """View the current state of the storage"""
        return self._storage