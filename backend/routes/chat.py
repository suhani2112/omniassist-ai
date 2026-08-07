from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.service_container import query_service

router = APIRouter()


class ChatRequest(BaseModel):
    user_id: str
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    response = query_service.process_query(
        user_id=request.user_id,
        question=request.question
    )

    return response