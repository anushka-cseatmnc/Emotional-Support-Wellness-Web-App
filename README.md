## Emotional Support & Wellness Web App


## 🌿 Overview

The Emotional Support and Wellness Web App is designed to provide users with AI-driven mental health support, wellness tracking, and emotional assistance. This platform integrates Retrieval-Augmented Generation (RAG) and NLP models to enhance user experience, offering personalized recommendations and interactive chatbot assistance.

## 🔍 Problem Statement

Mental health support is often inaccessible, and many individuals struggle to find immediate emotional assistance. Traditional therapy can be expensive, and self-help resources are not always personalized. Our goal is to bridge this gap by providing an AI-powered emotional support system that offers instant, empathetic, and context-aware responses.

## 💡 Solution

This web app leverages AI-driven sentiment analysis, NLP models, and contextual memory to create a chatbot capable of providing meaningful emotional support. By integrating ChromaDB for past conversation tracking and ChatGroq for AI-generated responses, the platform ensures users receive relevant and personalized support.

## 🚀 Current Progress

## ✅ Features Implemented

FastAPI Backend: Built a backend API using FastAPI for handling chatbot interactions.

AI Chatbot Integration: Implemented a chatbot using LangChain and ChatGroq for emotional support.

Sentiment Analysis: AI analyzes user messages as Positive, Neutral, or Negative.

ChromaDB for Contextual Responses: Stores and retrieves past conversations for improved response generation.

Streamlit Frontend: Developed a simple UI for user interactions with the chatbot.

Basic API Endpoints: Implemented routes for chatbot communication and sentiment analysis.

## 🧞‍♂️ How It Works

User Inputs a Message: The frontend sends a message to the backend API.

Sentiment Analysis: The AI determines the sentiment of the message.

Response Generation: Based on sentiment, an appropriate response is generated.

Context Handling with ChromaDB: Past messages are checked for similarity to improve replies.

Response Displayed: The frontend displays the AI-generated response with sentiment.

## 💜 Impact

Instant Emotional Support: Users receive immediate responses, reducing stress and anxiety.

Personalized Interaction: AI adapts to user emotions for better engagement.

Encouraging Mental Wellness: Provides an accessible platform for emotional well-being.

## Scalability: Can be expanded to support multiple languages and integrate with mental health professionals.

🚀 Upcoming Features & Work in Progress

Enhanced AI Model: Improving chatbot responses with better emotion detection.

User Authentication & Profiles: Allowing users to save their conversation history.

Mood Tracking Dashboard: Graphical representation of emotional trends over time.

Community Support Feature: Anonymous discussion forums for mental health support.

Secure & Private Conversations: Implementing encryption for user data protection.

## 🛠️ Tech Stack

Frontend: Streamlit (UI for chatbot interactions)

Backend: FastAPI

AI/ML: LangChain, ChatGroq (LLM), Sentiment Analysis

Database: ChromaDB (for storing chat history)

Deployment: GitHub

## 📌 Next Steps

Fixing existing errors in chatbot responses.

Enhancing AI-driven emotional support.

Refining frontend UI for a smoother experience.

Implementing user authentication and saving chat history.

🛠️ Note: The project is still in development, and the current repository primarily showcases work in progress.

## Conclusion

This AI-driven Emotional Support & Wellness Web App is an innovative and scalable solution to address the growing need for affordable and accessible mental health support. By leveraging advanced NLP, real-time sentiment analysis, and RAG-based response generation, this app can provide meaningful, emotion-aware interactions without relying on external APIs. With low-latency performance, offline capabilities, and scalability, it is an ideal tool for improving mental well-being on a global scale.



## 🌍 Impact:
🔹 Provides 24/7 mental health support with emotion-aware AI.
🔹 Works without internet dependency, making it useful globally.
🔹 Scalable for counseling centers, therapy apps, or chatbot services.

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
