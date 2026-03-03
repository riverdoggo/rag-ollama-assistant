# RAG Ollama Assistant (Base Version)

## Overview

This project is a fully local Retrieval-Augmented Generation (RAG)
system built using:

-   Ollama for local LLM inference (llama3)
-   Ollama embeddings (nomic-embed-text)
-   Qdrant as the vector database
-   FastAPI as the REST API layer

The goal of this project is to demonstrate a production-oriented GenAI
backend architecture that:

-   Converts documents into embeddings
-   Stores vectors in a vector database
-   Performs semantic similarity search
-   Injects relevant context into an LLM
-   Returns grounded responses through an API

This is the base version (v1) focused on core RAG functionality.

------------------------------------------------------------------------

## Architecture (Base Version)

User → FastAPI → Embedding Generation → Qdrant → Semantic Retrieval →
LLM → Response

### Core Flow

1.  Document is uploaded via `/upload`
2.  Text is chunked into overlapping segments
3.  Each chunk is converted into embeddings
4.  Embeddings are stored in Qdrant using cosine similarity
5.  Query is embedded
6.  Most relevant chunks are retrieved
7.  Retrieved context is injected into LLM prompt
8.  Grounded answer is generated

------------------------------------------------------------------------

## Why This Project Matters

This project demonstrates:

-   RAG pipeline implementation
-   Local LLM deployment (cost-efficient)
-   Vector database integration
-   Embedding-based semantic search
-   Context injection strategies
-   REST API architecture
-   Backend systems thinking

It avoids external API costs by running fully locally.

------------------------------------------------------------------------

## How to Run (Basic Setup)

### 1. Install Ollama

Download and install: https://ollama.com

Pull required models:

    ollama pull llama3
    ollama pull nomic-embed-text

Ensure Ollama is running:

    ollama serve

------------------------------------------------------------------------

### 2. Start Qdrant (Docker)

    docker run -p 6333:6333 qdrant/qdrant

------------------------------------------------------------------------

### 3. Install Dependencies

Inside the project folder:

    pip install -r requirements.txt

------------------------------------------------------------------------

### 4. Start the API

    uvicorn app.main:app --reload

Open Swagger UI:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

### 5. Usage

Upload Document:

POST `/upload`

Example:

{ "text": "Artificial intelligence systems use embeddings and vector
databases." }

Query Document:

POST `/query`

Example:

{ "question": "What does this text talk about?" }

------------------------------------------------------------------------

## Current Limitations (Base Version)

-   No metadata filtering
-   No latency tracking
-   No structured output enforcement
-   No evaluation framework
-   No authentication layer
-   No async optimization
-   No cloud deployment

This is intentionally minimal to focus on core RAG logic.

------------------------------------------------------------------------

## Planned Improvements (Roadmap)

### Short-Term Improvements

-   Add latency measurement (embedding, retrieval, generation timing)
-   Add logging system
-   Add document IDs and chunk indexing metadata
-   Add token estimation tracking
-   Add structured JSON output mode

### Mid-Term Improvements

-   Add evaluation script (retrieval accuracy testing)
-   Add metadata filtering support
-   Add chunk size comparison benchmarking
-   Add streaming responses

### Advanced Improvements

-   Multi-document collections
-   Agent-based query planner
-   Hybrid search (BM25 + vector search)
-   Context window optimization
-   Production Docker Compose setup
-   Deployment to cloud (AWS / Azure / GCP)
-   Monitoring and metrics integration

------------------------------------------------------------------------

## Educational Value

This project is designed as a foundational GenAI systems project.

It focuses on understanding:

-   How RAG works internally
-   How embeddings interact with vector databases
-   How LLM grounding reduces hallucinations
-   How to structure AI systems beyond simple chatbot demos

------------------------------------------------------------------------

## Version

Current version: v1 -- Core RAG Implementation

Future versions will expand toward enterprise-grade AI backend
architecture.
