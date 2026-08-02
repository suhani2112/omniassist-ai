from backend.services.llm_service import LLMService


def main():
    llm = LLMService()

    question = "Say hello in one sentence."

    answer = llm.generate_answer(
        question=question,
        context="The assistant should greet the user politely."
    )

    print("=" * 60)
    print("LLM Response")
    print("=" * 60)
    print(answer)


if __name__ == "__main__":
    main()