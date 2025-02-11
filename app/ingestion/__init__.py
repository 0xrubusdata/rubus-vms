"""
Manages database connections globally.
"""

import os
import psycopg2

# Select database type
DB_TYPE = os.getenv("DB_TYPE", "postgres")  # Default is PostgreSQL

# Define connection and cursor globally
if DB_TYPE == "postgres":
    # 🌍 Remote CRON-PostgreSQL (source data)   
    DATABASE_URL = os.getenv(
        "DATABASE_CRON_URL",
        f"postgres://{os.getenv('CRON_POSTGRES_USER')}:{os.getenv('CRON_POSTGRES_PASSWORD')}@{os.getenv('CRON_POSTGRES_HOST')}:{os.getenv('CRON_POSTGRES_PORT')}/{os.getenv('CRON_POSTGRES_DB')}"
    )
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
else:
    raise ValueError(f"Unsupported database type: {DB_TYPE}")
