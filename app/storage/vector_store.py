"""
Handles vector storage and retrieval using FAISS.
"""

import faiss
import numpy as np
import uuid
import logging

logging.basicConfig(level=logging.DEBUG)

class VectorStore:
    """Manages vector storage and similarity search."""

    def __init__(self, dim=4096):
        """
        Initializes the vector storage.
        Args:
            dim (int): Dimension of the embeddings (4096 for DeepSeek, 1536 for OpenAI, etc.).
        """
        self.dim = dim
        self.index = faiss.IndexFlatL2(self.dim)  # FAISS L2 (Euclidean) index
        self.vector_id_map = {}  # Dictionary to track generated vector IDs

    def add_vectors(self, embeddings: list) -> list:
        """
        Stores embeddings in FAISS and returns generated vector IDs.
        Args:
            embeddings (list): List of embedding vectors.
        Returns:
            list: List of generated vector IDs.
        """
        embeddings_np = np.array(embeddings, dtype=np.float32)
        self.index.add(embeddings_np)

        # Generate unique vector IDs
        vector_ids = [str(uuid.uuid4()) for _ in embeddings]
        for i, vec_id in enumerate(vector_ids):
            self.vector_id_map[vec_id] = i  # Map UUID to FAISS index

        logging.debug(f"Stored {len(embeddings)} vectors in FAISS with generated IDs.")
        return vector_ids

    def search_vectors(self, query_vector: list, top_k: int) -> list:
        """
        Searches for the top-k closest vectors.
        Args:
            query_vector (list): The query embedding.
            top_k (int): Number of closest vectors to return.
        Returns:
            list: List of closest vector IDs.
        """
        query_np = np.array([query_vector], dtype=np.float32)
        distances, indices = self.index.search(query_np, top_k)
        
        # Convert FAISS indices to vector UUIDs
        vector_ids = [list(self.vector_id_map.keys())[idx] for idx in indices[0]]
        return vector_ids
