import re

from backend.tools.pdf.models import PDFDocument


class PDFParser:
    """
    Cleans extracted PDF text.
    """

    def parse(self, document: PDFDocument) -> PDFDocument:

        for page in document.pages:

            text = page.text

            # Remove multiple spaces
            text = re.sub(r"[ \t]+", " ", text)

            # Remove excessive blank lines
            text = re.sub(r"\n{3,}", "\n\n", text)

            # Strip leading/trailing whitespace
            text = text.strip()

            page.text = text

        return document