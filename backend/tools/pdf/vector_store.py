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

    # ----------------------------------------------------
    # Add PDF Chunks
    # ----------------------------------------------------

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

    # ----------------------------------------------------
    # Search
    # ----------------------------------------------------

    def search(
        self,
        query,
        top_k=3
    ):

        query_embedding = self.embedder.embed(query)

        results = self.collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k,

            include=[
                "documents",
                "metadatas",
                "distances"
            ]

        )

        print("\n==============================")
        print("Retriever Results")
        print("==============================")

        docs = results.get("documents", [[]])[0]
        distances = results.get("distances", [[]])[0]

        filtered_docs = []

        for doc, distance in zip(docs, distances):

            print(f"\nDistance : {distance:.4f}")
            print(doc[:150])

            # Smaller distance = Better match
            if distance < 1.2:

                filtered_docs.append(doc)

        print("==============================\n")

        return {
            "documents": [filtered_docs]
        }


# Global retriever instance

retriever = PDFVectorStore()