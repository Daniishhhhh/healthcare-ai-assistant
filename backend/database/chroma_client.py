import chromadb
from chromadb.config import Settings

CHROMA_PATH = "chroma_db"

client = chromadb.PersistentClient(
    path=CHROMA_PATH,
    settings=Settings(
        anonymized_telemetry=False
    )
)

def get_collection(name: str):
    return client.get_or_create_collection(name=name)
