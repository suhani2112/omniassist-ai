from backend.services.llm_service import LLMService


llm = LLMService()


response1 = llm.generate_response(
    "My name is Suhani"
)

print("\nResponse 1:")
print(response1)


response2 = llm.generate_response(
    "What is my name?"
)

print("\nResponse 2:")
print(response2)