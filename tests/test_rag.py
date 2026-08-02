import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from rag.loader import DocumentLoader
from rag.chunker import DocumentChunker
from rag.vector_store import VectorStore


def main():
    # Replace with your own PDF path
    pdf_path = "data/raw/sample.pdf"

    print("Loading document...")
    loader = DocumentLoader()
    docs = loader.load(pdf_path)

    print(f"Loaded {len(docs)} pages")

    for i, doc in enumerate(docs):
        print("=" * 50)
        print(f"PAGE {i+1}")
        print(doc.page_content[:500])

    print("Chunking...")
    chunker = DocumentChunker()
    chunks = chunker.split(docs)
    print(f"Created {len(chunks)} chunks")

    print("Creating vector database...")
    vector_store = VectorStore()
    vector_store.add_documents(chunks)

    print("✅ Documents indexed successfully!")


if __name__ == "__main__":
    main()