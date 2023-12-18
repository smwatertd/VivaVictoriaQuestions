from abc import ABC, abstractmethod

from models import Category, Question

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CategoriesRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Category]:
        pass

    @abstractmethod
    async def get(self, id: int) -> Category:
        pass


class SQLAlchemyCategoriesRepository(CategoriesRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_all(self) -> list[Category]:
        result = await self._session.execute(select(Category))
        return list(result.scalars().all())

    async def get(self, id: int) -> Category:
        result = await self._session.execute(select(Category).where(Category.id == id))
        category = result.scalars().one_or_none()
        if category is None:
            raise ValueError(f'Category with id {id} not found')
        return category


class QuestionsRepository(ABC):
    @abstractmethod
    async def all_by_category_id(self, category_id: int) -> list[Question]:
        pass
