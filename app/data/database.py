documents = {}

def save_document(name: str, text: str):
    documents[name] = text
    return documents[name]

def get_document(name: str) -> str:
    return documents.get(name)
