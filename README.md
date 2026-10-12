# AI Chat Bot

A Flask conversational assistant with an OpenAI-compatible LLM integration and a deterministic demo fallback when no API key is configured.

## Features
- Real-time chat interface
- Context-aware LLM responses when configured
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

To enable LLM responses, copy `.env.example` to `.env`, add your API key, then start the app. You can optionally change `OPENAI_MODEL` (defaults to `gpt-4o-mini`). The `.env` file is ignored by Git; never commit or share your API key.
