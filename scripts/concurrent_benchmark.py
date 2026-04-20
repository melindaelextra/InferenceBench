import time
import statistics
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "http://127.0.0.1:8000/embed"
TOTAL_REQUESTS = 100
CONCURRENCY = 10

payload = {
    "text": "Machine learning inference systems need to be efficient."
}


def send_request(request_id: int):
    start = time.perf_counter()
    response = requests.post(URL, json=payload)
    end = time.perf_counter()

    response.raise_for_status()

    latency_ms = (end - start) * 1000
    return {
        "request_id": request_id,
        "latency_ms": latency_ms,
        "status_code": response.status_code,
    }


def percentile(sorted_values, p):
    if not sorted_values:
        return None
    index = int(p * len(sorted_values)) - 1
    index = max(0, min(index, len(sorted_values) - 1))
    return sorted_values[index]


def main():
    latencies = []
    start_total = time.perf_counter()

    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(send_request, i + 1) for i in range(TOTAL_REQUESTS)]

        for future in as_completed(futures):
            result = future.result()
            latencies.append(result["latency_ms"])
            print(
                f"Request {result['request_id']}: "
                f"{result['latency_ms']:.2f} ms "
                f"(status {result['status_code']})"
            )

    end_total = time.perf_counter()

    latencies_sorted = sorted(latencies)
    total_time_s = end_total - start_total
    throughput = TOTAL_REQUESTS / total_time_s

    print("\n=== Concurrent Benchmark Results ===")
    print(f"Total requests: {TOTAL_REQUESTS}")
    print(f"Concurrency: {CONCURRENCY}")
    print(f"Total wall time: {total_time_s:.2f} s")
    print(f"Throughput: {throughput:.2f} req/s")
    print(f"Average latency: {statistics.mean(latencies_sorted):.2f} ms")
    print(f"P50 latency: {statistics.median(latencies_sorted):.2f} ms")
    print(f"P95 latency: {percentile(latencies_sorted, 0.95):.2f} ms")
    print(f"Min latency: {min(latencies_sorted):.2f} ms")
    print(f"Max latency: {max(latencies_sorted):.2f} ms")


if __name__ == "__main__":
    main()