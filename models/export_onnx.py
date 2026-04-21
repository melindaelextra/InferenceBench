from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import AutoTokenizer

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
SAVE_DIR = "models/onnx_model"


def main():
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    print("Exporting model to ONNX...")
    model = ORTModelForFeatureExtraction.from_pretrained(
        MODEL_ID,
        export=True
    )

    print("Saving tokenizer and ONNX model...")
    tokenizer.save_pretrained(SAVE_DIR)
    model.save_pretrained(SAVE_DIR)

    print(f"ONNX model exported to: {SAVE_DIR}")


if __name__ == "__main__":
    main()