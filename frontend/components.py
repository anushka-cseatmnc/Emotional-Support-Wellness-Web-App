import streamlit as st

def chat_message(sender, message):
    if sender == "user":
        st.write(f"🧑 You: {message}")
    else:
        st.write(f"🤖 AI: {message}")
