from schemas import CategorySchema

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    def __repr__(self) -> str:
        return f'Category(id={self.id}, name={self.name})'

    def to_schema(self) -> CategorySchema:
        return CategorySchema(id=self.id, name=self.name)


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))


class Answer(Base):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str]
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'))
