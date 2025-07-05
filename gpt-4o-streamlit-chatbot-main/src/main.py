import os
import json
import streamlit as st
import google.generativeai as genai

# Load config and set API key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
GEMINI_API_KEY = config_data["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit page settings
st.set_page_config(
    page_title="KIXO-CHATGOD",
    page_icon="⚡",
    layout="centered"
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize Gemini 1.5 Flash chat model
if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-1.5-flash")
    st.session_state.chat = model.start_chat(history=[])

chat = st.session_state.chat

# Page title
st.title("⚡ KIXO-CHATGOD")

# Show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
user_prompt = st.chat_input("Ask KIXO-CHATGOD anything...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Send message
    response = chat.send_message(user_prompt)
    assistant_response = response.text

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
