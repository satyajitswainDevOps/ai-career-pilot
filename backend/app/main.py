from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="AI-powered Career Copilot API",
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Career Copilot 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }