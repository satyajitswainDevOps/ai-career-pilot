from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
    ats_score: int
    experience: str
    skills: list[str]
    missing_skills: list[str]
    recommendations: list[str]