import time
from models.model_loader import ModelLoader


class InferenceService:
    """
    Handles embedding generation and inference timing.
    """

    def __init__(self):
        self.loader = ModelLoader()
        self.model = None
        self.model_name = self.loader.model_name

    def _ensure_model_loaded(self):
        if self.model is None:
            self.model = self.loader.load()

    def embed(self, text: str):
        self._ensure_model_loaded()

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

    def embed_batch(self, texts: list[str]):
        self._ensure_model_loaded()

        start_time = time.perf_counter()
        embeddings = self.model.encode(texts).tolist()
        end_time = time.perf_counter()

        inference_time_ms = (end_time - start_time) * 1000
        dimension = len(embeddings[0]) if embeddings else 0

        return {
            "embeddings": embeddings,
            "batch_size": len(texts),
            "dimension": dimension,
            "model_name": self.model_name,
            "inference_time_ms": round(inference_time_ms, 3),
        }