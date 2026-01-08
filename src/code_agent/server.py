from fastapi import FastAPI

app = FastAPI(title="Code Agent API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Code Agent API is running"}

@app.get("/health")
async def health():
    return {"status": "ok", "database": "unknown"} # TODO: Check DB connection
