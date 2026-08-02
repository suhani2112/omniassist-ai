# OmniAssist AI

# System Architecture Document (SDD)

Version: 1.0

Author: Suhani Gupta

Status: Designing

---

# 1. Overview

OmniAssist AI is a modular, multi-agent Enterprise Intelligence Platform designed to assist organizations in performing knowledge-intensive and repetitive tasks using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Agentic AI.

The system is designed around independent AI agents coordinated through LangGraph. Instead of directly answering user questions, OmniAssist understands the task, plans its execution, retrieves relevant organizational knowledge, reasons over the retrieved context, executes required actions, validates the output, and finally generates a response.

The architecture is modular so that different organizational domains (University, Hospital, Hotel, HR, Banking, etc.) can be supported without changing the core system.

---

# 2. High-Level Architecture

                +----------------------+
                |     Streamlit UI     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    FastAPI Backend   |
                +----------+-----------+
                           |
                           v
              +-------------------------+
              | Request Controller/API  |
              +-----------+-------------+
                          |
                          v
              +-------------------------+
              |  LangGraph Orchestrator |
              +-----------+-------------+
                          |
      +-------------------+-------------------+
      |                   |                   |
      v                   v                   v
+-------------+    +--------------+   +---------------+
| Intelligence|    | Knowledge    |   | Execution     |
| Engine      |    | Engine       |   | Engine        |
+-------------+    +--------------+   +---------------+
      |                   |                   |
      +---------+---------+---------+---------+
                          |
                          v
                 +------------------+
                 | Final Response   |
                 +------------------+

---

# 3. Core Components

## 3.1 Frontend

Technology:
- Streamlit

Responsibilities:
- Accept user requests
- Display AI responses
- Upload organizational documents
- Show citations
- Display generated reports
- Display conversation history

---

## 3.2 Backend

Technology:
- FastAPI

Responsibilities:
- REST API
- Request validation
- Session management
- API routing
- Authentication (Future)
- Communication with LangGraph

---

## 3.3 LangGraph Orchestrator

LangGraph is responsible for coordinating all AI agents.

Responsibilities:

- Maintain workflow state
- Route tasks between agents
- Retry failed nodes
- Share memory
- Manage execution flow

---

# 4. Intelligence Engine

The Intelligence Engine is responsible for thinking.

Components:

## Router Agent

Purpose:

Classifies user intent.

Example:

Student asks:

"I want placement eligibility."

↓

Placement Workflow

---

## Planner Agent

Breaks large tasks into smaller executable steps.

Example:

Generate semester report

↓

Collect attendance

↓

Collect marks

↓

Generate summary

---

## Reasoning Agent

Uses LLM reasoning over retrieved context.

Responsibilities:

- Decision making
- Context synthesis
- Multi-step reasoning

---

## Memory Agent

Stores conversation context.

Responsibilities:

- Short-term memory
- Conversation history
- User preferences

---

## Validation Agent

Reviews generated outputs.

Checks:

- Hallucination
- Missing information
- Formatting
- Completeness

---

# 5. Knowledge Engine

Responsible for enterprise knowledge.

Components:

## Document Loader

Loads

- PDFs
- DOCX
- TXT
- CSV

---

## Chunking Module

Splits large documents into smaller chunks.

---

## Embedding Generator

Converts chunks into vector embeddings.

Model:

Sentence Transformers

---

## Vector Database

Technology:

ChromaDB

Stores

- embeddings
- metadata
- document references

---

## Retriever

Retrieves the most relevant chunks.

Supports

- Semantic Search
- Similarity Search

---

## Citation Manager

Provides source references used by the AI.

---

# 6. Execution Engine

Responsible for performing actions.

Current Tools:

- Report Generator
- Email Generator
- Document Summarizer

Future Tools:

- ERP Integration
- Slack
- Microsoft Teams
- Calendar
- Database Query
- Analytics

---

# 7. Data Flow

Step 1

User submits a request.

↓

Step 2

FastAPI receives request.

↓

Step 3

LangGraph starts workflow.

↓

Step 4

Router Agent identifies intent.

↓

Step 5

Planner Agent creates execution plan.

↓

Step 6

Knowledge Engine retrieves relevant information.

↓

Step 7

Reasoning Agent generates response.

↓

Step 8

Execution Engine performs requested actions.

↓

Step 9

Validation Agent verifies response.

↓

Step 10

Final response returned to user.

---

# 8. Technology Stack

Frontend

- Streamlit

Backend

- FastAPI

AI

- LangChain
- LangGraph

Vector Database

- ChromaDB

Embedding Model

- Sentence Transformers

LLM

- OpenAI GPT
- Groq Llama (Configurable)

Database

- SQLite (Initial)
- PostgreSQL (Future)

Deployment

- Docker
- Render / Railway / Azure (Future)

---

# 9. Scalability

The architecture is modular.

Only the Knowledge Base and domain-specific tools need to change to support new industries.

Supported Future Domains

- University
- Hospital
- Hotel
- Banking
- HR
- Manufacturing
- Government

No modifications are required in the orchestration layer.

---

# 10. Future Improvements

- Multi-modal support
- Voice interaction
- Long-term memory
- Multi-user support
- Authentication & Authorization
- Agent collaboration
- Human-in-the-loop approval
- Workflow customization
- Autonomous task scheduling