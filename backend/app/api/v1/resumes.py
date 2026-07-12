from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.resume import ResumeResponse
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


@router.post(
    "/upload",
    response_model=ResumeResponse,
)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed.",
        )

    service = ResumeService(db)

    return service.upload_resume(
        current_user=current_user,
        file=file,
    )


@router.get(
    "",
    response_model=list[ResumeResponse],
)
def get_my_resumes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ResumeService(db)

    return service.get_user_resumes(current_user)