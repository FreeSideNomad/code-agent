from typing import Any

from fastapi import FastAPI

app = FastAPI(title="Code Agent API", version="0.1.0")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Code Agent API is running"}


@app.get("/health")
async def health() -> dict[str, Any]:
    return {"status": "ok", "database": "unknown"}  # TODO: Check DB connection
