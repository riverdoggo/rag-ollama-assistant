from fastapi import FastAPI
from pydantic import BaseModel
from app.ingest import create_collection, ingest_document
from app.retrieve import retrieve_chunks
from app.generate import generate_answer

app = FastAPI()

class Document(BaseModel):
    text: str

class Query(BaseModel):
    question: str

@app.on_event("startup")
def startup():
    create_collection()

@app.post("/upload")
def upload_document(doc: Document):
    ingest_document(doc.text)
    return {"status": "Document indexed"}

@app.post("/query")
def query_doc(q: Query):
    chunks = retrieve_chunks(q.question)
    answer = generate_answer(q.question, chunks)
    return {
        "answer": answer,
        "retrieved_chunks": chunks
    }
