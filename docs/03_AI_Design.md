# OmniAssist AI

# AI Design Document

Version: 1.0

Author: Suhani Gupta

Status: Designing

---

# 1. Overview

OmniAssist AI is built as a Multi-Agent Enterprise Intelligence Platform.

Instead of relying on a single Large Language Model prompt, the system divides complex tasks among specialized AI agents coordinated using LangGraph.

Each agent has a single responsibility.

The Supervisor Agent decides which agents should execute based on the user's request.

---

# 2. AI Design Philosophy

The platform follows five principles:

1. Think before acting.
2. Retrieve before generating.
3. Use tools whenever required.
4. Validate every important output.
5. Maintain conversational memory.

---

# 3. Multi-Agent Architecture

                         User
                           |
                           v
                  Supervisor Agent
                           |
      -------------------------------------------------
      |        |          |          |                |
      v        v          v          v                v
 Knowledge   Task     Analytics   Report        Memory
  Agent      Agent      Agent      Agent         Agent
      \        |          |          |           /
       \       |          |          |          /
        ----------------------------------------
                        |
                 Validation Agent
                        |
                 Final Response

---

# 4. Agent Responsibilities

## 4.1 Supervisor Agent

Purpose

Acts as the brain of the platform.

Responsibilities

- Understand user intent
- Decide workflow
- Select required agents
- Coordinate execution
- Merge outputs
- Generate final response

Input

User request

Output

Execution Plan

Example

User:

Generate placement eligibility report.

↓

Calls

Knowledge Agent

↓

Analytics Agent

↓

Report Agent

↓

Validation Agent

---

## 4.2 Knowledge Agent

Purpose

Retrieves organization-specific knowledge.

Responsibilities

- Query ChromaDB
- Retrieve relevant documents
- Return citations
- Filter irrelevant information

Input

Search query

Output

Relevant context

Uses

- LangChain Retriever
- ChromaDB
- Sentence Transformers

---

## 4.3 Task Agent

Purpose

Performs organizational tasks.

Examples

- Draft email
- Summarize document
- Generate meeting notes
- Generate policy summary

Future

- Calendar scheduling
- ERP actions
- HR workflows

---

## 4.4 Analytics Agent

Purpose

Performs reasoning over structured data.

Examples

- Attendance analysis
- Placement statistics
- Student performance
- Trend analysis

Future

- Predictive analytics
- Dashboard generation

---

## 4.5 Report Agent

Purpose

Creates structured outputs.

Examples

- PDF reports
- Markdown reports
- Executive summaries
- Weekly reports

---

## 4.6 Memory Agent

Purpose

Maintains context across interactions.

Responsibilities

- Store conversation history
- Remember previous tasks
- Preserve user preferences
- Pass context to other agents

Memory Types

Short-Term Memory

Current conversation

Long-Term Memory (Future)

User preferences

Project history

Organization-specific memory

---

## 4.7 Validation Agent

Purpose

Checks quality before response.

Responsibilities

- Detect hallucinations
- Verify citations
- Check formatting
- Ensure completeness
- Review generated output

---

# 5. Agent Communication

All agents communicate through LangGraph State.

Shared State contains

- User Query
- Retrieved Context
- Current Plan
- Intermediate Outputs
- Memory
- Tool Results
- Final Response

No agent directly communicates with another agent.

All communication occurs through the shared workflow state.

---

# 6. Prompt Strategy

Each agent uses a dedicated system prompt.

Supervisor Prompt

Focus on planning.

Knowledge Prompt

Focus on retrieving accurate context.

Task Prompt

Focus on completing tasks.

Analytics Prompt

Focus on reasoning over structured data.

Validation Prompt

Focus on quality assurance.

---

# 7. Memory Strategy

Current Version

Conversation Buffer Memory

Future Versions

Vector Memory

Knowledge Graph Memory

Long-Term User Memory

---

# 8. Tool Calling

Current Tools

- Document Loader
- RAG Retriever
- Report Generator

Future Tools

- SQL Database
- Calendar
- Email
- ERP
- Slack
- Microsoft Teams
- REST APIs

---

# 9. RAG Pipeline

User Query

↓

Embedding Generation

↓

Vector Search

↓

Top-k Retrieval

↓

Context Ranking

↓

Supervisor Agent

↓

Response Generation

↓

Citation Attachment

---

# 10. Failure Handling

If retrieval fails

↓

Ask user for clarification.

If tool execution fails

↓

Retry.

If retry fails

↓

Fallback response.

If validation fails

↓

Regenerate response.

---

# 11. Future Improvements

- Multi-modal agents
- Voice agents
- Autonomous planning
- Agent collaboration
- Self-reflection
- Human approval workflow
- Multi-agent debate
- Continuous learning