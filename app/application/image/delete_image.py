from app.domain.image.image_repository import ImageRepository

class DeleteImage:

    def __init__(self, repo: ImageRepository):
        self.repo = repo

    def execute(self, image_id: int, user_id: int):
        image = self.repo.find_by_id(image_id)
        if not image:
            raise ValueError("Image not found")

        if image.owner_id != user_id:
            raise PermissionError("Not allowed")

        self.repo.delete(image)
