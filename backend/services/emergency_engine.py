EMERGENCY_KEYWORDS = [
    "chest pain",
    "shortness of breath",
    "unconscious",
    "severe bleeding",
    "stroke",
    "heart attack",
    "suicidal",
    "not breathing"
]

def check_emergency(user_query: str):

    query_lower = user_query.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in query_lower:
            return True

    return False
