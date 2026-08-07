from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.tools.pdf.pdf_processor import pdf_processor
from backend.tools.pdf.vector_store import retriever


router = APIRouter()


UPLOAD_FOLDER = Path(
    "backend/storage/uploads"
)

UPLOAD_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)



# -------------------------------------------------
# Upload PDF
# -------------------------------------------------

@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):


    # -----------------------------
    # Validate
    # -----------------------------

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )



    file_path = UPLOAD_FOLDER / file.filename



    # -----------------------------
    # Save File
    # -----------------------------

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )



    # -----------------------------
    # Process PDF
    # -----------------------------

    document = pdf_processor.process(
        str(file_path)
    )



    print("=" * 60)
    print("UPLOAD SUCCESS")
    print("Filename :", document.filename)
    print("Pages    :", document.total_pages)
    print("Chunks   :", len(document.chunks))
    print("=" * 60)




    # -----------------------------
    # Store in Chroma
    # -----------------------------

    retriever.add_document(
        document
    )



    # -----------------------------
    # Get Updated PDF List
    # -----------------------------

    pdfs = retriever.list_pdfs()



    print("Available PDFs:")
    print(pdfs)



    return {

        "success": True,

        "message":
        f"{document.filename} uploaded successfully.",

        "filename":
        document.filename,

        "pages":
        document.total_pages,

        "chunks":
        len(document.chunks),

        "pdfs":
        pdfs

    }