import numpy as np

embeddings = []
documents = []

def add_embedding(name: str, embedding: np.ndarray):
    embeddings.append(embedding)
    documents.append(name)

def get_embeddings():
    return np.array(embeddings), documents
