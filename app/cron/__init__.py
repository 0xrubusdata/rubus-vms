"""
Handles periodic execution of the ingestion service.
"""

import schedule
import time
from app.cron.ingestion_service import IngestionService
import logging

logging.basicConfig(level=logging.INFO)

def job():
    """Runs the ingestion pipeline periodically."""
    logging.info("⏳ Running scheduled ingestion job...")
    
    # Example: Ingest different memory types
    for memory_type in ["economic", "hacker", "poet"]:
        service = IngestionService(memory_type)
        service.run()

    logging.info("✅ Scheduled ingestion job completed.")

# Schedule the job to run every 24 hours
schedule.every().day.at("00:00").do(job)

if __name__ == "__main__":
    logging.info("🕒 Scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
