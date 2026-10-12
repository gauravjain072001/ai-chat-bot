# AI Chat Bot

A Flask conversational assistant with local Ollama support, optional OpenAI API support, and a deterministic demo fallback.

## Features
- Real-time chat interface
- Local LLM responses through Ollama (no per-request API charge)
- Optional OpenAI API responses
- No-key demo mode for local testing
- Easy to extend with OpenAI or other LLM APIs

## Run locally
```bash
cd ai-chatbot-portfolio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

Install [Ollama](https://ollama.com/download/windows), then download the local model once:

```powershell
ollama pull qwen2.5:3b
```

Copy `.env.example` to `.env`, keep `LLM_PROVIDER=ollama`, and start the app. Ollama must be running locally. To use the optional paid OpenAI API instead, set `LLM_PROVIDER=openai` and add `OPENAI_API_KEY` in `.env`. The `.env` file is ignored by Git.
