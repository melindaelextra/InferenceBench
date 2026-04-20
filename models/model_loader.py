from sentence_transformers import SentenceTransformer


class ModelLoader:
    """
    Loads and stores the embedding model so it can be reused
    instead of being reloaded on every request.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = None

    def load(self):
        if self.model is None:
            self.model = SentenceTransformer(self.model_name)
        return self.model