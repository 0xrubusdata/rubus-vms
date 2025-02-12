"""
Handles text preprocessing and embedding generation via the embedding API.
"""

import requests
import logging
from app.ingestion import EMBEDDING_API_URL

logging.basicConfig(level=logging.DEBUG)

class DataTransformer:
    """Transforms raw text into clean text and embeddings."""

    def preprocess(self, text: str) -> str:
        """
        Cleans and normalizes text before embedding.
        """
        cleaned_text = text.strip().lower()  # Basic cleaning
        return cleaned_text

    def embed(self, text: str, model: str = "llama3.2") -> list:
        """
        Converts cleaned text into an embedding using the configured embedding API.
        """
        payload = {"model": model, "text": text}
        try:
            logging.debug(f"Sending request to embedding API: {payload}")
            response = requests.get(EMBEDDING_API_URL, params=payload)
            response.raise_for_status()
            embedding = response.json()
            logging.debug(f"Received embedding: {embedding}")
            return embedding
        except requests.RequestException as e:
            logging.error(f"Error fetching embedding: {str(e)}")
            return None
