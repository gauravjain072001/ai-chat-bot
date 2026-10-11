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

To enable LLM responses, set `OPENAI_API_KEY` before starting the app. You can optionally set `OPENAI_MODEL` (defaults to `gpt-4o-mini`). Never commit API keys.
