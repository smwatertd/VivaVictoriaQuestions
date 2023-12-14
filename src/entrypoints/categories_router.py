from entrypoints.schemas import CategorySchema

from fastapi import APIRouter

import services


router = APIRouter(
    tags=['Categories'],
)


@router.get('/categories', status_code=200, response_model=list[CategorySchema])
async def get_categories() -> list[CategorySchema]:
    categories = await services.get_all_categories()
    return [CategorySchema(id=category.id, name=category.name) for category in categories]


@router.get('/categories/{category_id}', status_code=200, response_model=CategorySchema)
async def get_category(category_id: int) -> CategorySchema:
    category = await services.get_category(category_id)
    return CategorySchema(id=category.id, name=category.name)
