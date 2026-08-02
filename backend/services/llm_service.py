import os
from dotenv import load_dotenv
from groq import Groq

from backend.memory.conversation_memory import ConversationMemory


load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is missing in .env file")


        self.client = Groq(
            api_key=api_key
        )

        self.memory = ConversationMemory()


    def generate_response(self, prompt: str):

        # Store user message
        self.memory.add_message(
            "user",
            prompt
        )


        messages = [
            {
                "role": "system",
                "content": "You are OmniAssistAI, an intelligent AI assistant."
            }
        ]


        # Add conversation history
        messages.extend(
            self.memory.get_messages()
        )


        response = self.client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=messages,

            temperature=0.7
        )


        answer = response.choices[0].message.content


        # Store assistant response
        self.memory.add_message(
            "assistant",
            answer
        )


        return answer