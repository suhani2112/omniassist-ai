from backend.tools.pdf.manager import PDFManager
from backend.tools.pdf.extractor import PDFExtractor
from backend.tools.pdf.parser import PDFParser
from backend.tools.pdf.chunker import PDFChunker
from backend.tools.pdf.vector_store import PDFVectorStore

manager = PDFManager()
extractor = PDFExtractor()
parser = PDFParser()
chunker = PDFChunker()
store = PDFVectorStore()

document = manager.register_document(
    "backend/storage/uploads/os_notes.pdf"
)

document = extractor.extract(document)
document = parser.parse(document)
document = chunker.chunk(document)

store.add_document(document)

print("Document Stored Successfully!")

results = store.search(
    "What is Prompt Engineering?"
)

print(results)