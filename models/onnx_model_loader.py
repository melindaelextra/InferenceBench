from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import AutoTokenizer


class ONNXModelLoader:
    """
    Loads ONNX Runtime model and tokenizer for embedding inference.
    """

    def __init__(self, model_dir: str = "models/onnx_model"):
        self.model_dir = model_dir
        self.model = None
        self.tokenizer = None
        self.model_name = "onnx-all-MiniLM-L6-v2"

    def load(self):
        if self.model is None or self.tokenizer is None:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
            self.model = ORTModelForFeatureExtraction.from_pretrained(self.model_dir)
        return self.model, self.tokenizer