from app.domain.user.user_repository import UserRepository
from app.domain.user.user_entity import User
from app.infrastructure.security import hash_password
from datetime import datetime

class RegisterUser:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, email: str, name: str, password: str):
        if self.repo.find_by_email(email):
            raise ValueError("Email already exists")

        user = User(
            id=None,
            email=email,
            name=name,
            password_hash=hash_password(password),
            created_at=datetime.utcnow()
        )

        return self.repo.save(user)
