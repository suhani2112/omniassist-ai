from pydantic import BaseModel


class UploadResponse(BaseModel):
    """
    Response returned after a successful document upload.
    """

    filename: str
    pages: int
    chunks: int
    status: str