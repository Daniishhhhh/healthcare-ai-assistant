# C:\Users\danis\OneDrive\Desktop\healthcare-ai-assistant\backend\database\chroma_client.py

import chromadb

try:
    from chromadb.config import Settings
except Exception:
    Settings = None


# ==========================================
# Persistent Storage Path
# ==========================================
CHROMA_PATH = "chroma_db"


# ==========================================
# Create Persistent Client Safely
# ==========================================
def _create_client():
    """
    Creates a ChromaDB persistent client with safe fallbacks.
    """

    try:
        if Settings:
            return chromadb.PersistentClient(
                path=CHROMA_PATH,
                settings=Settings(
                    anonymized_telemetry=False,
                    allow_reset=True
                )
            )
        else:
            return chromadb.PersistentClient(path=CHROMA_PATH)

    except Exception as e:
        print("⚠️ Chroma PersistentClient failed. Falling back to in-memory client.")
        print("Error:", e)

        return chromadb.Client()


# Global client instance
client = _create_client()


# ==========================================
# Collection Getter
# ==========================================
def get_collection(name: str):
    """
    Returns existing collection or creates new one.
    """
    return client.get_or_create_collection(name=name)


# ==========================================
# Delete Collection (For ingestion/testing)
# ==========================================
def delete_collection(name: str):
    """
    Deletes collection safely.
    """
    try:
        client.delete_collection(name=name)
        print(f"✅ Collection '{name}' deleted successfully.")
    except Exception:
        print(f"⚠️ Collection '{name}' not found.")
