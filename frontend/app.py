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
st.write("Ask questions from your knowledge base.")

# -------------------------
# API URL
# -------------------------

API_URL = "http://127.0.0.1:8000/chat"

# -------------------------
# User ID
# -------------------------

USER_ID = "default_user"

# -------------------------
# Session State
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# -------------------------
# Chat Input
# -------------------------

question = st.chat_input("Ask something...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    try:

        response = requests.post(
            API_URL,
            json={
                "user_id": USER_ID,
                "question": question
            }
        )

        if response.status_code == 200:

            answer = response.json()["answer"]

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):
                st.write(answer)

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

            st.write(response.text)

    except Exception as e:

        st.error(
            f"Could not connect to backend:\n{e}"
        )