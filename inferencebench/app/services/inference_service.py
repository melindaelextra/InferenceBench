"""Business logic for inference."""

from app.schemas.inference import InferenceRequest, InferenceResponse


def run_inference(request: InferenceRequest) -> InferenceResponse:
    """Return a simple baseline inference response."""
    return InferenceResponse(result={"echo": request.prompt})
