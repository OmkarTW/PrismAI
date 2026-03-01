# 🧠 PrismAI

An AI-powered multi-agent coding assistant that analyzes, explains, fixes, scores, and generates personalized practice for student code across multiple programming languages.

Built with **FastAPI + Groq LLM + Modular Multi-Agent Architecture**.

---

## 🚀 Problem Statement

Students learning to code often struggle with:

- Lack of personalized feedback
- Understanding logical mistakes
- Identifying recurring weaknesses
- Getting targeted practice for improvement

Most tools only check syntax or give generic responses. PrismAI acts as an adaptive AI tutor that not only analyzes code but learns from user mistakes and generates personalized improvement plans.

---

## ✨ Features

### 🔎 Code Analysis
- Detects syntax errors and logical mistakes
- Highlights inefficiencies
- Assigns clarity score (0–10)
- Generates concise summary

### 🛠 Fix Agent
- Identifies root issue
- Returns corrected code with clear explanation

### 📘 Explanation Agent
- Beginner mode — simple, approachable breakdown
- Interview mode — deeper technical explanation
- Step-by-step logic walkthrough

### 📊 Scoring Agent
- Syntax, logic, clarity, and robustness scores
- Overall evaluation out of 10

### 🧩 Practice Agent
- Generates similar and challenge problems
- Provides structured hints

### 🔧 Correction Engine
- Tracks recurring mistakes across sessions
- Identifies common weakness patterns
- Generates 5 targeted practice questions
- Builds personalized improvement plans

---

## 🏗 Architecture

PrismAI uses a modular multi-agent pipeline orchestrated through a centralized `run_pipeline()`:

```
analyzer_agent
pedagogy_agent
fix_agent
practice_agent
scoring_agent
mistake_fixer_agent
memory_agent
intent_router
```

Each agent operates independently with structured JSON output, timeout protection, graceful fallback handling, and safe parsing.

---

## 🛡 Safety & Reliability

- Prompt injection detection
- Input validation (max 5000 characters)
- Graceful fallback responses — no crashes or infinite spinners
- Safe JSON parsing
- CORS enabled for frontend integration

---

## 🌐 API

### POST `/run`

**Request Body:**

```json
{
  "code": "string",
  "language": "c | cpp | java | python | csharp | javascript",
  "mode": "beginner | interview",
  "user_query": "string",
  "user_id": "string",
  "intent": "analyze | explain | fix | practice | score | full_review | mistake_fixer"
}
```

**Example Response (Full Review):**

```json
{
  "analysis": {},
  "explanation": "...",
  "fix": {},
  "practice": {},
  "score": {}
}
```

---

## 📁 Project Structure

```
PrismAI/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── analyzer_agent.py
│   │   │   ├── execution_agent.py
│   │   │   ├── fix_agent.py
│   │   │   ├── intent_router.py
│   │   │   ├── memory_agent.py
│   │   │   ├── mistake_fixer_agent.py
│   │   │   ├── pedagogy_agent.py
│   │   │   ├── practice_agent.py
│   │   │   └── scoring_agent.py
│   │   ├── memory/
│   │   │   ├── memory_data.json
│   │   │   └── memory_store.py
│   │   ├── services/
│   │   │   ├── llm_service.py
│   │   │   ├── pipeline.py
│   │   │   └── sandbox.py
│   │   ├── utils/
│   │   │   ├── formatters.py
│   │   │   ├── injection_guard.py
│   │   │   └── validators.py
│   │   ├── config.py
│   │   ├── main.py
│   │   └── schemas.py
│   ├── tests/
│   │   ├── test_pipeline.py
│   │   └── test_security.py
│   ├── .env
│   └── requirements.txt
├── frontend/
│   ├── app.js
│   ├── index.html
│   ├── prismai-logo.png
│   └── styles.css
├── docs/
│   └── test_cases.md
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
cd PrismAI
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add environment variables

Create a `.env` file inside `/backend`:

```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` to explore the API, or open `frontend/index.html` directly in your browser.

---

## 🧠 What Makes This Different

- True multi-agent architecture — not a single monolithic LLM call
- Structured JSON outputs for reliable frontend rendering
- Memory-based personalized feedback that improves per user over time
- Graceful fallback system — no crashes, no broken UI states
- Supports C, C++, Python, Java, C#, and JavaScript

---

## ⚠️ Limitations

- LLM output quality depends on Groq model availability
- Memory is stored locally in JSON (not a database)
- Practice problem difficulty may vary

---

## 🧑‍💻 Authors

Built for [Hackathon Name] by [Your Names Here].
