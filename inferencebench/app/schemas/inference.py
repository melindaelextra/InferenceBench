"""Inference request/response schemas."""

from dataclasses import dataclass
from typing import Any


@dataclass
class InferenceRequest:
    """Input payload for inference."""

    prompt: str


@dataclass
class InferenceResponse:
    """Output payload for inference."""

    result: Any
