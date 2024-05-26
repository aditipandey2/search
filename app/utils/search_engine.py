from sentence_transformers import SentenceTransformer, util
import numpy as np
from typing import List
from app.data.embeddings_store import get_embeddings, add_embedding

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text: str) -> np.ndarray:
    return model.encode(text)

def perform_search(query: str) -> List[str]:
    query_embedding = embed_text(query)
    embeddings, documents = get_embeddings()
    
    scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    results = [documents[i] for i in scores.argsort(descending=True)]
    
    return results

def add_document(text: str, name: str):
    embedding = embed_text(text)
    add_embedding(name, embedding)
