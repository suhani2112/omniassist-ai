# from fastapi import FastAPI

# from backend.api.router import api_router

# app = FastAPI(
#     title="OmniAssist AI",
#     description="Multi-Agent Enterprise Intelligence Platform",
#     version="1.0.0",
# )

# app.include_router(api_router)


# @app.get("/")
# async def root():
#     return {
#         "message": "Welcome to OmniAssist AI 🚀"
#     }

from fastapi import FastAPI

from backend.api.router import router

app = FastAPI(
    title="OmniAssist AI",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "OmniAssist AI API is running 🚀"
    }