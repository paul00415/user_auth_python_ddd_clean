from abc import ABC, abstractmethod
from .image_entity import Image

class ImageRepository(ABC):

    @abstractmethod
    def save(self, image: Image) -> Image:
        pass

    @abstractmethod
    def find_by_owner(self, owner_id: int) -> list[Image]:
        pass

    @abstractmethod
    def find_by_id(self, image_id: int) -> Image | None:
        pass

    @abstractmethod
    def delete(self, image: Image) -> None:
        pass
