import requests
import sqlite3
import json
from datetime import datetime

# --- KONFIGURACJA ---
# TUTAJ PODMIEN WARTOSCI NA SWOJE
API_KEY = "JTQ72WJ-H6Z44CN-NJ194P9-235S88M"
WORKSPACE_SLUG = "risk-policy-analyzer"  # Zmień na swój slug z przeglądarki
BASE_URL = "http://127.0.0.1:3001"  # Domyślny adres AnythingLLM

# Endpoint POST do wysłania wiadomości (zgodnie ze zrzutem z dokumentacji)
CHAT_ENDPOINT = f"{BASE_URL}/api/v1/workspace/{WORKSPACE_SLUG}/chat"

# --- ZAPYTANIE (PROMPT) ---
TEST_PROMPT = """Analyze the Local Branch SOP against the Group ICT Security Policy. 
List all non-compliance issues regarding Passwords, Backups, and Incident Reporting."""


def init_db():
    """Tworzy lokalną bazę SQLite i tabelę do zapisywania wyników ewaluacji."""
    conn = sqlite3.connect('risk_evaluation.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evaluation_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            prompt TEXT,
            model_response TEXT,
            sources_used INTEGER
        )
    ''')
    conn.commit()
    return conn


def send_chat_to_anythingllm(prompt):
    """Wysyła zapytanie do API AnythingLLM używając metody POST."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Body (payload) zgodnie z wymogami API AnythingLLM dla POST /chat
    payload = {
        "message": prompt,
        "mode": "query"  # Zmienione na query dla izolowanych, audytowych zapytań
    }

    print(f"Wysyłam zapytanie do {CHAT_ENDPOINT}...")
    try:
        response = requests.post(CHAT_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Wyrzuci błąd jeśli status to np. 400 lub 500
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Błąd połączenia z API: {e}")
        return None


def save_result_to_db(conn, prompt, api_response):
    """Parsuje odpowiedź z API i zapisuje ją do bazy danych."""
    if not api_response:
        print("Brak odpowiedzi do zapisania.")
        return

    # Wyciąganie kluczowych danych z JSONa zwróconego przez AnythingLLM
    # Dokładna struktura zależy od wersji API, zazwyczaj tekst jest w 'textResponse'
    model_text = api_response.get("textResponse", "Brak tekstu w odpowiedzi")

    # Zliczamy, ilu fragmentów kontekstu (chunks) użył system
    sources_count = len(api_response.get("sources", []))

    timestamp = datetime.now().isoformat()

    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO evaluation_runs (timestamp, prompt, model_response, sources_used)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, prompt, model_text, sources_count))

    conn.commit()
    print("Wynik zapisany w bazie SQLite (risk_evaluation.db).")


def main():
    # 1. Inicjalizacja bazy
    db_conn = init_db()

    # 2. Strzał do API
    result = send_chat_to_anythingllm(TEST_PROMPT)

    # 3. Zapis do bazy
    if result:
        print("\nOtrzymano odpowiedź z modelu.")
        print("-" * 40)
        # Opcjonalne wypisanie kawałka odpowiedzi dla weryfikacji w konsoli
        print(result.get("textResponse", "")[:200] + "...\n")
        print("-" * 40)

        save_result_to_db(db_conn, TEST_PROMPT, result)

    db_conn.close()


if __name__ == "__main__":
    main()