from abc import ABC, abstractmethod
from .user_entity import User

class UserRepository(ABC):

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass
