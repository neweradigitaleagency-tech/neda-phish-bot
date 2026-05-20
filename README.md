# Neda Phish Bot

Chatbot cybersécurité spécialisé dans la détection et prévention du **phishing**. Backend **FastAPI** + **Gemini 1.5 Flash**, frontend **React + Vite**.

## Stack

| Backend | Frontend | IA |
|---------|----------|----|
| FastAPI + Pydantic | React + Vite | Gemini 1.5 Flash |

## Quick Start

### Backend
```bash
pip install -r requirements.txt
cp .env.example .env   # add your GEMINI_API_KEY
uvicorn main:app --reload
```

### Frontend
```bash
cd chatbot-cyber
npm install
npm run dev
```
