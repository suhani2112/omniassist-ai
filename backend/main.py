from fastapi import FastAPI
from backend.routes.chat import router


app = FastAPI(
    title="OmniAssistAI"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "OmniAssistAI Backend Running"
    }