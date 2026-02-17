import json
from backend.services.retrieval_service import retrieve_context
from backend.services.llm_service import generate_llm_response
from backend.services.emergency_engine import check_emergency
from backend.utils.logger import logger
from backend.services.language_service import (
    detect_language,
    translate_to_english,
    translate_from_english
)

CONFIDENCE_THRESHOLD = 20


# ==========================================================
# SIMPLE RISK DETECTOR (Demo Friendly)
# ==========================================================
def detect_risk_level(query: str):

    q = query.lower()

    critical_keywords = [
        "chest pain", "heart attack", "unconscious", "not breathing",
        "stroke", "seizure", "severe bleeding", "suicide"
    ]

    moderate_keywords = [
        "fever", "vomiting", "infection", "pain", "dizziness",
        "blood pressure", "diabetes"
    ]

    if any(k in q for k in critical_keywords):
        return "CRITICAL", "RED"

    if any(k in q for k in moderate_keywords):
        return "MODERATE", "ORANGE"

    return "LOW", "GREEN"


# ==========================================================
# MAIN SAFE RESPONSE ENGINE
# ==========================================================
def generate_safe_response(user_query: str):

    logger.info(f"Incoming Query: {user_query}")

    # ==========================================
    # 🌍 Detect Language
    # ==========================================
    detected_lang = detect_language(user_query)

    if detected_lang != "en":
        user_query_en = translate_to_english(user_query)
    else:
        user_query_en = user_query

    # ==========================================
    # 🚨 Emergency Override
    # ==========================================
    emergency_result = check_emergency(user_query_en)
    if emergency_result:
        logger.warning("Emergency detected.")
        return emergency_result

    # ==========================================
    # 📊 Risk Detection
    # ==========================================
    risk_level, risk_color = detect_risk_level(user_query_en)

    # ==========================================
    # 📚 Retrieve Context
    # ==========================================
    retrieval_result = retrieve_context(user_query_en)

    guideline = retrieval_result.get("guideline")

    context_text = ""
    confidence = 50  # default demo confidence

    if guideline:
        context_text = guideline["text"]
        confidence = guideline.get("confidence", 60)

    # ==========================================
    # 🤖 LLM FALLBACK (Always respond)
    # ==========================================
    medical_prompt = f"""
User Query: {user_query_en}

Context (if available):
{context_text}

Provide a helpful healthcare response including:

1. Possible causes
2. Home care or precautions
3. When to see a doctor
4. Emergency warning signs (if relevant)
5. Simple language suitable for rural users

Add a short safety disclaimer at the end.

Do NOT prescribe medicines.
Do NOT claim diagnosis.
"""

    llm_response = generate_llm_response(user_query_en, medical_prompt)

    if detected_lang != "en":
        llm_response = translate_from_english(llm_response, detected_lang)

    logger.info("LLM response generated successfully.")

    return {
        "status": "SUCCESS",
        "risk_level": risk_level,
        "risk_color": risk_color,
        "confidence": confidence,
        "message": llm_response,
        "confidence_explanation": "Demo confidence score based on AI medical reasoning.",
        "sources": []
    }


# ==========================================================
# GOVERNMENT SCHEME INFORMATION
# ==========================================================
def generate_scheme_info(query: str):

    prompt = f"""
You are a healthcare assistant providing official Indian government health scheme information.

Return ONLY valid JSON in this format:

{{
  "description": "",
  "eligibility": "",
  "benefits": "",
  "official_source": ""
}}

Rules:
- Do NOT include explanations outside JSON.
- Official source must be real government website if known.
- Keep response concise.

Query: {query}
"""

    raw_response = generate_llm_response(query, prompt)

    try:
        parsed = json.loads(raw_response or "{}")
        parsed["disclaimer"] = (
            "Information based on publicly available government sources. "
            "Please verify on official portal."
        )
        return parsed
    except Exception:
        return {
            "description": raw_response,
            "eligibility": "",
            "benefits": "",
            "official_source": "Refer official government portal",
            "disclaimer": "Information may not be fully structured. Please verify officially."
        }
# ==========================================================
# GOVERNMENT SCHEME INFORMATION (STRICT JSON)
# ==========================================================
def generate_scheme_info(query: str):

    system_prompt = """
You are an expert assistant for Indian Government Health Schemes.

Return ONLY valid JSON in this format:

{
  "description": "",
  "eligibility": "",
  "benefits": "",
  "official_source": ""
}

Rules:
- Do NOT include numbering
- Do NOT include explanations outside JSON
- Keep text concise and factual
- Official source should be government website if known
- If unsure use: "Refer official government portal"
"""

    prompt = f"Provide information for scheme: {query}"

    raw_response = generate_llm_response(prompt, system_prompt)

    try:
        parsed = json.loads(raw_response)

        parsed["disclaimer"] = (
            "Information based on publicly available government sources. "
            "Please verify on official portal."
        )

        return parsed

    except Exception:

        # Fallback clean structure
        return {
            "description": raw_response,
            "eligibility": "Refer official government portal",
            "benefits": "Refer official government portal",
            "official_source": "Refer official government portal",
            "disclaimer": "Information may not be fully structured. Please verify officially."
        }
