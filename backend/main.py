from fastapi import FastAPI

from backend.api.chat import router
from backend.core.memory import init_memory


app = FastAPI(
    title="OmniAssistAI API",
    version="1.0"
)


@app.on_event("startup")
def startup_event():
    init_memory()


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "OmniAssistAI API running"
    }