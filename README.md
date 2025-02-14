## Emotional Support & Wellness Web App

![image](https://github.com/user-attachments/assets/39440fc0-602d-45eb-ae0a-47e9b8bf680d)



## 🌿 Overview

The Emotional Support and Wellness Web App is designed to provide users with AI-driven mental health support, wellness tracking, and emotional assistance. This platform integrates Retrieval-Augmented Generation (RAG) and NLP models to enhance user experience, offering personalized recommendations and interactive chatbot assistance.

## 🔍 Problem Statement

Mental health support is often inaccessible, and many individuals struggle to find immediate emotional assistance. Traditional therapy can be expensive, and self-help resources are not always personalized. Our goal is to bridge this gap by providing an AI-powered emotional support system that offers instant, empathetic, and context-aware responses.

## 💡 Solution

This web app leverages AI-driven sentiment analysis, NLP models, and contextual memory to create a chatbot capable of providing meaningful emotional support. By integrating ChromaDB for past conversation tracking and ChatGroq for AI-generated responses, the platform ensures users receive relevant and personalized support.

# 🌿 Emotional Support & Wellness Web App

## 🔍 Overview
The **Emotional Support and Wellness Web App** is an AI-powered platform providing mental health support, wellness tracking, and emotional assistance. Using **Retrieval-Augmented Generation (RAG)** and **NLP models**, it delivers **empathetic, context-aware, and personalized** responses to users.

## 🚨 Problem Statement
Mental health support is often inaccessible, with therapy being expensive and self-help resources lacking personalization. Our goal is to bridge this gap by **offering an AI-driven emotional support system** that provides **instant, empathetic, and intelligent** responses.

## 💡 Solution
This app integrates **sentiment analysis, contextual memory (ChromaDB), and AI-driven responses (ChatGroq)** to create a meaningful emotional support chatbot. Users receive responses tailored to their emotional state, enhancing engagement and mental well-being.

---

## 🚀 Current Progress
### ✅ Features Implemented
- **FastAPI Backend:** API handling chatbot interactions.
- **AI Chatbot Integration:** LangChain + ChatGroq-powered emotional support chatbot.
- **Sentiment Analysis:** AI categorizes user emotions as **Positive, Neutral, or Negative**.
- **ChromaDB for Contextual Responses:** Stores and retrieves past conversations for enhanced replies.
- **Streamlit Frontend:** Interactive UI for chatbot interactions.
- **Basic API Endpoints:** Implemented routes for communication and sentiment analysis.

---

## 🧞‍♂️ How It Works
1. **User Inputs a Message** → Sent to backend API.
2. **Sentiment Analysis** → AI detects emotion.
3. **Response Generation** → AI formulates an empathetic reply.
4. **Context Handling with ChromaDB** → Past interactions refine responses.
5. **Response Displayed** → AI-generated response shown in frontend.

## 🔥 Upcoming Features & Work in Progress
- **Enhanced AI Model:** More refined emotion detection.
- **User Authentication & Profiles:** Saving user conversation history.
- **Mood Tracking Dashboard:** Graphical insights into emotional trends.
- **Community Support Feature:** Anonymous mental health discussion forums.
- **Secure & Private Conversations:** Encrypted user data protection.

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Chatbot UI)
- **Backend:** FastAPI
- **AI/ML:** LangChain, ChatGroq (LLM), Sentiment Analysis
- **Database:** ChromaDB (Chat history storage)
- **Deployment:** GitHub

---

## 📌 Next Steps
🔹 Fix chatbot response errors.  
🔹 Enhance AI-driven emotional support.  
🔹 Improve frontend UI for seamless interactions.  
🔹 Implement user authentication & chat history saving.  

### 🚀 Why It Matters:
🔹 **24/7 Mental Health Support** → AI-driven, always available.  
🔹 **Offline Capability** → No internet dependency for global accessibility.  
🔹 **Scalable** → Useful for **counseling centers, therapy apps,** and **chatbot services**.  

## Conclusion

This AI-driven Emotional Support & Wellness Web App is an innovative and scalable solution to address the growing need for affordable and accessible mental health support. By leveraging advanced NLP, real-time sentiment analysis, and RAG-based response generation, this app can provide meaningful, emotion-aware interactions without relying on external APIs. With low-latency performance, offline capabilities, and scalability, it is an ideal tool for improving mental well-being on a global scale.



## 🌍 Impact:
🔹 Provides 24/7 mental health support with emotion-aware AI.
🔹 Works without internet dependency, making it useful globally.
🔹 Scalable for counseling centers, therapy apps, or chatbot services.
![image](https://github.com/user-attachments/assets/fd9bcf72-5237-49f3-86ba-c396c0200521)

This application has the potential to make a significant positive impact in the mental health space.


## Emotional-Support-App/
│── backend/
│   ├── main.py                 # FastAPI backend
│   ├── models.py               # ML models (BERT/RoBERTa, FAISS)
│   ├── database.py             # FAISS/ChromaDB for storing responses
│   ├── requirements.txt        # Backend dependencies
│── frontend/
│   ├── app.py                  # Streamlit frontend UI
│   ├── components.py           # UI components for chat
│   ├── requirements.txt        # Frontend dependencies
│── data/
│   ├── responses.json          # Predefined responses for RAG
│── models/
│   ├── sentiment_model.pt      # Trained Sentiment Analysis Model
│── README.md                   # Project documentation
│── run.sh                      # Shell script to start backend and frontend

## 🛠️ Note

The project is still in development, and the current repository primarily showcases work in progress.
