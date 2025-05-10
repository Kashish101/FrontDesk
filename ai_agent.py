import random
import time

# Simulated knowledge base
knowledge_base = {
    "what are your hours?": "We are open from 9 AM to 6 PM.",
    "where are you located?": "We are located at 123 Main St."
}

def answer_question(question):
    """Simulate the AI answering questions"""
    time.sleep(1)  # Simulate AI processing time
    return knowledge_base.get(question.lower(), None)

def request_help(question):
    """Simulate triggering a request for human assistance"""
    print(f"AI doesn't know the answer to: {question}")
    return f"Requesting help for: {question}"
