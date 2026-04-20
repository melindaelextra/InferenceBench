from fastapi import APIRouter
from app.schemas.inference import EmbeddingRequest, EmbeddingResponse
from app.services.inference_service import InferenceService

router = APIRouter()
inference_service = InferenceService()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/embed", response_model=EmbeddingResponse)
def embed_text(request: EmbeddingRequest):
    return inference_service.embed(request.text)