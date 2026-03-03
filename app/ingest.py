from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from app.config import *
from app.embeddings import generate_embedding
import uuid

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def create_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
    )

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def ingest_document(text):
    chunks = chunk_text(text)
    points = []

    for chunk in chunks:
        embedding = generate_embedding(chunk)
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={"text": chunk}
            )
        )

    client.upsert(collection_name=COLLECTION_NAME, points=points)
