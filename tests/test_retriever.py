from rag.retriever import Retriever


def main():
    retriever = Retriever()

    question = "What is covered in Week 10?"

    docs = retriever.retrieve(question)

    print("=" * 60)
    print(f"Question: {question}")
    print("=" * 60)

    for i, doc in enumerate(docs, start=1):
        print(f"\nResult {i}")
        print("-" * 60)
        print(doc.page_content)
        print("-" * 60)


if __name__ == "__main__":
    main()