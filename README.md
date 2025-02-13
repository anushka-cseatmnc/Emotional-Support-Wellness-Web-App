# -Emotional-Support-Wellness-Web-App
🛠 Tech Stack:
Frontend: Streamlit
Backend: FastAPI (with WebSockets for real-time chat)
ML Models: BERT/RoBERTa for sentiment analysis, RAG with FAISS for response retrieval
Database: FAISS/ChromaDB (local vector storage)
Libraries: PyTorch, Transformers, SentenceTransformers, Scikit-learn, NLTK
🧩 Problem It Solves:
Mental health support is expensive & inaccessible. This app provides real-time emotional support using AI.

🚀 Unique Selling Proposition (USP):
✅ Real-time responses with dynamic emotion analysis
✅ No external API dependency (works fully offline if needed)
✅ Retrieval-Augmented Generation (RAG) for context-aware responses

⚡ Scalability:
Can handle thousands of users with FAISS for fast similarity searches.
Asynchronous WebSockets ensure low-latency messaging.
Deployable on any local/cloud system without external APIs.
📊 Complexity:
Sentiment Classification: O(n) (text tokenization + BERT inference)
RAG Query Retrieval: O(log n) (FAISS indexing for fast retrieval)
WebSocket Real-Time Processing: O(1) (constant time per user message)
🔢 DSA & Optimizations Used:
✔ FAISS Indexing (for nearest neighbor search)
✔ Trie for Fast Query Matching (optimizing keyword-based responses)
✔ Asynchronous Processing (reducing response time bottlenecks)

🌍 Impact:
🔹 Provides 24/7 mental health support with emotion-aware AI.
🔹 Works without internet dependency, making it useful globally.
🔹 Scalable for counseling centers, therapy apps, or chatbot services.
