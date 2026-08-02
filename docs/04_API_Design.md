# OmniAssist AI

# API Design Document

Version: 1.0

Author: Suhani Gupta

Status: Designing

---

# 1. Overview

The FastAPI backend exposes REST APIs that allow the frontend and external applications to interact with OmniAssist AI.

The API layer is responsible for receiving requests, validating input, invoking the LangGraph workflow, and returning structured responses.

Base URL

/api/v1

---

# 2. Endpoints

## Health Check

GET /health

Description

Checks whether the backend service is running.

Response

{
    "status": "healthy"
}

---

## Process User Task

POST /query

Description

Processes a user request through the Supervisor Agent workflow.

Request

{
    "query":"Generate placement eligibility report."
}

Response

{
    "response":"...",
    "citations":[...],
    "workflow":"completed"
}

---

## Upload Documents

POST /upload

Description

Uploads enterprise documents to the knowledge base.

Supported Formats

- PDF
- DOCX
- TXT
- CSV

Response

{
    "status":"uploaded"
}

---

## Retrieve Uploaded Documents

GET /documents

Description

Returns uploaded documents.

Response

[
    {
        "document_id":1,
        "name":"PlacementPolicy.pdf"
    }
]

---

## Delete Document

DELETE /documents/{id}

Description

Deletes a document from the knowledge base.

---

## Conversation History

GET /history

Description

Returns previous conversations.

---

## Clear Conversation

DELETE /history

Description

Clears session memory.

---

## Feedback

POST /feedback

Description

Stores user feedback for evaluation.

Request

{
    "rating":5,
    "feedback":"Very Helpful"
}

---

# 3. Error Codes

200

Success

400

Invalid Request

404

Resource Not Found

500

Internal Server Error

---

# 4. Future APIs

POST /agent

POST /workflow

POST /analytics

POST /reports

POST /email

POST /calendar

POST /erp

POST /sql

---

# 5. Authentication (Future)

JWT Authentication

OAuth2

Role-Based Access Control (RBAC)

---

# 6. API Versioning

Current Version

v1

Future Versions

v2

v3