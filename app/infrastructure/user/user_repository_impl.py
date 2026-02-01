from app.domain.user.user_repository import UserRepository
from app.domain.user.user_entity import User
from app.infrastructure.user.user_model import UserModel
from app.infrastructure.database import SessionLocal

class UserRepositoryImpl(UserRepository):

    def find_by_email(self, email: str):
        db = SessionLocal()
        model = db.query(UserModel).filter_by(email=email).first()
        db.close()

        if not model:
            return None

        return User(
            id=model.id,
            email=model.email,
            name=model.name,
            password_hash=model.password_hash,
            created_at=model.created_at
        )

    def save(self, user: User):
        db = SessionLocal()
        model = UserModel(
            email=user.email,
            name=user.name,
            password_hash=user.password_hash
        )
        db.add(model)
        db.commit()
        db.refresh(model)
        db.close()

        return User(
            id=model.id,
            email=model.email,
            name=model.name,
            password_hash=model.password_hash,
            created_at=model.created_at
        )
