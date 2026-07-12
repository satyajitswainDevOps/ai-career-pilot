from datetime import datetime

from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    user_id: int
    file_name: str
    file_path: str
    file_type: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }