# C:\Users\danis\OneDrive\Desktop\healthcare-ai-assistant\backend\services\retrieval_service.py

from backend.services.embedding_service import generate_embedding
from backend.database.chroma_client import client
from backend.services.confidence_engine import calculate_confidence, classify_confidence


def retrieve_context(user_query: str):

    query_embedding = generate_embedding(user_query)

    response_data = {}

    # ==============================
    # 1️⃣ MEDICAL GUIDELINES
    # ==============================
    guideline_collection = client.get_or_create_collection("medical_guidelines")

    guideline_results = guideline_collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    guideline_docs = guideline_results.get("documents")
    guideline_dists = guideline_results.get("distances")
    
    if (guideline_docs and 
        guideline_dists and 
        len(guideline_docs) > 0 and 
        len(guideline_dists) > 0 and 
        guideline_docs[0] and 
        guideline_dists[0] and
        len(guideline_docs[0]) > 0 and
        len(guideline_dists[0]) > 0):
        guideline_doc = guideline_docs[0][0]
        guideline_distance = guideline_dists[0][0]

        confidence = calculate_confidence(guideline_distance)
        level = classify_confidence(confidence)

        response_data["guideline"] = {
            "text": guideline_doc,
            "confidence": confidence,
            "level": level
        }
    else:
        response_data["guideline"] = None


    # ==============================
    # 2️⃣ SYMPTOM PATTERNS
    # ==============================
    pattern_collection = client.get_or_create_collection("symptom_patterns")

    pattern_results = pattern_collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    pattern_matches = []

    pattern_docs = pattern_results.get("documents")
    pattern_dists = pattern_results.get("distances")
    if (pattern_docs and 
        pattern_dists and
        len(pattern_docs) > 0 and 
        len(pattern_dists) > 0 and
        pattern_docs[0] and
        pattern_dists[0]):
        for doc, dist in zip(pattern_docs[0], pattern_dists[0]):
            pattern_matches.append({
                "text": doc,
                "confidence": calculate_confidence(dist)
            })

    response_data["patterns"] = pattern_matches


    # ==============================
    # 3️⃣ REAL PATIENT CASES (NEW)
    # ==============================
    case_collection = client.get_or_create_collection("symptom_cases")

    case_results = case_collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    case_matches = []

    if case_results:
        docs = case_results.get("documents")
        dists = case_results.get("distances")
        if docs and len(docs) > 0 and docs[0]:
            if dists and len(dists) > 0 and dists[0]:
                for doc, dist in zip(docs[0], dists[0]):
                    case_matches.append({
                        "text": doc,
                        "confidence": calculate_confidence(dist)
                    })

    response_data["cases"] = case_matches

    return response_data
