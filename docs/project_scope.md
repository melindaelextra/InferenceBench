# Project Scope

## Project Title
InferenceBench: ML Inference Optimization System

## Objective
Build a FastAPI-based text embedding inference service and optimize its performance for low latency and high throughput on a single machine.

## Core Use Case
A client sends text to the API, and the system returns:
- embedding vector
- embedding dimension
- model name
- inference time

## Initial Version (V1)
The first version will include:
- one embedding model
- one FastAPI service
- one `/embed` endpoint
- one `/health` endpoint
- CPU-first local deployment
- baseline benchmarking support

## Primary Metrics
The system will be evaluated using:
- p50 latency
- p95 latency
- throughput (requests per second)
- memory usage

## Planned Optimizations
Planned improvements include:
- batching
- caching
- worker/server tuning
- ONNX Runtime
- quantization
- observability and monitoring

## Out of Scope
The following are not included in V1:
- training a custom model
- distributed inference
- Kubernetes
- GPU scheduling
- multiple model routing
- frontend dashboard
- authentication
- autoscaling

## Success Criteria
The project is considered successful if:
1. The API serves embeddings correctly.
2. The model is loaded once and reused efficiently.
3. Baseline inference performance is measured.
4. Later optimizations show measurable improvements.
5. The repository clearly demonstrates production-style ML systems engineering.