import os
import sqlite3
from datetime import datetime
import requests

# --- CONFIGURATION ---
API_KEY = os.getenv("ANYTHINGLLM_API_KEY")
if not API_KEY:
    raise ValueError("Missing ANYTHINGLLM_API_KEY environment variable.")

WORKSPACE_SLUG = "risk-policy-analyzer"
BASE_URL = "http://127.0.0.1:3001"  # Default local AnythingLLM address

# POST endpoint for sending a chat/query message to a workspace
CHAT_ENDPOINT = f"{BASE_URL}/api/v1/workspace/{WORKSPACE_SLUG}/chat"

# --- EVALUATION PROMPT ---
TEST_PROMPT = """Analyze the Local Branch SOP against the Group ICT Security Policy. 
List all non-compliance issues regarding Passwords, Backups, and Incident Reporting."""


def init_db():
    """Creates a local SQLite database and table to store evaluation runs."""
    conn = sqlite3.connect("risk_evaluation.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluation_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            prompt TEXT,
            model_response TEXT,
            sources_used INTEGER
        )
    """)
    conn.commit()
    return conn


def send_chat_to_anythingllm(prompt):
    """Sends a prompt to the AnythingLLM API using HTTP POST."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Payload configured in 'query' mode for stateless, isolated audit runs
    payload = {
        "message": prompt,
        "mode": "query",
    }

    print(f"Sending request to {CHAT_ENDPOINT}...")
    try:
        response = requests.post(CHAT_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API connection error: {e}")
        return None


def save_result_to_db(conn, prompt, api_response):
    """Parses the API response and stores the result in SQLite."""
    if not api_response:
        print("No response to save.")
        return

    model_text = api_response.get("textResponse", "No text returned in response")
    sources_count = len(api_response.get("sources", []))
    timestamp = datetime.now().isoformat()

    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO evaluation_runs (timestamp, prompt, model_response, sources_used)
        VALUES (?, ?, ?, ?)
        """,
        (timestamp, prompt, model_text, sources_count),
    )

    conn.commit()
    print("Result saved to SQLite database (risk_evaluation.db).")


def main():
    # 1. Initialize database
    db_conn = init_db()

    # 2. Query the API
    result = send_chat_to_anythingllm(TEST_PROMPT)

    # 3. Save results
    if result:
        print("\nModel response received.")
        print("-" * 40)
        # Print a short preview for console verification
        print(result.get("textResponse", "")[:200] + "...\n")
        print("-" * 40)

        save_result_to_db(db_conn, TEST_PROMPT, result)

    db_conn.close()


if __name__ == "__main__":
    main()