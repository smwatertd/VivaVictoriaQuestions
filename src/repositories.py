from abc import ABC, abstractmethod

from models import Category


class CategoriesRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Category]:
        pass

    @abstractmethod
    async def get(self, id: int) -> Category:
        pass
