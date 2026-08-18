from fastapi import FastAPI
from . import models
from .database import engine
from .routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="A simple CRUD API for managing tasks, built with FastAPI + SQLite.",
    version="1.0.0",
)

app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Task Man API is running"}