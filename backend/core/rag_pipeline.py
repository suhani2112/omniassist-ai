import json

from backend.core.memory import (
    get_memory,
    save_memory
)

from backend.tools.pdf.vector_store import retriever
from backend.services.llm_service import llm



# ---------------------------------------------------------
# Permanent Memory Extraction
# ---------------------------------------------------------

def extract_memory(question: str):

    prompt = f"""
Extract only permanent user facts.

Allowed facts:

- name
- city
- location
- profession
- education
- skill
- preference


Examples:

User:
"My name is Rahul"

Output:
{{
"name":"Rahul"
}}


Rules:

- Return JSON only.
- Return {{}} if no permanent fact exists.
- Do not extract PDF information.
- Do not extract questions.
- Do not extract topics.
- Do not extract temporary tasks.


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





# ---------------------------------------------------------
# Main OmniAssist Function
# ---------------------------------------------------------

def ask_omniassist(
    question: str,
    user_id: str = "default_user",
    active_pdf: str = None
):


    # -------------------------------------------------
    # Greeting Handling
    # -------------------------------------------------

    greetings = [
        "hi",
        "hello",
        "hey",
        "hii",
        "hola",
        "good morning",
        "good afternoon",
        "good evening"
    ]


    if question.lower().strip() in greetings:


        answer = (
            "Hello! 👋\n\n"
            "I'm OmniAssistAI.\n\n"
            "You can upload documents and ask questions "
            "about them, or ask me anything."
        )


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


        return answer





    # -------------------------------------------------
    # User Memory
    # -------------------------------------------------

    user_memory = get_memory(user_id)


    memory_context = ""


    for key,value in user_memory.items():

        memory_context += (
            f"{key}: {value}\n"
        )





    # -------------------------------------------------
    # Conversation Memory
    # -------------------------------------------------

    conversation = llm.memory.get_messages(user_id)


    conversation_context = ""


    for msg in conversation:

        conversation_context += (

            f"{msg['role']}: {msg['content']}\n"

        )






    # -------------------------------------------------
    # PDF Retrieval
    # -------------------------------------------------

    pdf_context = ""

    sources = []




    try:


        if active_pdf:


            results = retriever.search(

                query=question,

                top_k=3,

                filename=active_pdf

            )


        else:


            results = retriever.search(

                query=question,

                top_k=3

            )




        if results and results.get("documents"):


            docs = results["documents"][0]

            metas = results["metadatas"][0]



            unique_docs = []



            for doc in docs:


                if doc not in unique_docs:

                    unique_docs.append(doc)



            if unique_docs:

                pdf_context = "\n\n".join(
                    unique_docs
                )



            for meta in metas:


                src = (

                    f"{meta['filename']} | "
                    f"Page {meta['page']}"

                )


                if src not in sources:

                    sources.append(src)




    except Exception as e:


        print(
            "Retriever Error:",
            e
        )





    print("=" * 60)

    print(
        "ACTIVE PDF:",
        active_pdf
    )

    print(
        "PDF CONTEXT:",
        len(pdf_context)
    )

    print(
        "SOURCES:",
        sources
    )

    print("=" * 60)






    # -------------------------------------------------
    # Hybrid AI Prompt
    # -------------------------------------------------

    prompt = f"""

You are OmniAssistAI.

You are a general AI assistant with document understanding ability.



Rules:


1. Answer user questions naturally using your general knowledge.


2. If the uploaded document contains useful information related to the question, use it.


3. If the question is unrelated to the uploaded document, answer using your own knowledge.


4. Never force PDF information into unrelated questions.


5. Never say you don't know only because the PDF does not contain the answer.


6. If PDF information is used, mention sources.


7. Do not mention retrieval, embeddings, vector database, or context.


8. Never generate JSON.





User Memory:

{memory_context}




Conversation:

{conversation_context}




Uploaded Document Information:

{pdf_context}




Question:

{question}

"""




    response = llm.client.chat.completions.create(


        model="llama-3.1-8b-instant",


        messages=[


            {

                "role":"system",

                "content":
                "You are OmniAssistAI."

            },


            {

                "role":"user",

                "content":prompt

            }


        ],


        temperature=0.3

    )




    answer = response.choices[0].message.content.strip()






    # -------------------------------------------------
    # Add Sources Only If PDF Used
    # -------------------------------------------------

    pdf_keywords = [
        "document",
        "pdf",
        "file",
        "roadmap",
        "chapter",
        "week",
        "page"
    ]



    if (
        active_pdf
        and sources
        and pdf_context(
            word in question.lower()
            for word in pdf_keywords
        )
    ):


        answer += "\n\n📚 Sources:\n\n"


        for src in sources:

            answer += (
                f"- {src}\n"
            )







    # -------------------------------------------------
    # Save Conversation
    # -------------------------------------------------

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






    # -------------------------------------------------
    # Save Permanent Memory
    # -------------------------------------------------

    extracted = extract_memory(question)



    for key,value in extracted.items():


        save_memory(

            user_id,

            key,

            value

        )





    return answer