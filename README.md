# Leave Management System

An end-to-end DevOps project built to demonstrate the complete software delivery lifecycle—from local development to production deployment on Red Hat OpenShift.

Rather than focusing solely on application development, this project emphasizes containerization, CI/CD, infrastructure automation, deployment, and monitoring.

---

## Current Features

- Employee Management
- Leave Request Management
- PostgreSQL Database
- Alembic Database Migrations
- Dockerized FastAPI Application
- Dockerized PostgreSQL
- Environment Variable Configuration
- Persistent Database Storage

---

## Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | FastAPI |
| Database | PostgreSQL 17 |
| ORM | SQLAlchemy |
| Database Migration | Alembic |
| Templates | Jinja2 |
| Containerization | Docker |
| Orchestration | Docker Compose *(Coming Soon)* |
| CI/CD | Jenkins *(Coming Soon)* |
| Artifact Repository | JFrog Artifactory *(Coming Soon)* |
| Platform | Red Hat OpenShift *(Coming Soon)* |
| Monitoring | Prometheus & Grafana *(Coming Soon)* |

---

## Architecture
<img width="1536" height="1024" alt="ETE Diagram Leave-Management" src="https://github.com/user-attachments/assets/52414716-866c-4024-a22b-0f0dbfe8ee09" />

Browser
│
▼
FastAPI Application
│
▼
SQLAlchemy ORM
│
▼
PostgreSQL Database
│
▼
Docker Volume

---
## Project Structure
leave-management/
│
├── app/
├── alembic/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
