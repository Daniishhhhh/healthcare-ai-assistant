from openai import AzureOpenAI
from backend.config import AZURE_API_KEY, AZURE_ENDPOINT, CHAT_DEPLOYMENT

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version="2024-02-15-preview"
)


def generate_llm_response(user_query: str, prompt: str):

    system_prompt = """
You are a helpful healthcare AI assistant designed for rural communities.

GOALS:
- Provide safe medical guidance
- Explain possible causes clearly
- Suggest simple home care if safe
- Mention when to consult a doctor
- Mention emergency signs if relevant

SAFETY RULES:
- Do NOT diagnose
- Do NOT prescribe medicines
- Encourage professional medical consultation when needed
- Keep language simple and reassuring

Always include a short disclaimer.
"""

    response = client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
