from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """
    Generates embeddings for text using a local SentenceTransformer model.
    """

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed(self, text: str):

        return self.model.encode(
            text,
            convert_to_numpy=True
        ).tolist()

    def embed_batch(self, texts):

        vectors = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return vectors.tolist()