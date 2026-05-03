# streamlit-chat-app

A ChatGPT‑style chat application using Streamlit in Python, without using any external Large Language Model (LLM) or API. Responses are generated locally by reversing the user's input. Conversation history is preserved across turns using `st.session_state`.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

## Run

```bash
uv run streamlit run chat_app.py
```

## Test

```bash
uv run pytest
```

## Project Structure

```
chat_app.py           # Streamlit UI + local response logic
tests/
└── test_responder.py
pyproject.toml
```

## How It Works

The assistant reply is generated entirely locally -> no API calls or LLM involved. `generate_response()` echoes the user's message and appends its reverse:

```
User:      hello
Assistant: You said: 'hello'. Here's my take: olleh
```
