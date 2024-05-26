from fastapi import FastAPI
from app.api import upload, search

app = FastAPI()

app.include_router(upload.router)
app.include_router(search.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to MindTickle Semantic Search API!"}
