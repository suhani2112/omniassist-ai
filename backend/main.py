from fastapi import FastAPI
from backend.routes.chat import router
from backend.routes.logs import router as logs_router

app = FastAPI(
    title="OmniAssistAI"
)


app.include_router(router)
app.include_router(logs_router)

@app.get("/")
def home():
    return {
        "message": "OmniAssistAI Backend Running"
    }