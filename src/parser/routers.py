from fastapi import APIRouter, Depends, requests
from sqlalchemy import insert
from sqlalchemy.orm import Session
import requests


from src.database import get_session
from src.parser.models import Question
from src.parser.schemas import QuestionAdd, QuestionSchema

router = APIRouter(
    prefix="/parser",
    tags=["Parser"],
)


@router.post("/")
def add_question(question_add: QuestionAdd, session: Session = Depends(get_session)):
    response = requests.get(f"https://jservice.io/api/random?count={question_add.model_dump()['questions_num']}")
    data = response.json()
    for question_data in data:
        question_schema = QuestionSchema(**question_data)
        question_id = question_schema.id
        if not session.query(Question).filter(Question.id == question_id).scalar():
            stmt = insert(Question).values(**question_schema.model_dump())
            session.execute(stmt)
    session.commit()
    return {'status': 'ok'}
