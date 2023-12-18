import schemas

from unit_of_work import UnitOfWork


class CategoriesService:
    async def get_all_categories(self, uow: UnitOfWork) -> list[schemas.CategorySchema]:
        async with uow:
            categories = await uow.categories.get_all()
            return [category.to_schema() for category in categories]

    async def get_category(self, category_id: int, uow: UnitOfWork) -> schemas.CategorySchema:
        async with uow:
            category = await uow.categories.get(category_id)
            return category.to_schema()


class QuestionsService:
    async def get_questions_by_category_id(
        self,
        category_id: int,
        uow: UnitOfWork,
    ) -> list[schemas.QuestionByCategorySchema]:
        async with uow:
            category = await uow.categories.get(category_id)
            questions = await uow.questions.get_all_by_category_id(category.id)
            return [schemas.QuestionByCategorySchema(id=question.id, body=question.body) for question in questions]

    async def get(self, id: int, uow: UnitOfWork) -> schemas.QuestionSchema:
        async with uow:
            question = await uow.questions.get(id)
            return question.to_schema()

    async def get_random_question_by_category_id(self, category_id: int, uow: UnitOfWork) -> schemas.QuestionSchema:
        async with uow:
            category = await uow.categories.get(category_id)
            question = await uow.questions.get_random_by_category_id(category.id)
            return question.to_schema()
