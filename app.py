import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def generate_reply(message: str) -> str:
    text = message.lower().strip()

    if not text:
        return "Please type a message so I can help you."

    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        payload = {
            "model": os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
            "messages": [
                {"role": "system", "content": "You are a helpful assistant for software, product, and career questions. Be concise and accurate."},
                {"role": "user", "content": message},
            ],
        }
        req = Request(
            "https://api.openai.com/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"].strip()
        except (HTTPError, URLError, KeyError, IndexError, json.JSONDecodeError):
            return "The AI service is unavailable right now. Please try again shortly."

    if "hello" in text or "hi" in text:
        return "Hello! I can help with projects, portfolio ideas, and product strategy."
    if "pdf" in text:
        return "I can help generate a clean PDF document from your content and structure it for reports or delivery."
    if "career" in text or "job" in text or "role" in text:
        return "I can help you explore career paths, skill gaps, and a roadmap based on your current strengths and interests."
    if "project" in text:
        return "I can help you evaluate project ideas, break them down into tasks, and prioritize the most valuable work."
    if "help" in text:
        return "I can provide ideas for AI apps, productivity workflows, and career planning. Ask me anything related to software or product work."
    return (
        "I’m a helpful AI assistant for product, research, and software ideation. "
        "Try asking about PDFs, career planning, projects, or portfolio ideas."
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(force=True)
    message = (payload or {}).get("message", "")
    reply = generate_reply(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
