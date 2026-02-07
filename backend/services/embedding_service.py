from openai import AzureOpenAI
from backend.config import AZURE_API_KEY, AZURE_ENDPOINT, EMBEDDING_DEPLOYMENT

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version="2024-02-15-preview"
)

def generate_embedding(text: str):
    response = client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT,
        input=text
    )
    return response.data[0].embedding
