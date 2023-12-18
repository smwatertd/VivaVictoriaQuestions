from schemas import CategorySchema

from unit_of_work import UnitOfWork


class CategoriesService:
    async def get_all_categories(self, uow: UnitOfWork) -> list[CategorySchema]:
        categories = await uow.categories.get_all()
        return [category.to_schema() for category in categories]

    async def get_category(self, category_id: int, uow: UnitOfWork) -> CategorySchema:
        category = await uow.categories.get(category_id)
        return category.to_schema()
