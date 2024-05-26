from fastapi import APIRouter, Query
from typing import List
from app.utils.search_engine import perform_search

router = APIRouter()

@router.get("/docs")
async def search_documents(q: str):
    results = perform_search(q)
    return {"query": q, "results": results}
