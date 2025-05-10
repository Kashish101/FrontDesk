from flask import Flask, render_template
from ai_agent import answer_question, request_help
import time
from db import add_pending_request, resolve_request, get_pending_requests

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page with pending requests"""
    requests = get_pending_requests()
    return render_template('index.html', requests=requests)

@app.route('/receive_call/<question>', methods=['GET'])
def receive_call(question):
    """Simulate receiving a call and asking the AI"""
    print(f"Received call with question: {question}")
    answer = answer_question(question)

    if answer:
        return f"AI Response: {answer}"
    else:
        help_request = request_help(question)
        # Add the request to the pending list
        add_pending_request({
            "question": question,
            "status": "Pending",
            "response": help_request
        })
        return f"AI couldn't answer. {help_request}"

@app.route('/resolve_request/<index>/<answer>', methods=['GET'])
def resolve_request_route(index, answer):
    """Simulate supervisor resolving a help request"""
    try:
        index = int(index)
        if resolve_request(index, answer):
            print(f"AI follows up with: {answer}")
            return f"Request resolved: {answer}"
        else:
            return "Invalid request index."
    except ValueError:
        return "Invalid index format."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
