from pydantic import BaseModel
from typing import Optional, List


class SourceItem(BaseModel):
    text: str
    confidence: float


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    status: str
    risk_level: str
    confidence: Optional[float]
    message: str
    sources: Optional[List[SourceItem]] = None