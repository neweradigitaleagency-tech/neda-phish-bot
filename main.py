from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Create a .env file based on .env.example")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

app = FastAPI(title="Neda Phish Bot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        chat_session = model.start_chat(history=[])
        system_prompt = (
            "Tu es un expert en cybersécurité, spécialisé uniquement dans les attaques de phishing. "
            "Tu aides à comprendre, détecter, prévenir et analyser les attaques de phishing : email frauduleux, "
            "SMShing, usurpation d'identité, sites falsifiés, etc. "
            "Sois précis, utilise des exemples, explique de manière simple mais technique. "
            "Ne réponds pas à des questions hors de ce domaine. "
            "Si la question n'est pas liée au phishing, réponds poliment que tu ne peux pas aider."
        )
        chat_session.send_message(system_prompt)
        response = chat_session.send_message(req.question)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
