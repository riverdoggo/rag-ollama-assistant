import requests
from app.config import OLLAMA_BASE_URL, LLM_MODEL

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a precise assistant.
Only answer using the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={"model": LLM_MODEL, "prompt": prompt, "stream": False}
    )

    response.raise_for_status()
    return response.json()["response"]
