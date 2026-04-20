import time
from models.model_loader import ModelLoader


class InferenceService:
    """
    Handles embedding generation and inference timing.
    """

    def __init__(self):
        self.loader = ModelLoader()
        self.model = self.loader.load()
        self.model_name = self.loader.model_name

    def embed(self, text: str):
        start_time = time.perf_counter()

        embedding = self.model.encode(text).tolist()

        end_time = time.perf_counter()
        inference_time_ms = (end_time - start_time) * 1000

        return {
            "embedding": embedding,
            "dimension": len(embedding),
            "model_name": self.model_name,
            "inference_time_ms": round(inference_time_ms, 3),
        }