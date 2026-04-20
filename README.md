# InferenceBench

InferenceBench is a FastAPI-based text embedding inference service designed to explore and optimize ML inference performance on a single machine.

## Goal
Build a production-style inference API and improve its latency and throughput through systematic optimization.

## Initial Features
- text embedding endpoint
- health check endpoint
- local CPU-based serving
- benchmark-ready code structure

## Planned Optimizations
- batching
- caching
- ONNX Runtime
- quantization
- server tuning
- observability

## Tech Stack
- Python
- FastAPI
- Sentence Transformers
- PyTorch

## Status
Week 1: project setup and architecture

## Current Status
- FastAPI inference API working
- SentenceTransformer model integrated
- /embed endpoint returns embeddings with latency

## Example Response
```json
{
  "dimension": 384,
  "model_name": "sentence-transformers/all-MiniLM-L6-v2",
  "inference_time_ms": 145.239
}

## Performance Highlights

- Reduced cold-start latency from ~4s to ~42ms
- Improved throughput from 6.4 → 64.1 req/s (10x increase)
- Reduced P95 latency from ~14s → ~181ms under concurrency