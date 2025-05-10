# Human-in-the-Loop AI Supervisor

## Description
This project simulates an AI receptionist system that escalates questions it can't answer to a human supervisor. Once the supervisor responds, the AI updates its knowledge base.

## Setup Instructions
1. Clone this repository or open it in Replit.
2. Install the dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app with:
    ```bash
    python app.py
    ```

## Design Decisions
- **AI Knowledge Base**: Simulated with a dictionary in `ai_agent.py`.
- **Request Management**: Pending requests are stored in-memory (can be replaced with Firebase/DynamoDB for production).
- **Supervisor UI**: Simple interface to manage pending requests.

## Future Improvements
- Integrate a real-time call system (e.g., Twilio).
- Scale the database to handle a larger number of requests.

