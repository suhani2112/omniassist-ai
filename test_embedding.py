from backend.tools.pdf.embeddings import EmbeddingGenerator

embedder = EmbeddingGenerator()

vector = embedder.embed(
    "Machine Learning is a subset of Artificial Intelligence."
)

print("Vector Length:", len(vector))

print()

print(vector[:10])