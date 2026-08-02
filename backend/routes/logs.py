from fastapi import APIRouter

from backend.logs.logger_instance import logger


router = APIRouter()



@router.get("/logs")
def get_logs():

    return {
        "logs": logger.get_logs()
    }