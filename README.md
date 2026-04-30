# Data Pipeline Project

## Overview
This project implements a data pipeline with 3 services:

- Flask API (Mock Server) → Provides customer data
- FastAPI Pipeline → Ingests data
- PostgreSQL → Stores data

Flow:
Flask → FastAPI → PostgreSQL → API Response

---

## Setup Instructions

Run the following command:

docker-compose up --build

---

## Services

- Flask API: http://localhost:5000
- FastAPI: http://localhost:8000

---

## API Endpoints

### Flask

- GET /api/customers?page=1&limit=5  
- GET /api/customers/{id}  
- GET /api/health  

---

### FastAPI

- POST /api/ingest  
- GET /api/customers?page=1&limit=5  
- GET /api/customers/{id}  

---

## Testing

### Fetch mock data
curl http://localhost:5000/api/customers?page=1&limit=5

### Ingest data
curl -X POST http://localhost:8000/api/ingest

### Fetch stored data
curl http://localhost:8000/api/customers?page=1&limit=5

---

## Tech Stack

- Python
- Flask
- FastAPI
- PostgreSQL
- Docker
- SQLAlchemy
