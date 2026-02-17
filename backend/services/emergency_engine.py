"""
Emergency Detection Engine
Smart triage system for healthcare chatbot demo

Author: Swasthya Setu AI
"""


CRITICAL_KEYWORDS = [
    # Cardiac / Breathing
    "chest pain",
    "severe chest pain",
    "heart attack",
    "left arm pain",
    "radiating pain",
    "difficulty breathing",
    "shortness of breath",
    "cannot breathe",

    # Neuro
    "stroke",
    "seizure",
    "unconscious",
    "fainting",
    "confusion",

    # Trauma
    "severe bleeding",
    "head injury",
    "accident",

    # Oxygen / Collapse
    "oxygen low",
    "collapsed"
]


MODERATE_KEYWORDS = [
    "high fever",
    "persistent vomiting",
    "severe headache",
    "migraine",
    "dizziness",
    "blood pressure high",
    "low blood pressure",
    "severe pain",
    "continuous vomiting"
]


LOW_KEYWORDS = [
    "cough",
    "cold",
    "mild fever",
    "body pain",
    "headache",
    "sore throat",
    "runny nose"
]


# Hindi support (basic demo level)
HINDI_CRITICAL = [
    "सीने में दर्द",
    "सांस लेने में दिक्कत",
    "बेहोश",
    "दौरा",
    "स्ट्रोक"
]

HINDI_MODERATE = [
    "तेज बुखार",
    "उल्टी",
    "चक्कर",
    "माइग्रेन"
]


def detect_risk_level(query: str) -> str:

    q = query.lower()

    # Context aware rule
    if "cough" in q and ("breathing" in q or "breath" in q):
        return "CRITICAL"

    # English critical
    for word in CRITICAL_KEYWORDS:
        if word in q:
            return "CRITICAL"

    # Hindi critical
    for word in HINDI_CRITICAL:
        if word in query:
            return "CRITICAL"

    # Moderate
    for word in MODERATE_KEYWORDS:
        if word in q:
            return "MODERATE"

    for word in HINDI_MODERATE:
        if word in query:
            return "MODERATE"

    # Low
    return "LOW"


def check_emergency(query: str):
    """
    Returns emergency response object if critical
    Otherwise returns None
    """

    risk = detect_risk_level(query)

    if risk == "CRITICAL":

        return {
            "status": "EMERGENCY",
            "risk_level": "CRITICAL",
            "risk_color": "RED",
            "confidence": 95.0,
            "message": (
                "🚨 Your symptoms may indicate a medical emergency.\n\n"
                "Please seek immediate medical attention or call emergency services (108 in India) immediately.\n\n"
                "Do not delay care."
            ),
            "confidence_explanation": "Critical symptom pattern detected.",
            "sources": []
        }

    return None
