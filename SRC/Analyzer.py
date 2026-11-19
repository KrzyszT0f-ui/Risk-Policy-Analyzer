import sqlite3


def analyze_db():
    """Queries the SQLite database and runs a basic quality check on model outputs."""
    conn = sqlite3.connect("risk_evaluation.db")
    cursor = conn.cursor()

    query = """
        SELECT 
            id, 
            timestamp, 
            sources_used, 
            model_response 
        FROM evaluation_runs 
        ORDER BY id DESC
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"Found {len(rows)} evaluation run(s) in the database.\n")

    for row in rows:
        run_id, timestamp, sources, response = row
        print(f"--- TEST ID: {run_id} | TIMESTAMP: {timestamp} ---")
        print(f"Retrieved context chunks from vector DB: {sources}")

        # Automated sanity check: verify if the model captured the 24-hour reporting rule
        print("QUALITY CHECK STATUS (INCIDENT REPORTING):")
        if "24" in response:
            print("[PASS] Model referenced the 24-hour rule. Manual review required to verify reasoning.")
        else:
            print("[FAIL] Model missed the 24-hour reporting rule from the local SOP (potential retrieval miss or hallucination).")

        print("\nFULL MODEL RESPONSE:")
        print(response)
        print("=" * 80)

    conn.close()


if __name__ == "__main__":
    analyze_db()