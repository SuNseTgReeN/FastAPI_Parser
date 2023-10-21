from datetime import datetime
from pydantic import BaseModel, Field


class QuestionSchema(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime


class QuestionAdd(BaseModel):
    questions_num: int = Field(ge=1)
