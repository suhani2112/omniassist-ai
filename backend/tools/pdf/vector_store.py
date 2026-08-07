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


        print("✅ ChromaDB Initialized")
        print("Collection:", self.collection.name)
        print("Collection Count:", self.collection.count())



    # ----------------------------------------------------
    # Add PDF
    # ----------------------------------------------------

    def add_document(
        self,
        document: PDFDocument
    ):


        ids = []
        embeddings = []
        documents = []
        metadatas = []



        for chunk in document.chunks:


            ids.append(
                chunk.chunk_id
            )


            embeddings.append(
                self.embedder.embed(
                    chunk.text
                )
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


        print(
            f"✅ Stored {len(ids)} chunks"
        )





    # ----------------------------------------------------
    # Search
    # ----------------------------------------------------

    def search(
        self,
        query,
        top_k=3,
        filename=None
    ):


        query_embedding = self.embedder.embed(
            query
        )



        kwargs = {

            "query_embeddings": [
                query_embedding
            ],

            "n_results": top_k,

            "include": [
                "documents",
                "metadatas",
                "distances"
            ]

        }



        if filename:


            kwargs["where"] = {

                "filename": filename

            }




        results = self.collection.query(
            **kwargs
        )



        print("\n==============================")
        print("Retriever Results")
        print("==============================")



        docs = results.get(
            "documents",
            [[]]
        )[0]


        metas = results.get(
            "metadatas",
            [[]]
        )[0]


        distances = results.get(
            "distances",
            [[]]
        )[0]



        filtered_docs = []

        filtered_meta = []



        # Lower distance = better match
        DISTANCE_THRESHOLD = 0.45




        for doc, meta, distance in zip(
            docs,
            metas,
            distances
        ):


            print(
                f"\nDistance : {distance:.4f}"
            )

            print(
                meta["filename"]
            )

            print(
                doc[:150]
            )



            if distance <= DISTANCE_THRESHOLD:


                filtered_docs.append(
                    doc
                )

                filtered_meta.append(
                    meta
                )


            else:

                print(
                    "❌ Rejected (Low relevance)"
                )




        print("==============================\n")



        return {

            "documents": [
                filtered_docs
            ],

            "metadatas": [
                filtered_meta
            ]

        }





    # ----------------------------------------------------
    # List PDFs
    # ----------------------------------------------------

    def list_pdfs(self):


        data = self.collection.get(
            include=[
                "metadatas"
            ]
        )


        files = set()



        for meta in data["metadatas"]:

            files.add(
                meta["filename"]
            )



        return sorted(
            list(files)
        )






    # ----------------------------------------------------
    # Delete PDF
    # ----------------------------------------------------

    def delete_pdf(
        self,
        filename
    ):


        self.collection.delete(

            where={

                "filename": filename

            }

        )


        print(
            f"Deleted {filename}"
        )





# Global Retriever Object

retriever = PDFVectorStore()