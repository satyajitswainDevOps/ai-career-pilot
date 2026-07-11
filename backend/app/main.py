from fastapi import FastAPI

app = FastAPI(
    title="AI Career Copilot",
    version="1.0.0",
    description="AI-powered Career Copilot API"
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