from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.service_container import query_service


router = APIRouter()


class ChatRequest(BaseModel):

    message: str



@router.post("/chat")
def chat(request: ChatRequest):

    response = query_service.process_query(
        request.message
    )

    return response