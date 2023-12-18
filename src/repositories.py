from abc import ABC, abstractmethod

from models import Category, Question

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


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
    async def get_all_by_category_id(self, category_id: int) -> list[Question]:
        pass

    @abstractmethod
    async def get(self, id: int) -> Question:
        pass

    @abstractmethod
    async def get_random_by_category_id(self, category_id: int) -> Question:
        pass


class SQLAlchemyQuestionsRepository(QuestionsRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_all_by_category_id(self, category_id: int) -> list[Question]:
        result = await self._session.execute(select(Question).where(Question.category_id == category_id))
        return list(result.scalars().all())

    async def get(self, id: int) -> Question:
        result = await self._session.execute(
            select(Question)
            .where(Question.id == id)
            .options(
                joinedload(Question.answers),
            ),
        )
        question = result.unique().scalars().one_or_none()
        if question is None:
            raise ValueError(f'Question with id {id} not found')
        return question

    async def get_random_by_category_id(self, category_id: int) -> Question:
        result = await self._session.execute(
            select(Question)
            .where(Question.category_id == category_id)
            .order_by(func.random())
            .limit(1)
            .options(
                joinedload(Question.answers),
            ),
        )
        question = result.unique().scalars().one_or_none()
        if question is None:
            raise ValueError(f'Question with category id {category_id} not found')
        return question
