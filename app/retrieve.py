from qdrant_client import QdrantClient
from app.config import *
from app.embeddings import generate_embedding

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def retrieve_chunks(query, top_k=5):
    query_vector = generate_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
    )

    return [point.payload["text"] for point in results.points]