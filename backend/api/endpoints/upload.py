from fastapi import APIRouter, File, UploadFile, HTTPException

from backend.schemas.response import UploadResponse
from backend.services.document_service import DocumentService

router = APIRouter()

service = DocumentService()


@router.post(
    "/upload",
    response_model=UploadResponse,
    summary="Upload and index a document",
)
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a PDF, process it, and store embeddings in ChromaDB.
    """

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    try:
        result = service.upload_document(file)
        return UploadResponse(**result)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )