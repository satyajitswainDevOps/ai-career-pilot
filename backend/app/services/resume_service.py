from pathlib import Path
import shutil

from fastapi import UploadFile

from app.models.resume import Resume
from app.models.user import User
from app.repositories.resume_repository import ResumeRepository


class ResumeService:

    def __init__(self, db):
        self.repository = ResumeRepository(db)

    def upload_resume(
        self,
        current_user: User,
        file: UploadFile,
    ):
        uploads_dir = Path("uploads") / str(current_user.id)
        uploads_dir.mkdir(parents=True, exist_ok=True)

        file_path = uploads_dir / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        resume = Resume(
            user_id=current_user.id,
            file_name=file.filename,
            file_path=str(file_path),
            file_type=file.content_type,
            extracted_text="",
        )

        return self.repository.create(resume)

    def get_user_resumes(self, user: User):
        return self.repository.get_by_user(user.id)