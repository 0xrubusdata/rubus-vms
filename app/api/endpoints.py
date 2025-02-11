"""
Defines API routes using FastAPI.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    """Root endpoint to check if the API is running."""
    return {"message": "Vector Memory Service is running"}
