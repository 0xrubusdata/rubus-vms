"""
Manages database connections and embedding API configuration.
"""

import os
import psycopg2

# Select database type
DB_TYPE = os.getenv("DB_TYPE", "postgres")  # Default is PostgreSQL

# 🌍 Remote CRON-PostgreSQL (source data)
DATABASE_URL = os.getenv(
    "DATABASE_CRON_URL",
    f"postgres://{os.getenv('CRON_POSTGRES_USER')}:{os.getenv('CRON_POSTGRES_PASSWORD')}@{os.getenv('CRON_POSTGRES_HOST')}:{os.getenv('CRON_POSTGRES_PORT')}/{os.getenv('CRON_POSTGRES_DB')}"
)

# Initialize PostgreSQL connection for data fetching
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# 🌐 Embedding API configuration (local or remote)
EMBEDDING_API_URL = os.getenv(
    "EMBEDDING_API_URL",
    "http://localhost:8001/api/embedding"  # Default: local API
)
