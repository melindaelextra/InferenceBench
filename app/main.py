from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="InferenceBench API",
    version="0.1.0",
    description="A text embedding inference API for benchmarking and optimization."
)

app.include_router(router)