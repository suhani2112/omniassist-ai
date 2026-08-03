from backend.tools.pdf.retriever import PDFRetriever

retriever = PDFRetriever()

results = retriever.retrieve(
    "What is Prompt Engineering?"
)

print()

print("=" * 60)

for i, chunk in enumerate(results, start=1):

    print(f"\nResult {i}")

    print(f"Page : {chunk['page']}")

    print(f"File : {chunk['filename']}")

    print(f"Distance : {chunk['distance']:.4f}")

    print()

    print(chunk["text"][:300])

    print("\n" + "-" * 60)