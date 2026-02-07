import json
import os
import time
from backend.services.embedding_service import client
from backend.database.chroma_client import client as chroma_client
from backend.config import EMBEDDING_DEPLOYMENT

BASE_PATH = r"C:\Users\danis\OneDrive\Desktop\healthcare-ai-assistant"
DATA_PATH = os.path.join(BASE_PATH, "data", "healthcare_500.json")

BATCH_SIZE = 50


def ingest_symptom_patterns():

    if DEV_MODE:
        try:
            chroma_client.delete_collection("symptom_patterns")
            print("Old symptom collection deleted (DEV MODE).")
        except:
            pass

    collection = chroma_client.get_or_create_collection("symptom_patterns")

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    total = len(data)
    print(f"Total records to ingest: {total}")

    for i in range(0, total, BATCH_SIZE):

        batch = data[i:i+BATCH_SIZE]

        texts = []
        ids = []
        metadatas = []

        for idx, record in enumerate(batch):
            symptoms = record["Symptoms"]
            text = f"Symptom pattern: {symptoms}"

            texts.append(text)

            # 🔥 Force unique ID using index
            ids.append(f"symptom_{i + idx}")

            metadatas.append({
                "symptom_count": record["Symptom_Count"]
            })

        response = client.embeddings.create(
            model=EMBEDDING_DEPLOYMENT,
            input=texts
        )

        embeddings = [item.embedding for item in response.data]

        collection.upsert(
            documents=texts,
            embeddings=embeddings,
            ids=ids,
            metadatas=metadatas
        )

        print(f"Processed batch {i} to {i + len(batch)}")

        time.sleep(1)

    print("Batch ingestion completed successfully.")
