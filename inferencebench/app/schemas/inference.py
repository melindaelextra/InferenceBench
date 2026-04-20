from typing import List
from pydantic import BaseModel, Field


class EmbeddingRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text to embed")


class EmbeddingResponse(BaseModel):
    embedding: List[float]
    dimension: int
    model_name: str
    inference_time_ms: float