from typing import Annotated

from entrypoints import dependencies

from fastapi import APIRouter, Depends, Query

from schemas import QuestionByCategorySchema

import services

from unit_of_work import UnitOfWork


router = APIRouter(
    tags=['Questions'],
)


@router.get('/questions', status_code=200)
async def get_questions_by_category(
    category_id: Annotated[int, Query(description='Category ID')],
    questions_service: Annotated[services.QuestionsService, Depends(dependencies.get_questions_service)],
    uow: Annotated[UnitOfWork, Depends(dependencies.get_unit_of_work)],
) -> list[QuestionByCategorySchema]:
    return await questions_service.get_questions_by_category_id(category_id, uow)
