# OmniAssistAI 🤖

An AI assistant powered by RAG, LLM, and persistent memory.

## Features

- PDF based Question Answering (RAG)
- ChromaDB vector search
- Groq LLM integration
- Persistent conversation memory
- User-specific memory
- FastAPI backend

## Architecture

User
 ↓
FastAPI
 ↓
RAG Pipeline
 ↓
ChromaDB + SQLite Memory
 ↓
Groq LLM


## Tech Stack

- Python
- FastAPI
- Groq LLM
- ChromaDB
- SQLite
- Sentence Transformers


## Installation

Clone repository:

```bash
git clone <your-repo-url>