import requests
from app.config import OLLAMA_BASE_URL, EMBED_MODEL

def generate_embedding(text: str):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text}
    )
    response.raise_for_status()
    return response.json()["embedding"]
