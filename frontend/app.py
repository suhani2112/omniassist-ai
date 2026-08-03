import streamlit as st
import requests


# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="OmniAssistAI",
    page_icon="🤖",
    layout="centered"
)


# -------------------------
# Title
# -------------------------

st.title("🤖 OmniAssistAI")

st.write(
    "Ask questions from your knowledge base."
)


# -------------------------
# API URL
# -------------------------

API_URL = "http://127.0.0.1:8000/chat"



# -------------------------
# Chat Input
# -------------------------

question = st.chat_input(
    "Ask something..."
)


if question:

    # User message
    with st.chat_message("user"):
        st.write(question)


    try:

        response = requests.post(
            API_URL,
            json={
                "question": question
            }
        )


        if response.status_code == 200:

            answer = response.json()["answer"]

            with st.chat_message("assistant"):
                st.write(answer)


        else:

            st.error(
                "API Error: " + str(response.status_code)
            )


    except Exception as e:

        st.error(
            f"Could not connect to backend: {e}"
        )