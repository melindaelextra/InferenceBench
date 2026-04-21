import time
import numpy as np
from models.onnx_model_loader import ONNXModelLoader


class ONNXInferenceService:
    """
    Handles embedding generation using ONNX Runtime.
    """

    def __init__(self):
        self.loader = ONNXModelLoader()
        self.model = None
        self.tokenizer = None
        self.model_name = self.loader.model_name

    def _ensure_model_loaded(self):
        if self.model is None or self.tokenizer is None:
            self.model, self.tokenizer = self.loader.load()

    def _mean_pooling(self, token_embeddings, attention_mask):
        input_mask_expanded = np.expand_dims(attention_mask, axis=-1)
        sum_embeddings = np.sum(token_embeddings * input_mask_expanded, axis=1)
        sum_mask = np.clip(np.sum(input_mask_expanded, axis=1), a_min=1e-9, a_max=None)
        return sum_embeddings / sum_mask

    def embed(self, text: str):
        self._ensure_model_loaded()

        start_time = time.perf_counter()

        encoded_input = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            return_tensors="np"
        )

        outputs = self.model(**encoded_input)
        token_embeddings = outputs.last_hidden_state
        sentence_embedding = self._mean_pooling(
            token_embeddings,
            encoded_input["attention_mask"]
        )[0].tolist()

        end_time = time.perf_counter()

        return {
            "embedding": sentence_embedding,
            "dimension": len(sentence_embedding),
            "model_name": self.model_name,
            "inference_time_ms": round((end_time - start_time) * 1000, 3),
            "cache_hit": False,
        }