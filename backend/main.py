from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.chat import router as chat_router
from backend.api.upload import router as upload_router
from backend.api.pdf_manager import router as pdf_router

from backend.core.memory import init_memory


app = FastAPI(
    title="OmniAssistAI API",
    version="2.0"
)


# -------------------------------------------------
# CORS
# -------------------------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ]

)



# -------------------------------------------------
# Startup
# -------------------------------------------------

@app.on_event("startup")
def startup():

    init_memory()

    print("=" * 60)
    print("OmniAssistAI Started")
    print("=" * 60)



# -------------------------------------------------
# Routes
# -------------------------------------------------

app.include_router(
    chat_router
)

app.include_router(
    upload_router
)

app.include_router(
    pdf_router
)



# -------------------------------------------------
# Home
# -------------------------------------------------

@app.get("/")
def home():

    return {

        "message":
        "OmniAssistAI API Running"

    }