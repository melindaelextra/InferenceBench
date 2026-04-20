# InferenceBench Performance Analysis

This document presents performance benchmarking and optimization of the inference API.

The goal is to:
- measure baseline performance
- identify bottlenecks
- apply optimizations
- evaluate improvements

## System Setup

- Model: sentence-transformers/all-MiniLM-L6-v2
- Hardware: Local CPU
- Framework: FastAPI + Uvicorn
- Endpoint: /embed
- Test Type: Sequential + Concurrent

## Sequential Benchmark (Initial)

Requests: 50  
Average latency: 104.08 ms  
P50 latency: 19.59 ms  
P95 latency: 39.55 ms  
Min latency: 16.81 ms  
Max latency: 4089.15 ms  

### Analysis

- Median latency (~20 ms) indicates fast steady-state inference.
- A large outlier (~4 seconds) was observed.
- The average latency is skewed by this outlier.
- This suggests a cold-start problem during early requests.

## Warm-up Optimization

### Change
Added a startup warm-up request to preload the model.

### Results

Requests: 50  
Average latency: 17.41 ms  
P50 latency: 16.29 ms  
P95 latency: 19.27 ms  
Min latency: 13.80 ms  
Max latency: 42.42 ms  

### Analysis

- Cold-start latency was eliminated.
- Average latency dropped significantly.
- Max latency reduced from ~4 seconds to ~42 ms.
- Performance became stable across all requests.

### Conclusion

Warm-up is an effective optimization to eliminate cold-start overhead.

## Concurrent Benchmark (Single Worker)

Requests: 100  
Concurrency: 10  
Throughput: 6.42 req/s  
Average latency: 1553.52 ms  
P50 latency: 151.51 ms  
P95 latency: 14117.70 ms  
Min latency: 90.09 ms  
Max latency: 14142.38 ms  

### Analysis

- Latency increased drastically under concurrent load.
- P95 exceeded 14 seconds, indicating severe request queuing.
- Throughput was very low.
- The system is CPU-bound and cannot handle parallel requests efficiently with a single worker.

### Conclusion

Single-worker deployment leads to request bottlenecks and poor scalability.

## Multi-Worker Optimization

### Change
Deployed the server with 4 workers.

### Results

Requests: 100  
Concurrency: 10  
Throughput: 64.11 req/s  
Average latency: 152.15 ms  
P50 latency: 151.21 ms  
P95 latency: 181.55 ms  
Min latency: 75.10 ms  
Max latency: 232.52 ms  

### Analysis

- Throughput improved by ~10x.
- P95 latency dropped from ~14 seconds to ~181 ms.
- Maximum latency reduced significantly.
- Median latency remained similar, indicating stable per-request inference cost.
- The main improvement came from parallel request handling.

### Conclusion

The bottleneck was request scheduling rather than inference speed. Multi-worker deployment significantly improved scalability.

## Key Insights

1. Cold-start latency can significantly distort performance metrics.
2. Median latency is a better indicator than average latency.
3. Single-worker inference servers cannot handle concurrent workloads efficiently.
4. Multi-worker deployment improves throughput and reduces tail latency.
5. Inference systems require both model optimization and system-level optimization.

## Next Steps

- Implement batching to improve throughput further
- Add caching for repeated queries
- Optimize model format (ONNX / quantization)
- Evaluate performance under higher concurrency