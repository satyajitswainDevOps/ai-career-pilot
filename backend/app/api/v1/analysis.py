from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.analysis import ResumeAnalysisResponse
from app.services.analysis_service import AnalysisService

router = APIRouter(
    prefix="/analysis",
    tags=["AI Resume Analysis"],
)


@router.post(
    "/resumes/{resume_id}",
    response_model=ResumeAnalysisResponse,
)
def analyze_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = AnalysisService(db)

    try:
        return service.analyze_resume(
            resume_id,
            current_user,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )