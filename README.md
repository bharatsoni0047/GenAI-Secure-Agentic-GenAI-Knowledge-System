# AgenticRAG – Secure Enterprise Multi-Modal AI Assistant

## Project Title
**AgenticRAG**  
(GenAI-Secure-Agentic-GenAI-Knowledge-System)

A secure, agent-based Generative AI system that lets non-technical users ask natural language questions to get answers from both your company database **and** all your documents — without writing any SQL or searching files manually.

## Description
AgenticRAG is an enterprise-ready AI assistant that combines:

- **Natural Language to SQL** → Ask business questions in plain English, get accurate answers from your MySQL database  
- **Multi-Modal RAG** → Ask questions about PDFs (policies, reports), Excel sheets (financials, KPIs), scanned images (invoices, forms), and text files — the system understands and retrieves relevant content automatically  
- **Agentic Architecture** → Smart agents decide whether the question needs database access, document search, or general reasoning  
- **Secure Access** → Protected by JWT authentication so only authorized people can ask questions  

You talk to it like a very smart colleague who already read all your documents and has full access to the company database.

## Tech Stack (High-Level)
- Backend: FastAPI  
- User Interface: Streamlit (simple chat-like experience)  
- Agents & Logic: Agentic workflow (router + SQL agent + RAG agent + safety checks)  
- Database: MySQL (easy to connect your own)  
- Document Understanding: PDF, Excel, OCR (for images/scanned docs), vector embeddings  
- Authentication: JWT tokens  
- Designed to be modular and configurable via environment settings  

## How It Gives Value to Your Organization

| Value Delivered                              | Real-World Benefit                                                                 |
|----------------------------------------------|-------------------------------------------------------------------------------------|
| Non-technical users get fast answers         | Managers, HR, finance, sales teams no longer wait for analysts or IT               |
| Single place for database + documents        | No more switching between Excel, PDFs, shared drives, and BI tools                 |
| Reduces dependency on developers/analysts    | Ad-hoc questions answered in seconds instead of hours/days                         |
| Safer data access                            | Controlled via login — no direct database or file access given to end users        |
| Handles multi-modal content                  | Can read scanned invoices, whiteboards, handwritten notes, charts in PDFs         |
| Audit-friendly & explainable                 | Shows reasoning, generated SQL (if enabled), and document sources                  |
| Scales to enterprise needs                   | JWT + modular agents → easy to add roles, more databases, conversation memory     |

In short:  
It turns your scattered company knowledge (database + documents) into one natural-language interface that anyone in the organization can use securely and productively.

## Usages – What People Actually Ask It

**Database / Business Analytics Questions**  
- Who are our top 10 highest-paid employees this year?  
- What is average salary by department in last 12 months?  
- Show total sales per product category for Q1–Q3  
- Compare revenue this year vs last year same period  

**Document & Policy Questions**  
- What is our current remote work policy?  
- Summarize the key points from the latest board report  
- What are the rules for maternity leave?  
- Explain our leave encashment policy in simple words  

**Excel & Financial Data Questions**  
- What was total marketing spend in FY 2024–25?  
- Show me travel expenses breakdown for last quarter  
- How many new clients did we onboard in 2025?  

**Scanned / Image-Based Questions**  
- How much GST is charged on this invoice?  
- What is the due date on this scanned bill?  
- Extract vendor name and amount from this receipt image  

**Mixed / Smart Questions**  
- Which departments have average salary above 8 lakhs? And what does HR policy say about salary bands?  
- Summarize Q3 performance and compare revenue numbers with last year  

Just type normal questions — the system automatically decides whether to look in the database, search documents, or combine both.

Perfect for:  
Finance teams • HR • Operations • Management • Anyone tired of digging through files and asking IT for reports.

Secure. Fast. Useful. Every day.
