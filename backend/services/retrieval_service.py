from backend.services.embedding_service import generate_embedding
from backend.database.chroma_client import client
from backend.services.confidence_engine import calculate_confidence, classify_confidence


def retrieve_context(user_query: str):

    query_embedding = generate_embedding(user_query)

    # --- Medical Guidelines Retrieval ---
    guideline_collection = client.get_or_create_collection("medical_guidelines")

    guideline_results = guideline_collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    # --- Symptom Pattern Retrieval ---
    symptom_collection = client.get_or_create_collection("symptom_patterns")

    symptom_results = symptom_collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    response_data = {}

    # --- Process Guideline Result ---
    if guideline_results["documents"][0]:
        guideline_doc = guideline_results["documents"][0][0]
        guideline_distance = guideline_results["distances"][0][0]

        confidence = calculate_confidence(guideline_distance)
        level = classify_confidence(confidence)

        response_data["guideline"] = {
            "text": guideline_doc,
            "confidence": confidence,
            "level": level
        }
    else:
        response_data["guideline"] = None

    # --- Process Symptom Results ---
    symptom_docs = symptom_results["documents"][0]
    symptom_distances = symptom_results["distances"][0]

    symptom_matches = []

    for doc, dist in zip(symptom_docs, symptom_distances):
        confidence = calculate_confidence(dist)

        symptom_matches.append({
            "text": doc,
            "confidence": confidence
        })

    response_data["symptoms"] = symptom_matches

    return response_data
