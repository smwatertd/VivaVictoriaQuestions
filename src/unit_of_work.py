from abc import ABC, abstractmethod
from typing import Any

from core.settings import db_settings

import repositories

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


DEFAULT_SESSION_MAKER = async_sessionmaker(
    bind=create_async_engine(db_settings.url),
    class_=AsyncSession,
    expire_on_commit=False,
)


class UnitOfWork(ABC):
    categories: repositories.CategoriesRepository
    questions: repositories.QuestionsRepository

    async def __aenter__(self) -> 'UnitOfWork':
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        await self.rollback()

    @abstractmethod
    async def rollback(self) -> None:
        pass

    @abstractmethod
    async def commit(self) -> None:
        pass


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession] = DEFAULT_SESSION_MAKER) -> None:
        self._session_factory = session_factory

    async def __aenter__(self) -> UnitOfWork:
        self._session = self._session_factory()
        self.categories = repositories.SQLAlchemyCategoriesRepository(self._session)
        self.questions = repositories.SQLAlchemyQuestionsRepository(self._session)
        return await super().__aenter__()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def commit(self) -> None:
        await self._session.commit()
