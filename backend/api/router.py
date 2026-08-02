# from fastapi import APIRouter

# from backend.api.endpoints.health import router as health_router

# api_router = APIRouter()

# api_router.include_router(
#     health_router,
#     prefix="",
#     tags=["Health"]
# )

from fastapi import APIRouter

from backend.api.endpoints import upload

router = APIRouter()

router.include_router(
    upload.router,
    tags=["Documents"],
)