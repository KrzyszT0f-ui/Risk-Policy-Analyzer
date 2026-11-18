import sqlite3


def analyze_db():
    # Połączenie z naszą bazą testową
    conn = sqlite3.connect('risk_evaluation.db')
    cursor = conn.cursor()

    # Zapytanie SQL wyciągające wyniki od najnowszego testu
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

    print(f"Znaleziono {len(rows)} testów w bazie.\n")

    for row in rows:
        run_id, timestamp, sources, response = row
        print(f"--- TEST ID: {run_id} ---")
        print(f"Liczba pobranych fragmentów z wektorowej bazy wiedzy (chunks): {sources}")

        # Automatyczna weryfikacja biznesowa - sprawdzamy, czy model wyłapał regułę 24 godzin
        print("STATUS KONTROLI JAKOŚCI (INCIDENT REPORTING):")
        if "24" in response:
            print("[OK] Model wspomniał o regule 24 godzin. Należy przeczytać, czy wyciągnął właściwy wniosek.")
        else:
            print("[BŁĄD] Model całkowicie zgubił fakt o 24 godzinach z lokalnej procedury (Ślepowidz/Halucynacja).")

        print("\nPEŁNA ODPOWIEDŹ MODELU:")
        print(response)
        print("=" * 80)

    conn.close()


if __name__ == "__main__":
    analyze_db()