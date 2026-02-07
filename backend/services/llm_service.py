from openai import AzureOpenAI
from backend.config import AZURE_API_KEY, AZURE_ENDPOINT, CHAT_DEPLOYMENT

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version="2024-02-15-preview"
)

def generate_llm_response(user_query: str, context: str):

    system_prompt = """
You are a healthcare assistant.

STRICT RULES:
- Use ONLY the provided context.
- Do NOT add new symptoms.
- Do NOT add new medical advice beyond the context.
- Do NOT diagnose.
- Do NOT prescribe medication.
- If context does not mention something, do not invent it.
- Keep response short and factual.
"""


    response = client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context:\n{context}\n\nUser Query:\n{user_query}"}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
