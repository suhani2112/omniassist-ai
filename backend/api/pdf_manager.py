from pathlib import Path

from fastapi import APIRouter, HTTPException

from backend.tools.pdf.vector_store import retriever


router = APIRouter()


UPLOAD_FOLDER = Path(
    "backend/storage/uploads"
)



# -------------------------------------------------
# Get PDF List
# -------------------------------------------------

@router.get("/pdfs")
def get_pdfs():


    pdfs = retriever.list_pdfs()


    return {

        "pdfs": pdfs

    }



# -------------------------------------------------
# Set Active PDF
# -------------------------------------------------

@router.post("/set-active-pdf/{filename}")
def set_active_pdf(
    filename: str
):


    pdfs = retriever.list_pdfs()


    if filename not in pdfs:

        raise HTTPException(

            status_code=404,

            detail="PDF not found"

        )


    return {

        "message":
        f"{filename} selected.",

        "active_pdf":
        filename

    }



# -------------------------------------------------
# Delete PDF
# -------------------------------------------------

@router.delete("/pdf/{filename}")
def delete_pdf(
    filename: str
):


    retriever.delete_pdf(
        filename
    )


    file_path = (
        UPLOAD_FOLDER / filename
    )


    if file_path.exists():

        file_path.unlink()



    return {

        "message":
        f"{filename} deleted."

    }