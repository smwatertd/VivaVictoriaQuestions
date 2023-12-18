from abc import ABC, abstractmethod
from typing import Any

import repositories


class UnitOfWork(ABC):
    categories: repositories.CategoriesRepository

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
