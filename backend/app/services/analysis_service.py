from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.resume_repository import ResumeRepository
from app.services.resume_analyzer import ResumeAnalyzer


class AnalysisService:

    def __init__(self, db: Session):
        self.resume_repository = ResumeRepository(db)

    def analyze_resume(
        self,
        resume_id: int,
        current_user: User,
    ):
        resume = self.resume_repository.get_by_id_and_user(
            resume_id,
            current_user.id,
        )

        if resume is None:
            raise ValueError("Resume not found")

        return ResumeAnalyzer.analyze(
            resume.extracted_text
        )