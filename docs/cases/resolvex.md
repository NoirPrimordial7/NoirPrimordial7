# CASE / 02 — ResolveX

Connects students, faculty and placement administrators through role-based ticket assignment, conversations and resolution workflows.

## Inside the system

A React interface sits above FastAPI, SQLAlchemy and PostgreSQL. JWT authentication and role checks separate customer, agent and administrator workflows. Alembic manages schema changes; Docker Compose packages the services.

**Components:** React · FastAPI · PostgreSQL · Docker

[Source repository ↗](https://github.com/NoirPrimordial7/ResolveX)
