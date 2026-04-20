import time
from models.model_loader import ModelLoader


class InferenceService:
    """
    Handles embedding generation, batching, caching, and inference timing.
    """

    def __init__(self):
        self.loader = ModelLoader()
        self.model = None
        self.model_name = self.loader.model_name
        self.cache = {}

    def _ensure_model_loaded(self):
        if self.model is None:
            self.model = self.loader.load()

    def embed(self, text: str):
        if text in self.cache:
            embedding = self.cache[text]
            return {
                "embedding": embedding,
                "dimension": len(embedding),
                "model_name": self.model_name,
                "inference_time_ms": 0.0,
                "cache_hit": True,
            }

        self._ensure_model_loaded()

        start_time = time.perf_counter()
        embedding = self.model.encode(text).tolist()
        end_time = time.perf_counter()

        self.cache[text] = embedding

        inference_time_ms = (end_time - start_time) * 1000

        return {
            "embedding": embedding,
            "dimension": len(embedding),
            "model_name": self.model_name,
            "inference_time_ms": round(inference_time_ms, 3),
            "cache_hit": False,
        }

    def embed_batch(self, texts: list[str]):
        self._ensure_model_loaded()

        start_time = time.perf_counter()

        embeddings = []
        uncached_texts = []
        uncached_indices = []
        cache_hits = 0

        for i, text in enumerate(texts):
            if text in self.cache:
                embeddings.append(self.cache[text])
                cache_hits += 1
            else:
                embeddings.append(None)
                uncached_texts.append(text)
                uncached_indices.append(i)

        if uncached_texts:
            new_embeddings = self.model.encode(uncached_texts).tolist()
            for idx, text, emb in zip(uncached_indices, uncached_texts, new_embeddings):
                embeddings[idx] = emb
                self.cache[text] = emb

        end_time = time.perf_counter()

        inference_time_ms = (end_time - start_time) * 1000
        dimension = len(embeddings[0]) if embeddings else 0

        return {
            "embeddings": embeddings,
            "batch_size": len(texts),
            "dimension": dimension,
            "model_name": self.model_name,
            "inference_time_ms": round(inference_time_ms, 3),
            "cache_hits": cache_hits,
        }