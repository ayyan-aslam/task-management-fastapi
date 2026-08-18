# Task Management REST API

A CRUD REST API for managing tasks, built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

## Features
- Create, read, update, delete tasks
- Mark a task as completed
- Request validation with Pydantic
- Data persisted in SQLite
- Auto-generated Swagger docs at `/docs`

## Project Structure
```
app/
├── main.py              # App entrypoint, creates tables, includes router
├── database.py           # Engine, SessionLocal, get_db dependency
├── models.py              # SQLAlchemy Task model
├── schemas.py              # Pydantic request/response schemas
├── routers/
│   └── tasks.py             # All /tasks endpoints
├── services/
│   └── task_service.py       # DB query logic (kept out of routes)
.env                            # DATABASE_URL config
requirements.txt
```

## Setup

1. Clone the repo and enter the folder:
   ```bash
   git clone <your-repo-url>
   cd task-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Open Swagger UI: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint                  | Purpose                |
|--------|----------------------------|-------------------------|
| POST   | /tasks                    | Create a new task       |
| GET    | /tasks                    | Get all tasks           |
| GET    | /tasks/{task_id}          | Get a task by ID        |
| PUT    | /tasks/{task_id}          | Update a task           |
| DELETE | /tasks/{task_id}          | Delete a task           |
| PATCH  | /tasks/{task_id}/complete | Mark a task as completed|

## Example Request

Create a task:
```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Finish assignment", "description": "FastAPI task API", "status": "pending"}'
```

Response:
```json
{
  "id": 1,
  "title": "Finish assignment",
  "description": "FastAPI task API",
  "status": "pending",
  "created_at": "2026-08-18T10:00:00"
}
```
