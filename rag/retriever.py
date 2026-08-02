from rag.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most relevant chunks from ChromaDB.
    """

    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(self, query: str, k: int = 4):
        """
        Returns the top-k most relevant chunks.
        """

        return self.vector_store.db.similarity_search(
            query=query,
            k=k
        )