import json
import time
from backend.database.chroma_client import client
from backend.services.embedding_service import generate_embedding


def ingest_symptom_cases(limit=3000, batch_size=50):

    print("Loading Healthcare dataset...")

    file_path = r"C:\Users\danis\OneDrive\Desktop\healthcare-ai-assistant\data\Healthcare.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data = data[:limit]

    print(f"Total records to ingest: {len(data)}")

    # 🔥 Delete old collection safely
    try:
        client.delete_collection("symptom_cases")
        print("Old symptom_cases collection deleted.")
    except:
        print("No previous collection found.")

    collection = client.get_or_create_collection("symptom_cases")

    total = len(data)

    for start in range(0, total, batch_size):

        end = min(start + batch_size, total)
        batch = data[start:end]

        documents = []
        embeddings = []
        ids = []

        for index, row in enumerate(batch, start=start):

            structured_text = (
                f"Patient Age: {row.get('Age', '')}. "
                f"Gender: {row.get('Gender', '')}. "
                f"Symptoms: {row.get('Symptoms', '')}. "
                f"Recorded Condition: {row.get('Disease', '')}."
            )

            embedding = generate_embedding(structured_text)

            documents.append(structured_text)
            embeddings.append(embedding)
            ids.append(f"case_{index}")

        collection.add(
            documents=documents,
            embeddings=embeddings,
            ids=ids
        )

        progress = round((end / total) * 100, 2)
        print(f"Processed {start} to {end} | Progress: {progress}%")

        time.sleep(1)  # avoid rate limit

    print("✅ Symptom cases ingestion completed successfully.")
