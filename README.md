# AI-Driven Risk Policy & SOP Gap Analyzer

## 1. Business Problem
Risk analysts and financial controllers spend countless hours manually cross-referencing local branch Standard Operating Procedures (SOPs) against overarching Group ICT Policies (e.g., DORA, EBA Guidelines). This manual mapping is labor-intensive, scales poorly during post-merger integrations, and is highly susceptible to human fatigue, resulting in critical compliance gaps being overlooked.

## 2. The Solution (PoC)
This Proof of Concept (PoC) is a Retrieval-Augmented Generation (RAG) pipeline designed to automate the detection of procedural deviations. To strictly adhere to Data Privacy, banking secrecy, and GDPR constraints, the solution executes entirely on-premise using a locally hosted Large Language Model (Llama 3.1 8B). Zero data leaves the local environment, ensuring that sensitive internal banking procedures are never exposed to public cloud APIs.

## 3. Architecture & Tech Stack
- **Engine:** AnythingLLM (Vector DB) + Ollama
- **LLM:** Llama 3.1 (8B) - 100% on-premise execution
- **Automation:** Python (REST API integration)
- **Evaluation:** SQLite & native SQL queries

## 4. Why API over UI? (Key Finding)
Initial testing via a standard graphical UI chat interface exposed a critical operational risk: stateful conversation memory and hidden UI parameters caused the model to drop explicit facts (e.g., overlooking a 24-hour incident reporting SLA). By migrating the evaluation to a Python-driven API using stateless, isolated queries (`mode="query"`), the model's extraction accuracy stabilized completely. This proves that programmatic, stateless execution is mandatory for predictable and auditable risk management workflows.

## 5. Human-in-the-Loop & Limitations
This tool operates strictly under a "Human-in-the-Loop" (HITL) governance model. The AI does not make final compliance decisions; it functions as a high-speed triage assistant. It generates an Exception Report highlighting specific deviations (e.g., 60 vs. 90-day password rotation), which a human Risk Analyst must then review and validate. While the model excels at semantic text extraction, it is not trusted with quantitative logic or absolute decision-making without expert oversight.

## 6. How to run (For technical review)
1. Ensure Ollama is running `llama3.1:8b` locally.
2. Setup an AnythingLLM Workspace and upload the provided `.txt` files located in `/data`.
3. Generate an API Key in AnythingLLM and update the `API_KEY` variable in `src/evaluator.py`.
4. Run `python src/evaluator.py` to trigger the automated gap analysis via API.
5. Run `python src/analyzer.py` to query the SQLite database and evaluate the pipeline's extraction accuracy.
