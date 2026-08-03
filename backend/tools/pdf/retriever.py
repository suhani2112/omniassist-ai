from backend.tools.pdf.vector_store import PDFVectorStore


class PDFRetriever:

    def __init__(self):

        self.store = PDFVectorStore()

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        results = self.store.search(
            query=query,
            top_k=top_k
        )

        chunks = []

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for doc, meta, distance in zip(
            documents,
            metadatas,
            distances
        ):

            chunks.append(

                {
                    "text": doc,
                    "page": meta.get("page"),
                    "filename": meta.get("filename"),
                    "distance": distance
                }

            )

        return chunks