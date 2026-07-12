from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    file_name: Mapped[str] = mapped_column(
        String(255)
    )

    file_path: Mapped[str] = mapped_column(
        String(500)
    )

    # Increased from 50 to 255 to support long MIME types
    file_type: Mapped[str] = mapped_column(
        String(255)
    )

    extracted_text: Mapped[str] = mapped_column(
        Text()
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    user = relationship(
        "User",
        back_populates="resumes",
    )