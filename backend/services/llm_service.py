import os

from dotenv import load_dotenv
from groq import Groq

from backend.memory.conversation_memory import ConversationMemory


load_dotenv()



class LLMService:


    def __init__(self):

        api_key = os.getenv(
            "GROQ_API_KEY"
        )


        if not api_key:

            raise ValueError(
                "GROQ_API_KEY is missing in .env file"
            )


        self.client = Groq(
            api_key=api_key
        )


        self.memory = ConversationMemory()


        self.user_id = "default_user"


        self.system_prompt = (

            "You are OmniAssistAI, an intelligent AI assistant. "

            "Be helpful, accurate, and concise."

        )




    def generate_response(
        self,
        prompt: str,
        use_memory: bool = True
    ):


        if use_memory:


            # Save user message

            self.memory.add_message(

                self.user_id,

                "user",

                prompt

            )


            messages = [

                {
                    "role": "system",
                    "content": self.system_prompt
                }

            ]


            messages.extend(

                self.memory.get_messages(
                    self.user_id
                )

            )



        else:


            messages = [

                {
                    "role": "system",
                    "content": self.system_prompt
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ]



        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=messages,

            temperature=0.7

        )



        answer = (

            response

            .choices[0]

            .message

            .content

            .strip()

        )



        if answer.startswith('"') and answer.endswith('"'):

            answer = answer[1:-1]



        if use_memory:


            # Save assistant response

            self.memory.add_message(

                self.user_id,

                "assistant",

                answer

            )



        return answer





    def clear_memory(self):


        self.memory.clear(

            self.user_id

        )




    def get_memory(self):


        return self.memory.get_messages(

            self.user_id

        )





# Global LLM instance

llm = LLMService()