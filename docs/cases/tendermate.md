# CASE / 01 — TenderMate AI

Turns tender PDFs into structured analysis, with authenticated workspaces, private storage, quotas and audit logging.

## Inside the system

The browser talks to a FastAPI service for PDF extraction and Gemini analysis. Supabase provides PostgreSQL and private document storage; authorization, account limits and audit events stay on the server.

**Components:** Next.js · FastAPI · Supabase · Gemini

[Source repository ↗](https://github.com/NoirPrimordial7/TenderMate-AI)
