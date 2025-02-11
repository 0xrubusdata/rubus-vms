"""
Generic metadata storage using a pre-defined database connection.
"""

from app.storage import conn, cursor

class MetadataStorage:
    """Handles metadata storage using a predefined database connection."""

    def store_metadata(self, metadata: list):
        """Stores metadata in the database using a shared connection."""
        pass

    def get_metadata(self, vector_ids: list) -> list:
        """Retrieves metadata using a shared database connection."""
        pass
