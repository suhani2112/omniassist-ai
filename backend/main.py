from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.chat import router
from backend.core.memory import init_memory

app = FastAPI(
    title="OmniAssistAI API",
    version="1.0"
)

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Startup
# -----------------------------
@app.on_event("startup")
def startup_event():
    init_memory()

# -----------------------------
# Routes
# -----------------------------
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "OmniAssistAI API running"
    }