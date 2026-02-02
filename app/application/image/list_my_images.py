from app.domain.image.image_repository import ImageRepository

class ListMyImages:

    def __init__(self, repo: ImageRepository):
        self.repo = repo

    def execute(self, owner_id: int):
        return self.repo.find_by_owner(owner_id)
