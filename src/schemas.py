from typing import Literal

from pydantic import BaseModel


class HealthSchema(BaseModel):
    status: Literal['ok']


class CategorySchema(BaseModel):
    id: int
    name: str


class AnswerSchema(BaseModel):
    id: int
    body: str
    is_correct: bool
