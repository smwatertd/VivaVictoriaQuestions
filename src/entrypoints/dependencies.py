from core.container import container

from services import CategoriesService, QuestionsService

from unit_of_work import UnitOfWork


def get_unit_of_work() -> UnitOfWork:
    return container.unit_of_work()


def get_categories_service() -> CategoriesService:
    return CategoriesService()


def get_questions_service() -> QuestionsService:
    return QuestionsService()
