# 🛡 AI Prompt Injection Firewall

A comprehensive full-stack security application designed to analyze, classify, and mitigate prompt injection attacks against LLMs.

## Features

- **Prompt Analysis:** Analyzes prompts for malicious intent and rule-based threats.
- **Risk Engine:** Calculates a risk score based on rule violations and LLM analysis.
- **Sanitization:** Cleans prompts by stripping dangerous patterns before submission.
- **Dual Interfaces:** Provides a FastAPI backend, a Streamlit dashboard, and a React frontend.
- **Attack Simulator:** Simulates known adversarial prompts for testing.

## Project Structure

- `app.py`: Streamlit-based interactive dashboard.
- `api.py`: FastAPI backend exposing `/analyze` and `/logs` endpoints.
- `frontend/`: React + Vite frontend application.
- `firewall_rules.py`, `sanitizer.py`, `risk_engine.py`, `intent_classifier.py`, `gemini_analyzer.py`: Core logic for prompt analysis and risk calculation.
- `logger.py`, `attack_simulator.py`, `dashboard.py`: Utility and auxiliary components.

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js (for the frontend)

### Backend Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit Dashboard:
   ```bash
   streamlit run app.py
   ```
3. Or run the FastAPI Server:
   ```bash
   python api.py
   # Runs on http://0.0.0.0:8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install Node dependencies:
   ```bash
   npm install
   ```
3. Start the Vite dev server:
   ```bash
   npm run dev
   ```
