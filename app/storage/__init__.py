"""
Manages database connections globally.
"""

import os
import psycopg2

# Select database type
DB_TYPE = os.getenv("DB_TYPE", "postgres")  # Default is PostgreSQL

# Define connection and cursor globally
if DB_TYPE == "postgres":
    # 🎯 Local VMS-PostgreSQL (stores metadata)
    DATABASE_URL = os.getenv(
        "DATABASE_VMS_URL",
        f"postgres://{os.getenv('VMS_POSTGRES_USER')}:{os.getenv('VMS_POSTGRES_PASSWORD')}@{os.getenv('VMS_POSTGRES_HOST')}:{os.getenv('VMS_POSTGRES_PORT')}/{os.getenv('VMS_POSTGRES_DB')}"
    )
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
else:
    raise ValueError(f"Unsupported database type: {DB_TYPE}")
