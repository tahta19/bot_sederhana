import streamlit as st
from inference import chat_bot

st.title("Chat Bot Sederhana dengan Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ketik Pesan Disini")
if prompt :
    # user ngirim chat
    response = chat_bot(prompt)
    # chat user muncul
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({
        "role": "user", "content": prompt
    })

    # chat respon muncul
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({
        "role": "assistant", "content": response
    })

