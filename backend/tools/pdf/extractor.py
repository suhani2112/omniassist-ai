import fitz

from backend.tools.pdf.models import PDFDocument, PDFPage


class PDFExtractor:
    """
    Extracts raw text from a PDF and populates a PDFDocument.
    """

    def extract(self, document: PDFDocument) -> PDFDocument:

        pdf = fitz.open(document.filepath)

        pages = []

        for page_number, page in enumerate(pdf, start=1):

            text = page.get_text("text")

            pages.append(
                PDFPage(
                    page_number=page_number,
                    text=text
                )
            )

        pdf.close()

        document.pages = pages
        document.total_pages = len(pages)

        return document