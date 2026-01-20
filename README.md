# 🛠️ Runbook AI Assistant (RAG-based)

An **AI-powered Production Runbook Assistant** built using **Python, LangChain, FAISS, and OpenAI**.  
It helps engineers **quickly resolve production issues** by answering questions **strictly from official runbook documentation**, preventing hallucinations.

---

## 🚀 What This Project Does

- Ingests a **TXT-based production runbook**
- Converts it into **vector embeddings**
- Stores embeddings locally using **FAISS**
- Answers user queries using **Retrieval-Augmented Generation (RAG)**
- Ensures answers are **grounded only in the runbook**
- Provides **structured, actionable responses** like a senior production engineer

---

## 🧠 Example Use Case

Instead of searching through long runbooks during incidents, engineers can ask:

> “Checkout API is returning 503 errors, how do I fix it?”

And get an **instant, step-by-step resolution**.

---

## 📁 Project Structure

```
txtrunbook/
│
├── runbooks/
│   └── prod_runbook.txt
│
├── ingest.py
├── bot.py
├── runbook_index/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
- Python **3.11**
- OpenAI API Key

---

### 2️⃣ Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

---

## 📥 Ingest the Runbook

```bash
python3 ingest.py
```

This creates a FAISS index locally.

---

## ▶️ Run the Bot

```bash
python3 bot.py
```

---

## 💬 Sample Interaction

**User**
```
Checkout API returning 503 errors
```

**Bot**
```
Root Cause:
Inventory service is down or unreachable.

Resolution Steps:
1. Check inventory-service pod status.
2. Restart pods.
3. Verify DB connectivity.

Validation:
- /health endpoint returns OK
```

---

## 🛑 Unknown Issue Handling

```
Redis cluster is failing
```

**Response**
```
Not found in runbook. Escalate to L3 support.
```

---

## 💰 Cost Notes

- Embedding generation during ingestion is billable
- LLM responses are billable
- File reads and FAISS storage are free

---

## 🔒 Security

- `.env` is git-ignored
- No secrets committed
- Vector indexes regenerated when needed

---

## 🎯 One-Line Summary

A **production-grade RAG-based AI assistant** for resolving incidents using official runbooks only.
