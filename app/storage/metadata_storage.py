"""
Generic metadata storage using a pre-defined database connection.
"""

from app.storage import conn, cursor
import logging

logging.basicConfig(level=logging.DEBUG)

class MetadataStorage:
    """Handles metadata storage using a predefined database connection."""

    def __init__(self, memory_type: str):
        """Initialize with the specific memory type (economic, hacker, poet...)."""
        self.memory_type = memory_type
        self.table_name = f"{memory_type}_memory"  # Example: economic_memory, hacker_memory

    def fetch_data(self) -> list:
        """Fetch raw data from CRON-PostgreSQL for the specified memory type."""
        query = f"SELECT * FROM {self.table_name};"
        cursor.execute(query)
        return cursor.fetchall()

    def store_metadata(self, metadata: list):
        """
        Stores metadata in PostgreSQL.
        Args:
            metadata (list): List of metadata dictionaries with 'vector_id' key.
        """
        query = f"INSERT INTO {self.table_name} (vector_id, source_text, metadata) VALUES (%s, %s, %s);"
        values = [(m["vector_id"], m["source_text"], m["metadata"]) for m in metadata]

        cursor.executemany(query, values)
        conn.commit()
        logging.debug(f"Stored {len(metadata)} metadata entries in PostgreSQL.")

    def associate(self, vector_ids: list, raw_texts: list, extra_metadata: list) -> list:
        """
        Associates vector IDs with metadata.
        Args:
            vector_ids (list): List of vector IDs from FAISS.
            raw_texts (list): Corresponding raw texts.
            extra_metadata (list): Additional metadata.
        Returns:
            list: Structured metadata list.
        """
        metadata_entries = []
        for vec_id, text, meta in zip(vector_ids, raw_texts, extra_metadata):
            metadata_entries.append({
                "vector_id": vec_id,
                "source_text": text,
                "metadata": meta
            })
        
        logging.debug("Metadata successfully associated with vector IDs.")
        return metadata_entries