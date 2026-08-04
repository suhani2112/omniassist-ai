# backend/core/rag_pipeline.py

import json

from backend.core.memory import (
    get_memory,
    save_memory
)

from backend.tools.pdf.vector_store import retriever
from backend.services.llm_service import llm



def extract_memory(question: str):

    prompt = f"""
Extract only permanent user facts.

Examples:

"My name is Rahul"

{{
"name": "Rahul"
}}

"I am learning Python"

{{
"skill": "Python"
}}

Rules:

- Return JSON only.
- Return {{}} if no permanent fact exists.
- Do not explain anything.

User message:

{question}
"""


    response = llm.client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0

    )


    content = response.choices[0].message.content.strip()


    try:
        return json.loads(content)

    except:
        return {}





def ask_omniassist(
    question: str,
    user_id: str = "default_user"
):


    # ---------------------------------
    # 1. Long Term Memory
    # ---------------------------------

    user_memory = get_memory(user_id)


    memory_context = ""


    for key, value in user_memory.items():

        memory_context += f"{key}: {value}\n"





    # ---------------------------------
    # 2. Conversation Memory
    # ---------------------------------

    conversation = llm.memory.get_messages(user_id)


    conversation_context = ""


    for msg in conversation:

        conversation_context += (
            f"{msg['role']}: {msg['content']}\n"
        )





    # ---------------------------------
    # 3. Retrieve PDF Context
    # ---------------------------------

    results = retriever.search(
        question,
        top_k=3
    )


    print("\n===== RETRIEVER OUTPUT =====")
    print(results)
    print("============================\n")



    pdf_context = ""


    if results and "documents" in results:


        docs = results["documents"][0]


        if docs:

            pdf_context = "\n\n".join(docs)





    # ---------------------------------
    # 4. Final Prompt
    # ---------------------------------


    prompt = f"""

You are OmniAssistAI.

You are an expert AI assistant specialized in:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Programming
- Data Science


Important technical context:

- RAG means Retrieval Augmented Generation in Artificial Intelligence.
- CNN means Convolutional Neural Network.
- ML means Machine Learning.


Rules:

1. Answer naturally like ChatGPT.
2. Never return JSON.
3. Never include Python code unless the user asks for code.
4. Never copy PDF text directly.
5. Use PDF context only when relevant.
6. If PDF context is unrelated, ignore it.
7. Do not mention PDF Context or User Memory.
8. Keep answers clear and conversational.
9. For technical questions, answer using your technical knowledge.


-----------------------------

User Memory:

{memory_context}


-----------------------------

Conversation History:

{conversation_context}


-----------------------------

Relevant Knowledge:

{pdf_context}


-----------------------------

User Question:

{question}

"""


    response = llm.client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {
                "role": "system",
                "content": "You are OmniAssistAI, a helpful AI assistant."
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0.3

    )



    answer = response.choices[0].message.content.strip()



    print("\n" + "=" * 80)
    print("QUESTION:")
    print(question)

    print("=" * 80)

    print("ANSWER:")
    print(answer)

    print("=" * 80 + "\n")





    # ---------------------------------
    # 5. Save Conversation Memory
    # ---------------------------------

    llm.memory.add_message(
        user_id,
        "user",
        question
    )


    llm.memory.add_message(
        user_id,
        "assistant",
        answer
    )





    # ---------------------------------
    # 6. Extract Permanent Memory
    # ---------------------------------

    extracted = extract_memory(question)



    for key, value in extracted.items():

        save_memory(
            user_id,
            key,
            value
        )



    return answer