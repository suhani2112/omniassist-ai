import uuid

from backend.tools.pdf.models import PDFChunk, PDFDocument


class PDFChunker:

    def __init__(
        self,
        chunk_size=800,
        overlap=150
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: PDFDocument):

        document.chunks = []

        for page in document.pages:

            text = page.text

            start = 0

            while start < len(text):

                end = start + self.chunk_size

                chunk_text = text[start:end]

                chunk = PDFChunk(
                    chunk_id=str(uuid.uuid4()),
                    page_number=page.page_number,
                    text=chunk_text
                )

                document.chunks.append(chunk)

                start += self.chunk_size - self.overlap

        return document