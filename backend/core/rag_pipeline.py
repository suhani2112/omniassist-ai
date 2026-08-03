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
- Return JSON only
- No explanation


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


    content = (
        response
        .choices[0]
        .message
        .content
    )


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

    user_memory = get_memory(
        user_id
    )


    memory_context = ""


    for key, value in user_memory.items():

        memory_context += (
            f"{key}: {value}\n"
        )



    # ---------------------------------
    # 2. Conversation Memory
    # ---------------------------------

    conversation = (
        llm.memory.get_messages(
            user_id
        )
    )


    for msg in conversation:

        memory_context += (

            f"{msg['role']}: "
            f"{msg['content']}\n"

        )



    # ---------------------------------
    # 3. PDF Retrieval
    # ---------------------------------

    results = retriever.search(

        question,

        top_k=5

    )


    pdf_context = ""


    if results and results.get("documents"):

        for doc in results["documents"][0]:

            pdf_context += (
                doc + "\n"
            )



    # ---------------------------------
    # 4. Final Prompt
    # ---------------------------------

    prompt = f"""

You are OmniAssistAI.

Use the following information:

User Memory:

{memory_context}


PDF Context:

{pdf_context}


Question:

{question}


Answer:

"""



    response = llm.client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {
                "role": "system",
                "content":
                "You are OmniAssistAI, a helpful AI assistant."
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0.7

    )



    answer = (

        response
        .choices[0]
        .message
        .content

    )



    # ---------------------------------
    # 5. Save Conversation
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
    # 6. Save Permanent Facts
    # ---------------------------------

    extracted = extract_memory(
        question
    )


    for key, value in extracted.items():

        save_memory(

            user_id,

            key,

            value

        )



    return answer