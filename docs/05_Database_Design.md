# OmniAssist AI

# Database Design Document

Version: 1.0

Author: Suhani Gupta

Status: Designing

---

# 1. Overview

The database stores application metadata, conversation history, uploaded documents, and system configuration.

Vector embeddings are stored separately in ChromaDB.

---

# 2. Database Choice

Current

SQLite

Future

PostgreSQL

---

# 3. Tables

## Users (Future)

| Field | Type |
|-------|------|
| id | Integer |
| name | String |
| email | String |
| created_at | Timestamp |

---

## Conversations

| Field | Type |
|-------|------|
| id | Integer |
| session_id | String |
| user_query | Text |
| ai_response | Text |
| timestamp | Timestamp |

---

## Documents

| Field | Type |
|-------|------|
| id | Integer |
| file_name | String |
| file_type | String |
| upload_date | Timestamp |

---

## Feedback

| Field | Type |
|-------|------|
| id | Integer |
| rating | Integer |
| feedback | Text |
| timestamp | Timestamp |

---

# 4. Vector Database

Technology

ChromaDB

Stores

- Embeddings
- Metadata
- Chunk IDs
- Document References

---

# 5. Relationships

One User

↓

Many Conversations

One Document

↓

Many Chunks

One Chunk

↓

One Embedding

---

# 6. Future Database

- PostgreSQL
- Redis
- Neo4j Knowledge Graph

---

# 7. Backup Strategy

Daily Backup

Weekly Snapshot

Cloud Storage

---

# 8. Scalability

Application Database

↓

PostgreSQL

Knowledge Database

↓

ChromaDB

Caching

↓

Redis