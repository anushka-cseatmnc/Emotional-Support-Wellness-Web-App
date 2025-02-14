import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from db import store_message, retrieve_similar_message

# Load environment variables
load_dotenv()

class EmotionalSupportChain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.7, 
            groq_api_key=os.getenv("GROQ_API_KEY"), 
            model_name="llama-3.1-70b-versatile"
        )

    def analyze_sentiment(self, user_input):
        """
        Determines the sentiment of the message: Positive, Neutral, or Negative.
        """
        prompt_sentiment = PromptTemplate.from_template(
            """
            ### USER MESSAGE:
            {message}
            
            ### INSTRUCTION:
            Determine the sentiment as one of: `Positive`, `Neutral`, or `Negative`.
            Return only the label.
            """
        )
        chain_sentiment = prompt_sentiment | self.llm
        return chain_sentiment.invoke({"message": user_input}).content.strip()

    def generate_response(self, user_input, sentiment):
        """
        Generates an AI response based on sentiment and past interactions.
        """
        # Check for similar past responses in ChromaDB
        previous_response = retrieve_similar_message(user_input)
        if previous_response:
            return previous_response

        prompt_response = PromptTemplate.from_template(
            """
            ### USER MESSAGE:
            {message}
            
            ### SENTIMENT:
            {sentiment}
            
            ### INSTRUCTION:
            Generate a supportive and empathetic response based on the sentiment.
            - If Negative: Provide encouragement and advice.
            - If Neutral: Respond with understanding.
            - If Positive: Reinforce positive emotions.
            """
        )
        chain_response = prompt_response | self.llm
        response = chain_response.invoke({"message": user_input, "sentiment": sentiment}).content.strip()

        # Store new conversation in ChromaDB
        store_message(user_input, response)

        return response
