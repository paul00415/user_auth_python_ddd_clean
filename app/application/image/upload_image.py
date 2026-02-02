from app.domain.image.image_repository import ImageRepository
from app.domain.image.image_entity import Image
from datetime import datetime

class UploadImage:

    def __init__(self, repo: ImageRepository):
        self.repo = repo

    def execute(self, owner_id: int, filename: str, title: str | None):
        image = Image(
            id=None,
            owner_id=owner_id,
            filename=filename,
            title=title,
            created_at=datetime.utcnow()
        )
        return self.repo.save(image)
