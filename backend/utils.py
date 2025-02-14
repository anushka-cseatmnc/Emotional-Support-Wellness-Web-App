import logging
from chains import EmotionalSupportChain

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_test():
    """Runs a sample test for the EmotionalSupportChain."""
    chain = EmotionalSupportChain()
    test_message = "I'm feeling really stressed about my exams."

    sentiment = chain.analyze_sentiment(test_message)
    response = chain.generate_response(test_message, sentiment)

    logging.info(f"Sentiment: {sentiment}")
    logging.info(f"Response: {response}")

if __name__ == "__main__":
    run_test()
