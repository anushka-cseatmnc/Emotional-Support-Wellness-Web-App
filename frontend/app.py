import streamlit as st
import requests

st.title("🧘 Emotional Support & Wellness Chatbot")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip():
        try:
            response = requests.post("http://127.0.0.1:8000/chat", json={"text": user_input})
            if response.status_code == 200:
                data = response.json()
                st.write(f"**AI ({data['sentiment']}):** {data['response']}")
            else:
                st.error("Error communicating with the chatbot.")
        except requests.exceptions.ConnectionError:
            st.error("Backend is not running. Please start the FastAPI server.")
