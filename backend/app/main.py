from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as user_router
from app.api.v1.resumes import router as resume_router

app = FastAPI(
    title="AI Career Copilot",
    version="1.0.0",
)

# Authentication APIs
app.include_router(auth_router)

# User APIs
app.include_router(user_router)

# Resume APIs
app.include_router(resume_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Career Copilot 🚀"
    }