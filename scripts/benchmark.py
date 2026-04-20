import requests
import time
import statistics

URL = "http://127.0.0.1:8000/embed"
NUM_REQUESTS = 50

payload = {
    "text": "Machine learning inference systems need to be efficient."
}

latencies = []

for i in range(NUM_REQUESTS):
    start = time.perf_counter()
    response = requests.post(URL, json=payload)
    end = time.perf_counter()

    response.raise_for_status()

    latency_ms = (end - start) * 1000
    latencies.append(latency_ms)
    print(f"Request {i + 1}: {latency_ms:.2f} ms")

latencies_sorted = sorted(latencies)
p50 = statistics.median(latencies_sorted)
p95 = latencies_sorted[int(0.95 * len(latencies_sorted)) - 1]
avg = statistics.mean(latencies_sorted)

print("\n=== Baseline Results ===")
print(f"Requests: {NUM_REQUESTS}")
print(f"Average latency: {avg:.2f} ms")
print(f"P50 latency: {p50:.2f} ms")
print(f"P95 latency: {p95:.2f} ms")
print(f"Min latency: {min(latencies_sorted):.2f} ms")
print(f"Max latency: {max(latencies_sorted):.2f} ms")