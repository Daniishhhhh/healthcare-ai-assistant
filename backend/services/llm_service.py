from openai import AzureOpenAI
from backend.config import AZURE_API_KEY, AZURE_ENDPOINT, CHAT_DEPLOYMENT


# ==========================================
# AZURE CLIENT (NO LONG RETRIES)
# ==========================================

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version="2024-02-15-preview",
    max_retries=0   # ⭐ VERY IMPORTANT
)


# ==========================================
# FAST FALLBACK RESPONSE
# ==========================================

def fallback_response(query: str):

    return f"""
🩺 Health Guidance for: {query}

Possible Causes:
• Temporary body imbalance
• Stress or fatigue
• Mild infection or lifestyle factors

What You Can Do:
• Rest properly
• Drink enough water
• Eat light nutritious food
• Monitor symptoms

When to See a Doctor:
• Symptoms persist more than 2–3 days
• Symptoms worsen
• Repeated episodes occur

Emergency Signs:
• Severe pain
• Difficulty breathing
• Fainting
• Chest discomfort

⚠ Medical Disclaimer:
This AI provides general health information only.
It does NOT replace professional medical advice.
Always consult a qualified doctor for diagnosis.
"""


# ==========================================
# MAIN RESPONSE FUNCTION
# ==========================================

def generate_llm_response(user_input: str, system_prompt: str):

    try:

        response = client.chat.completions.create(
            model=CHAT_DEPLOYMENT,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        print("LLM ERROR:", e)
        return "Unable to retrieve information at the moment."
