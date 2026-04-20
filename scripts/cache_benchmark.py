import requests
import time
import statistics

URL = "http://127.0.0.1:8000/embed"
TEXT = "Caching can reduce repeated inference cost."
NUM_REQUESTS = 20

latencies = []
cache_hits = 0

for i in range(NUM_REQUESTS):
    start = time.perf_counter()
    response = requests.post(URL, json={"text": TEXT})
    end = time.perf_counter()

    response.raise_for_status()
    data = response.json()

    latency_ms = (end - start) * 1000
    latencies.append(latency_ms)

    if data.get("cache_hit"):
        cache_hits += 1

    print(
        f"Request {i+1}: {latency_ms:.2f} ms | "
        f"cache_hit={data.get('cache_hit')}"
    )

print("\n=== Cache Benchmark Results ===")
print(f"Requests: {NUM_REQUESTS}")
print(f"Cache hits: {cache_hits}")
print(f"Average latency: {statistics.mean(latencies):.2f} ms")
print(f"P50 latency: {statistics.median(latencies):.2f} ms")
print(f"Min latency: {min(latencies):.2f} ms")
print(f"Max latency: {max(latencies):.2f} ms")