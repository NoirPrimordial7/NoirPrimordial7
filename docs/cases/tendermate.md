# TenderMate AI

**05 / Tender-readiness MVP**

Turns tender PDFs into AI-assisted analysis with private storage, user-scoped history, text extraction, and Gemini OCR fallback for scanned documents.

## Inside the system

A Next.js frontend connects to FastAPI, Supabase PostgreSQL, private Supabase Storage, and Gemini. JWT authentication, rate limits, daily upload quotas, account lockout, audit logs, and trial-credit tracking support the workflow.

**Built with:** Next.js · FastAPI · Supabase · Gemini

## Current scope

An MVP with separate Vercel and Render deployment flows. OCR and AI analysis depend on backend provider configuration.

[Source repository ↗](https://github.com/NoirPrimordial7/TenderMate-AI) · [Back to profile](../../README.md#selected-work)
