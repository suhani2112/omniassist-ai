from pathlib import Path
import shutil

from rag.loader import DocumentLoader
from rag.chunker import DocumentChunker
from rag.vector_store import VectorStore


class DocumentService:
    """
    Handles document upload, processing, and indexing.
    """

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = DocumentChunker()
        self.vector_store = VectorStore()

        self.upload_dir = Path("data/raw/uploads")
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def upload_document(self, file) -> dict:
        """
        Save a document, process it, and index it.
        """

        file_path = self.upload_dir / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        documents = self.loader.load(str(file_path))

        chunks = self.chunker.split(documents)

        self.vector_store.add_documents(chunks)

        return {
            "filename": file.filename,
            "pages": len(documents),
            "chunks": len(chunks),
            "status": "indexed",
        }