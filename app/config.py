"""
Loads environment variables and configurations for database connections.
"""

import os

# 🎯 Local VMS-PostgreSQL (stores metadata)
DATABASE_VMS_URL = os.getenv(
    "DATABASE_VMS_URL",
    f"postgres://{os.getenv('VMS_POSTGRES_USER')}:{os.getenv('VMS_POSTGRES_PASSWORD')}@{os.getenv('VMS_POSTGRES_HOST')}:{os.getenv('VMS_POSTGRES_PORT')}/{os.getenv('VMS_POSTGRES_DB')}"
)

# 🌍 Remote CRON-PostgreSQL (source data)
DATABASE_CRON_URL = os.getenv(
    "DATABASE_CRON_URL",
    f"postgres://{os.getenv('CRON_POSTGRES_USER')}:{os.getenv('CRON_POSTGRES_PASSWORD')}@{os.getenv('CRON_POSTGRES_HOST')}:{os.getenv('CRON_POSTGRES_PORT')}/{os.getenv('CRON_POSTGRES_DB')}"
)
