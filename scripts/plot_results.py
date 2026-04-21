import matplotlib.pyplot as plt

# ---------- Chart 1: Warm-up optimization ----------
labels = ["Before warm-up", "After warm-up"]
avg_latency = [104.08, 17.41]
p50_latency = [19.59, 16.29]
p95_latency = [39.55, 19.27]
max_latency = [4089.15, 42.42]

plt.figure(figsize=(8, 5))
plt.plot(labels, avg_latency, marker="o", label="Average")
plt.plot(labels, p50_latency, marker="o", label="P50")
plt.plot(labels, p95_latency, marker="o", label="P95")
plt.plot(labels, max_latency, marker="o", label="Max")
plt.ylabel("Latency (ms)")
plt.title("Latency Before vs After Warm-up")
plt.legend()
plt.tight_layout()
plt.savefig("docs/warmup_comparison.png")
plt.close()

# ---------- Chart 2: Multi-worker throughput ----------
labels = ["Single worker", "4 workers"]
throughput = [6.42, 64.11]
p95 = [14117.70, 181.55]

plt.figure(figsize=(8, 5))
plt.bar(labels, throughput)
plt.ylabel("Requests per second")
plt.title("Throughput Before vs After Multi-worker Scaling")
plt.tight_layout()
plt.savefig("docs/throughput_comparison.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(labels, p95)
plt.ylabel("P95 latency (ms)")
plt.title("P95 Latency Before vs After Multi-worker Scaling")
plt.tight_layout()
plt.savefig("docs/multiworker_p95.png")
plt.close()

# ---------- Chart 3: PyTorch vs ONNX ----------
labels = ["PyTorch", "ONNX"]
p50_vals = [4.87, 8.43]
p95_vals = [9.89, 22.22]

x = range(len(labels))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - width / 2 for i in x], p50_vals, width=width, label="P50")
plt.bar([i + width / 2 for i in x], p95_vals, width=width, label="P95")
plt.xticks(list(x), labels)
plt.ylabel("Latency (ms)")
plt.title("PyTorch vs ONNX Latency Comparison")
plt.legend()
plt.tight_layout()
plt.savefig("docs/onnx_vs_pytorch.png")
plt.close()

# ---------- Chart 4: Cache benchmark ----------
labels = ["Cold request", "Cached requests"]
latencies = [16352.68, 4.67]

plt.figure(figsize=(8, 5))
plt.bar(labels, latencies)
plt.ylabel("Latency (ms)")
plt.title("Cold vs Cached Request Latency")
plt.tight_layout()
plt.savefig("docs/cache_comparison.png")
plt.close()

print("Charts saved to docs/")