from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, Token
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

    def login_user(self, login_data: LoginRequest) -> Token:

        user = self.user_repository.get_by_email(login_data.email)

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            login_data.password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password")

        access_token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
        )