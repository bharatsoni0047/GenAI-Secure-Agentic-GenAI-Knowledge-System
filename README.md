AgenticRAG – Enterprise Multi-Modal AI Assistant

AgenticRAG is an enterprise-grade, agent-based Generative AI system that allows users to query structured data (SQL) and unstructured data (PDFs, Excel, Images, Text) using natural language.
The system combines Agentic workflows, RAG (Retrieval-Augmented Generation), and secure API access to deliver accurate, explainable answers.

Key Capabilities
1. Natural Language to SQL Querying

Users can ask questions in plain English, and the system intelligently converts them into valid SQL queries and executes them on a connected MySQL database.

Example use cases:

Fetching top-paid employees

Aggregations like totals, averages, rankings

Table-level analytical queries

2. Multi-Modal RAG (Retrieval-Augmented Generation)

The system supports querying knowledge from multiple document types:

PDF documents (policies, reports, manuals)

Excel files (structured reports, analytics sheets)

Images (via OCR for scanned documents)

Plain text files

Relevant content is retrieved from a vector database and used to generate grounded, context-aware answers.

3. Agent-Based Architecture

The project follows an Agentic design, where responsibilities are clearly separated:

Query Agent – Understands user intent and routes the query

SQL Agent – Handles database-related questions

RAG Agent – Retrieves and reasons over document data

Guard / Validation Logic – Ensures safe and valid execution

This architecture makes the system modular, scalable, and enterprise-ready.

4. Secure Access Using JWT Authentication

Access to the system is protected using JWT (JSON Web Token) authentication.

Users must log in to obtain a token

Only authorized users can query data

Easy to extend for role-based access (admin / user)

This prevents unauthorized access to sensitive databases and documents.

5. Database Agnostic Design

The system is designed so that any user can connect their own database by simply updating environment configuration.

No code changes required

Supports MySQL (can be extended to others)

Configuration-driven setup

6. API + UI Separation

Backend: FastAPI handles authentication, query processing, and agent orchestration

Frontend: Streamlit provides a simple UI for interacting with the system

This separation allows easy deployment, scaling, and future UI upgrades.

Data Ingestion Workflow

Documents are placed inside a designated data directory

An ingestion process extracts text from files

Content is converted into embeddings

Embeddings are stored in a vector database

User questions retrieve relevant chunks at query time

Once ingested, documents can be queried using natural language without referencing file names.

Supported Question Types

SQL questions on database tables

Questions based on company documents

Summaries of PDFs or reports

Information extraction from Excel sheets

Text extraction and understanding from images

General AI questions (LLM-only mode)
