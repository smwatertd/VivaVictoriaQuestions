from typing import Type

from dependency_injector import containers, providers

import repositories

import services

from unit_of_work import SQLAlchemyUnitOfWork, UnitOfWork


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    categories_repository: Type[repositories.CategoriesRepository] = providers.Factory(
        repositories.SQLAlchemyCategoriesRepository,
    )  # type: ignore

    categories_service: Type[services.CategoriesService] = providers.Factory(
        services.CategoriesService,
    )  # type: ignore

    questions_repository: Type[repositories.QuestionsRepository] = providers.Factory(
        repositories.SQLAlchemyQuestionsRepository,
    )  # type: ignore

    questions_service: Type[services.QuestionsService] = providers.Factory(
        services.QuestionsService,
    )  # type: ignore

    unit_of_work: Type[UnitOfWork] = providers.Factory(
        SQLAlchemyUnitOfWork,
    )  # type: ignore


container = Container()
