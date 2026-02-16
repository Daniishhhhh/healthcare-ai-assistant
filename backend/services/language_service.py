from backend.services.llm_service import generate_llm_response


def detect_language(text: str) -> str:
    prompt = f"""
Detect the language of the following text.
Return only ISO language code like:
en, hi, ta, te, kn, ml, ur

Text: {text}
"""
    return (generate_llm_response(text, prompt) or "").strip().lower()


def translate_to_english(text: str) -> str:
    prompt = f"Translate this to English:\n\n{text}"
    return (generate_llm_response(text, prompt) or "").strip()


def translate_from_english(text: str, target_lang: str) -> str:
    prompt = f"Translate this to {target_lang} language:\n\n{text}"
    return (generate_llm_response(text, prompt) or "").strip()
