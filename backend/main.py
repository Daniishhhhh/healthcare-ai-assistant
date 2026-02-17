
from backend.models.response_models import ChatRequest, ChatResponse
from backend.services.rag_services import generate_safe_response, generate_scheme_info
import os
os.environ["CHROMA_TELEMETRY"] = "FALSE"
os.environ["ANONYMIZED_TELEMETRY"] = "FALSE"


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Healthcare AI Chatbot ",
    description="Safety-first multilingual healthcare assistant",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def root():
    return {"message": "Healthcare AI Backend Running"}


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    return generate_safe_response(request.query)


@app.post("/scheme")
def scheme_endpoint(request: ChatRequest):
    result = generate_scheme_info(request.query)

    return {
        "status": "SCHEME_INFO",
        "scheme_data": result
    }
