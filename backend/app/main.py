from fastapi import FastAPI

app = FastAPI(
    title="Smart Document Reader",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "smart-document-reader",
    }