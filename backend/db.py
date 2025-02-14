import chromadb
from chromadb.config import Settings

# Initialize ChromaDB Client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create a collection
collection = chroma_client.get_or_create_collection(name="chat_history")

def store_message(user_message, ai_response):
    """
    Stores user messages and AI responses in ChromaDB.
    """
    collection.add(
        ids=[str(len(collection.get()["ids"]) + 1)],
        metadatas=[{"user_message": user_message, "ai_response": ai_response}]
    )

def retrieve_similar_message(user_message):
    """
    Retrieves similar messages from ChromaDB for better contextual responses.
    """
    results = collection.query(
        query_texts=[user_message],
        n_results=1
    )
    if results["metadatas"]:
        return results["metadatas"][0].get("ai_response")
    return None
