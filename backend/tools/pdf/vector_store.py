# backend/tools/pdf/vector_store.py

import chromadb

from backend.tools.pdf.embeddings import EmbeddingGenerator
from backend.tools.pdf.models import PDFDocument


class PDFVectorStore:

    def __init__(self):

        self.embedder = EmbeddingGenerator()

        self.client = chromadb.PersistentClient(
            path="backend/storage/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="pdf_documents"
        )


    def add_document(self, document: PDFDocument):

        ids = []
        embeddings = []
        documents = []
        metadatas = []


        for chunk in document.chunks:

            ids.append(chunk.chunk_id)

            embeddings.append(
                self.embedder.embed(chunk.text)
            )

            documents.append(
                chunk.text
            )

            metadatas.append(
                {
                    "document_id": document.document_id,
                    "filename": document.filename,
                    "page": chunk.page_number
                }
            )


        self.collection.add(

            ids=ids,

            embeddings=embeddings,

            documents=documents,

            metadatas=metadatas
        )


    def search(self, query, top_k=5):

        query_embedding = self.embedder.embed(query)


        results = self.collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k
        )


        return results



# Global retriever instance
# Used by rag_pipeline.py

retriever = PDFVectorStore()