from fastapi import APIRouter
from pydantic import BaseModel

from backend.core.rag_pipeline import ask_omniassist


router = APIRouter()



class ChatRequest(BaseModel):

    user_id: str

    question: str



class ChatResponse(BaseModel):

    answer: str




@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):


    answer = ask_omniassist(

        request.question,

        user_id=request.user_id

    )


    return {

        "answer": answer

    }