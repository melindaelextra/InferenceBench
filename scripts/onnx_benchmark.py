import requests
import time
import statistics

PYTORCH_URL = "http://127.0.0.1:8000/embed"
ONNX_URL = "http://127.0.0.1:8000/embed_onnx"
NUM_REQUESTS = 30

payload = {
    "text": "ONNX Runtime can improve CPU inference performance."
}


def benchmark(url, label):
    latencies = []

    for i in range(NUM_REQUESTS):
        start = time.perf_counter()
        response = requests.post(url, json=payload, timeout=30)
        end = time.perf_counter()

        response.raise_for_status()

        latency_ms = (end - start) * 1000
        latencies.append(latency_ms)
        print(f"{label} request {i+1}: {latency_ms:.2f} ms")

    latencies_sorted = sorted(latencies)

    print(f"\n=== {label} Results ===")
    print(f"Average latency: {statistics.mean(latencies_sorted):.2f} ms")
    print(f"P50 latency: {statistics.median(latencies_sorted):.2f} ms")
    print(f"P95 latency: {latencies_sorted[int(0.95 * len(latencies_sorted)) - 1]:.2f} ms")
    print(f"Min latency: {min(latencies_sorted):.2f} ms")
    print(f"Max latency: {max(latencies_sorted):.2f} ms")


benchmark(PYTORCH_URL, "PyTorch")
benchmark(ONNX_URL, "ONNX")