from app.domain.user.user_repository import UserRepository
from app.infrastructure.security import verify_password, create_access_token

class LoginUser:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, email: str, password: str):
        user = self.repo.find_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")

        return create_access_token({"sub": user.email})
