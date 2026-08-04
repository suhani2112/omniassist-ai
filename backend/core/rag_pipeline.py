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
    # 1. Long-Term Memory
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
    # 3. Retrieve PDF Chunks
    # ---------------------------------

    results = retriever.search(
        question,
        top_k=2
    )

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

Follow these rules carefully:

1. Answer naturally like ChatGPT.
2. Never return JSON.
3. Never include Python code unless the user explicitly asks for code.
4. Never copy the PDF text verbatim.
5. Use the PDF only if it is relevant.
6. If the PDF is unrelated, ignore it and answer using your general knowledge.
7. Do not mention "PDF Context" or "User Memory" in your answer.
8. Keep the answer clear, concise and conversational.

-------------------------
User Memory
-------------------------
{memory_context}

-------------------------
Conversation History
-------------------------
{conversation_context}

-------------------------
Relevant PDF Context
-------------------------
{pdf_context}

-------------------------
Question
-------------------------
{question}
"""

    response = llm.client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": "You are OmniAssistAI."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5

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
    # 6. Save Permanent Memory
    # ---------------------------------

    extracted = extract_memory(question)

    for key, value in extracted.items():

        save_memory(
            user_id,
            key,
            value
        )

    return answer