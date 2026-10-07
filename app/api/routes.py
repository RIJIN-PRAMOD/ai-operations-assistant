from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.assistant import find_solution


router = APIRouter()


class Question(BaseModel):
    question: str = Field(min_length=3)


@router.get("/")
def home():

    return {
        "message": "AI Operations Assistant is running"
    }


@router.post("/ask")
def ask_question(data: Question):

    answer = find_solution(data.question)

    return answer