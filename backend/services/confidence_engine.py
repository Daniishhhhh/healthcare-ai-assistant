def calculate_confidence(distance: float) -> float:
    confidence = (1 - distance) * 100
    confidence = max(0, min(confidence, 100))  # clamp 0–100
    return round(confidence, 2)


def classify_confidence(confidence: float) -> str:
    if confidence >= 75:
        return "HIGH"
    elif confidence >= 60:
        return "MODERATE"
    else:
        return "LOW"
