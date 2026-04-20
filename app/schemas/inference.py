from typing import List
from pydantic import BaseModel, Field


class EmbeddingRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text to embed")


class EmbeddingResponse(BaseModel):
    embedding: List[float]
    dimension: int
    model_name: str
    inference_time_ms: float
    cache_hit: bool


class BatchEmbeddingRequest(BaseModel):
    texts: List[str] = Field(..., min_length=1, description="List of input texts to embed")


class BatchEmbeddingResponse(BaseModel):
    embeddings: List[List[float]]
    batch_size: int
    dimension: int
    model_name: str
    inference_time_ms: float
    cache_hits: int