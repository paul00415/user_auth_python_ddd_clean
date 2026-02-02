from app.domain.image.image_repository import ImageRepository
from app.domain.image.image_entity import Image
from app.infrastructure.image.image_model import ImageModel
from app.infrastructure.database import SessionLocal

class ImageRepositoryImpl(ImageRepository):

    def save(self, image: Image):
        db = SessionLocal()
        model = ImageModel(
            owner_id=image.owner_id,
            filename=image.filename,
            title=image.title
        )
        db.add(model)
        db.commit()
        db.refresh(model)
        db.close()

        return Image(
            id=model.id,
            owner_id=model.owner_id,
            filename=model.filename,
            title=model.title,
            created_at=model.created_at
        )

    def find_by_owner(self, owner_id: int):
        db = SessionLocal()
        models = db.query(ImageModel).filter_by(owner_id=owner_id).all()
        db.close()

        return [
            Image(
                id=m.id,
                owner_id=m.owner_id,
                filename=m.filename,
                title=m.title,
                created_at=m.created_at
            )
            for m in models
        ]

    def find_by_id(self, image_id: int):
        db = SessionLocal()
        model = db.query(ImageModel).filter_by(id=image_id).first()
        db.close()

        if not model:
            return None

        return Image(
            id=model.id,
            owner_id=model.owner_id,
            filename=model.filename,
            title=model.title,
            created_at=model.created_at
        )

    def delete(self, image: Image):
        db = SessionLocal()
        db.query(ImageModel).filter_by(id=image.id).delete()
        db.commit()
        db.close()
