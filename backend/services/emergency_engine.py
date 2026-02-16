def check_emergency(query: str):

    emergency_keywords = [
        "chest pain",
        "severe chest pain",
        "radiating pain",
        "left arm pain",
        "heart attack",
        "unconscious",
        "difficulty breathing",
        "severe bleeding",
        "stroke",
        "seizure"
    ]

    query_lower = query.lower()

    for keyword in emergency_keywords:
        if keyword in query_lower:
            return {
                "status": "EMERGENCY",
                "risk_level": "CRITICAL",
                "risk_color": "RED",
                "confidence": 100.0,
                "message": "Your symptoms indicate a possible medical emergency. Please seek immediate medical attention or call your local emergency number immediately.",
                "confidence_explanation": "Emergency keyword match detected.",
                "sources": []
            }

    return None
