import schemas

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    def __repr__(self) -> str:
        return f'Category(id={self.id}, name={self.name})'

    def to_schema(self) -> schemas.CategorySchema:
        return schemas.CategorySchema(id=self.id, name=self.name)


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(unique=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    answers: Mapped[list['Answer']] = relationship('Answer', back_populates='question')

    def _repr__(self) -> str:
        return f'Question(id={self.id}, body={self.body})'

    def to_schema(self) -> schemas.QuestionSchema:
        return schemas.QuestionSchema(
            id=self.id,
            body=self.body,
            answers=[answer.to_schema() for answer in self.answers],
        )


class Answer(Base):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str]
    is_correct: Mapped[bool] = mapped_column(default=False)
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'))

    question: Mapped['Question'] = relationship('Question', back_populates='answers')

    def __repr__(self) -> str:
        return f'Answer(id={self.id}, body={self.body}, is_correct={self.is_correct})'

    def to_schema(self) -> schemas.AnswerSchema:
        return schemas.AnswerSchema(id=self.id, body=self.body, is_correct=self.is_correct)
