from backend.tools.pdf.manager import PDFManager
from backend.tools.pdf.extractor import PDFExtractor
from backend.tools.pdf.parser import PDFParser
from backend.tools.pdf.chunker import PDFChunker

manager = PDFManager()
extractor = PDFExtractor()
parser = PDFParser()
chunker = PDFChunker()

document = manager.register_document(
    "backend/storage/uploads/os_notes.pdf"
)

document = extractor.extract(document)
document = parser.parse(document)
document = chunker.chunk(document)

print("Pages :", document.total_pages)
print("Chunks:", len(document.chunks))

print("\n----------------------\n")

print(document.chunks[0].text)