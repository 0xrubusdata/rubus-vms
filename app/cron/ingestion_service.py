"""
Handles automated data ingestion, transformation, and vectorization.
"""

from app.ingestion.fetcher import DataFetcher
from app.ingestion.transformer import DataTransformer
from app.storage.vector_store import VectorStore
from app.storage.metadata_storage import MetadataStorage
import logging

logging.basicConfig(level=logging.INFO)

class IngestionService:
    """Handles the full ingestion and vectorization pipeline."""

    def __init__(self, memory_type: str, model: str = "llama3.2"):
        """
        Initializes the ingestion service.
        Args:
            memory_type (str): The type of memory (economic, hacker, poet...).
            model (str): The embedding model to use.
        """
        self.memory_type = memory_type
        self.model = model
        self.fetcher = DataFetcher(memory_type)
        self.transformer = DataTransformer()
        self.vector_store = VectorStore()
        self.metadata_storage = MetadataStorage(memory_type)

    def run(self):
        """Executes the full data ingestion process."""
        logging.info(f"🚀 Starting ingestion for {self.memory_type} memory.")

        # 1️⃣ Fetch data
        raw_data = self.fetcher.fetch_data()
        if not raw_data:
            logging.info("No new data found.")
            return

        texts = [entry[1] for entry in raw_data]  # Assuming text is in the second column

        # 2️⃣ Preprocess texts
        cleaned_texts = [self.transformer.preprocess(text) for text in texts]

        # 3️⃣ Generate embeddings
        embeddings = [self.transformer.embed(text, self.model) for text in cleaned_texts]

        # 4️⃣ Store embeddings in FAISS
        vector_ids = self.vector_store.add_vectors(embeddings)

        # 5️⃣ Associate metadata and store it in PostgreSQL
        metadata = self.metadata_storage.associate(vector_ids, texts, [{} for _ in texts])
        self.metadata_storage.store_metadata(metadata)

        logging.info(f"✅ Ingestion for {self.memory_type} completed successfully.")
