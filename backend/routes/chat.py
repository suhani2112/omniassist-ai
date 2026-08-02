from fastapi import APIRouter
from backend.schemas.chat_schema import ChatRequest, ChatResponse
from backend.services.query_service import QueryService


router = APIRouter()

query_service = QueryService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = query_service.process_query(
        request.message
    )

    return result