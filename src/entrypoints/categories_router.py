from typing import Annotated

from entrypoints import dependencies

from fastapi import APIRouter, Depends

from schemas import CategorySchema

from services import CategoriesService

from unit_of_work import UnitOfWork


router = APIRouter(
    tags=['Categories'],
)


@router.get('/categories', status_code=200, response_model=list[CategorySchema])
async def get_categories(
    categories_service: Annotated[CategoriesService, Depends(dependencies.get_categories_service)],
    uow: Annotated[UnitOfWork, Depends(dependencies.get_unit_of_work)],
) -> list[CategorySchema]:
    return await categories_service.get_all_categories(uow)


@router.get('/categories/{category_id}', status_code=200, response_model=CategorySchema)
async def get_category(
    category_id: int,
    categories_service: Annotated[CategoriesService, Depends(dependencies.get_categories_service)],
    uow: Annotated[UnitOfWork, Depends(dependencies.get_unit_of_work)],
) -> CategorySchema:
    return await categories_service.get_category(category_id, uow)
