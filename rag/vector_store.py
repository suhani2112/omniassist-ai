from langchain_chroma import Chroma

from rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.embedding = EmbeddingModel().get_model()

        self.db = Chroma(
            persist_directory="data/vector_db",
            embedding_function=self.embedding,
        )

    def add_documents(self, docs):

        self.db.add_documents(docs)

    def as_retriever(self):

        return self.db.as_retriever(search_kwargs={"k": 5})