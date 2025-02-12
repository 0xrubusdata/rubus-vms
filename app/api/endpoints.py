"""
Defines API routes using FastAPI.
"""

from fastapi import APIRouter, HTTPException
from app.ingestion.transformer import DataTransformer
from app.storage.vector_store import VectorStore
from app.storage.metadata_storage import MetadataStorage
import logging

router = APIRouter()

@router.get("/")
def read_root():
    """Root endpoint to check if the API is running."""
    return {"message": "Vector Memory Service is running"}

"""
API endpoints for querying the vector memory.
"""

@router.get("/api/search")
async def search_endpoint(model: str, memory_type: str, query: str, top_k: int = 5):
    """
    API endpoint to search in the vector memory.
    
    Args:
        model (str): The embedding model to use (e.g., "llama3.2", "deepseek-r1:8b").
        memory_type (str): The type of memory to search in (e.g., "economic", "hacker").
        query (str): The user's search query.
        top_k (int, optional): Number of top results to return. Defaults to 5.

    Returns:
        dict: The search results with metadata.
    """
    logging.info(f"🔍 Searching in {memory_type} memory using {model} for query: {query}")

    try:
        # 1️⃣ Convert query into embedding
        transformer = DataTransformer()
        query_vector = transformer.embed(query, model)
        if query_vector is None:
            raise HTTPException(status_code=500, detail="Failed to generate embedding.")

        # 2️⃣ Search for the closest vectors
        vector_store = VectorStore()
        vector_ids = vector_store.search_vectors(query_vector, top_k)
        if not vector_ids:
            return {"message": "No relevant results found."}

        # 3️⃣ Retrieve metadata for the matched vectors
        metadata_storage = MetadataStorage(memory_type)
        metadata_results = metadata_storage.get_metadata(vector_ids)

        return {"results": metadata_results}

    except Exception as e:
        logging.error(f"Error during search: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during search.")

