# Neda Phish Bot

Chatbot cybersécurité spécialisé dans la **détection et prévention du phishing**.

Backend **FastAPI** + **Gemini 1.5 Flash**, frontend **React + Vite**.

## Features

- Analyse d'URLs et de messages suspects via IA
- Détection de tentatives de phishing en temps réel
- Interface de chat intuitive
- API REST pour intégration tierce

## Stack

| Backend       | Frontend      | IA              |
|---------------|---------------|-----------------|
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

## API Endpoints

| Method | Path            | Description                |
|--------|-----------------|----------------------------|
| GET    | `/health`       | Health check               |
| POST   | `/analyze`      | Analyze a URL or message   |
| POST   | `/chat`         | Chat with the bot          |

## Environment Variables

| Variable         | Description                |
|------------------|----------------------------|
| `GEMINI_API_KEY` | Google Gemini API key      |
| `CORS_ORIGINS`   | Allowed CORS origins       |

## License

MIT
