from fastapi import FastAPI
from chains import EmotionalSupportChain
import uvicorn

app = FastAPI()
chatbot = EmotionalSupportChain()

@app.get("/")
def home():
    return {"message": "Emotional Support API Running"}

@app.post("/chat/")
def chat_response(data: dict):
    """Handles text queries and returns an AI response."""
    user_message = data.get("text", "")
    
    if not user_message:
        return {"error": "No message provided"}

    sentiment = chatbot.analyze_sentiment(user_message)
    response = chatbot.generate_response(user_message, sentiment)

    return {"sentiment": sentiment, "response": response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
