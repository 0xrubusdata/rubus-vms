"""
Handles data fetching from CRON-PostgreSQL.
"""

from app.ingestion import conn, cursor  # Uses the ingestion database connection

class DataFetcher:
    """Fetches raw data from CRON-PostgreSQL for a specific data source."""

    def __init__(self, source: str):
        """Initialize with the specific data source (europarl, eurostat, federal_reserve...)."""
        self.source_table = source  # Example: "europarl", "eurostat", "federal_reserve"

    def fetch_data(self) -> list:
        """Fetch raw data from CRON-PostgreSQL for the specified source."""
        query = f"SELECT * FROM {self.source_table};"
        cursor.execute(query)
        return cursor.fetchall()
