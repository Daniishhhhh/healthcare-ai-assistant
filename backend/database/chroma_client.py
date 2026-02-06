import chromadb

client = chromadb.Client()

def get_collection(name: str):
    return client.get_or_create_collection(name=name)
