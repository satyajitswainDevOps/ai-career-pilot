from pathlib import Path
import shutil

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.models.user import User
from app.repositories.resume_repository import ResumeRepository
from app.services.resume_parser import ResumeParser


class ResumeService:

    def __init__(self, db: Session):
        self.repository = ResumeRepository(db)

    def upload_resume(
        self,
        current_user: User,
        file: UploadFile,
    ):
        uploads_dir = Path("uploads") / str(current_user.id)
        uploads_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = uploads_dir / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = ResumeParser.extract_text(
            str(file_path)
        )

        resume = Resume(
            user_id=current_user.id,
            file_name=file.filename,
            file_path=str(file_path),
            file_type=file.content_type,
            extracted_text=extracted_text,
        )

        return self.repository.create(resume)

    def get_user_resumes(
        self,
        current_user: User,
    ):
        return self.repository.get_by_user(
            current_user.id
        )

    def get_resume_text(
        self,
        resume_id: int,
        current_user: User,
    ):
        resume = self.repository.get_by_id_and_user(
            resume_id,
            current_user.id,
        )

        if resume is None:
            raise ValueError("Resume not found")

        return {
            "resume_id": resume.id,
            "file_name": resume.file_name,
            "extracted_text": resume.extracted_text,
        }