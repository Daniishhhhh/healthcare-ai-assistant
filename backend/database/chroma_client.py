import chromadb
from chromadb.config import Settings

import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"

# ==============================
# CHROMA CLIENT (Telemetry OFF)
# ==============================

client = chromadb.PersistentClient(
    path="chroma_db",
    settings=Settings(
        anonymized_telemetry=False,
        allow_reset=True
    )
)


# ==============================
# COLLECTIONS
# ==============================

guideline_collection = client.get_or_create_collection(
    name="guidelines"
)

pattern_collection = client.get_or_create_collection(
    name="patterns"
)

case_collection = client.get_or_create_collection(
    name="cases"
)
