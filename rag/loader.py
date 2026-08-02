from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)


class DocumentLoader:
    """Loads PDF, DOCX and TXT documents."""

    def load(self, file_path: str):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found.")

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            loader = PyPDFLoader(file_path)

        elif suffix == ".docx":
            loader = Docx2txtLoader(file_path)

        elif suffix == ".txt":
            loader = TextLoader(file_path, encoding="utf-8")

        else:
            raise ValueError(f"Unsupported file type: {suffix}")

        docs = loader.load()

        # Remove empty pages
        docs = [doc for doc in docs if doc.page_content.strip()]

        if not docs:
            raise ValueError(
                "No readable text found. "
                "The document may be scanned, encrypted, or corrupted."
            )

        return docs