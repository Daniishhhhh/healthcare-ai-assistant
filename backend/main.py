from fastapi import FastAPI
from backend.routes.chat import router as chat_router

app = FastAPI(title="Healthcare AI Assistant")

app.include_router(chat_router)

@app.get("/")
def health_check():
    return {"status": "Backend running"}
