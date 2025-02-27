# CRUD Blog Post Application

## Objective
This web application allows users to create, read, update, and delete (CRUD) blog posts. The backend is implemented using FastAPI, and the database using PostgreSQL and SQLalchemy. The application is dockerized to ensure ease of deployment and consistency across environments.

## Features
- Create, read, update, and delete blog posts.
- Pagination for blog post listings.
- Dockerized setup for easy deployment.

## Initial Setup

### 1. Clone the Repository
```bash
git clone git@github.com:purplecui/fastapi_cru.git
cd fastapi_cru
```

### 2. Create and activate virtual environment
```bash
python -m pip install --user virtualenv
virtualenv venv

# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

```
### 3. Run docker compose
```bash
#starting application
docker compose up
 ```
