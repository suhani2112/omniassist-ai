import os
import uuid
from datetime import datetime

import fitz  # PyMuPDF

from backend.tools.pdf.models import (
    PDFDocument,
    PDFPage,
    PDFChunk,
)


class PDFProcessor:

    def __init__(self, chunk_size=800):

        self.chunk_size = chunk_size

    # ----------------------------------------
    # Process PDF
    # ----------------------------------------

    def process(self, pdf_path):

        filename = os.path.basename(pdf_path)

        document = PDFDocument(
            document_id=str(uuid.uuid4()),
            filename=filename,
            filepath=pdf_path,
            upload_time=datetime.now(),
        )

        pdf = fitz.open(pdf_path)

        document.total_pages = len(pdf)

        # -----------------------------
        # Read Pages
        # -----------------------------

        for page_number, page in enumerate(pdf, start=1):

            text = page.get_text().strip()
            print("=" * 60)
            print(f"PAGE {page_number}")
            print("Characters:", len(text))
            print(text[:300])
            print("=" * 60)

            document.pages.append(
                PDFPage(
                    page_number=page_number,
                    text=text
                )
            )

            # -----------------------------
            # Chunking
            # -----------------------------

            start = 0

            while start < len(text):

                chunk_text = text[start:start + self.chunk_size]

                document.chunks.append(
                    PDFChunk(
                        chunk_id=str(uuid.uuid4()),
                        page_number=page_number,
                        text=chunk_text
                    )
                )

                start += self.chunk_size

        pdf.close()

        return document


# Global instance
pdf_processor = PDFProcessor()