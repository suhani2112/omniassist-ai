from fastapi import APIRouter
from pydantic import BaseModel

from backend.core.rag_pipeline import ask_omniassist


router = APIRouter()



# ---------------------------------
# Request Model
# ---------------------------------

class ChatRequest(BaseModel):

    user_id: str

    question: str

    active_pdf: str | None = None



# ---------------------------------
# Response Model
# ---------------------------------

class ChatResponse(BaseModel):

    answer: str



# ---------------------------------
# Chat Endpoint
# ---------------------------------

@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):


    answer = ask_omniassist(

        request.question,

        user_id=request.user_id,

        active_pdf=request.active_pdf

    )


    return {

        "answer": answer

    }