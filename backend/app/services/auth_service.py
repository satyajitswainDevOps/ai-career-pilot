from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class AuthService:

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register_user(self, user: UserCreate):

        existing_user = self.user_repository.get_by_email(user.email)

        if existing_user:
            raise ValueError("Email already registered")

        db_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            hashed_password=hash_password(user.password),
        )

        return self.user_repository.create(db_user)