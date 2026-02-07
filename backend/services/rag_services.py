from backend.services.retrieval_service import retrieve_context
from backend.services.llm_service import generate_llm_response
from backend.services.emergency_engine import check_emergency


CONFIDENCE_THRESHOLD = 60  # Adjustable


def generate_safe_response(user_query: str):
        # 🚨 Emergency override
    if check_emergency(user_query):
        return {
    "status": "EMERGENCY",
    "risk_level": "CRITICAL",
    "message": "...",
    "confidence": None
}



    retrieval_result = retrieve_context(user_query)

    guideline = retrieval_result["guideline"]

    # 🔒 Guardrail
    if guideline is None:
        return {
            "status": "INSUFFICIENT_CONTEXT",
            "message": "Insufficient verified medical information available.",
            "confidence": 0
        }

    confidence = guideline["confidence"]

    if confidence < CONFIDENCE_THRESHOLD:
        return {
            "status": "LOW_CONFIDENCE",
            "risk_level": "MODERATE",
            "message": "Insufficient verified medical information. Please consult a healthcare professional.",
            "confidence": confidence
}


    # ✅ If confidence acceptable → call LLM
    llm_response = generate_llm_response(
        user_query,
        guideline["text"]
    )

    return {
    "status": "SUCCESS",
    "risk_level": "LOW" if confidence > 75 else "MODERATE",
    "message": llm_response,
    "confidence": confidence
}
