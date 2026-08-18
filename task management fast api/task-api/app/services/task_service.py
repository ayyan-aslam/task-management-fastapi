from sqlalchemy.orm import Session
from .. import models, schemas


def create_task(db: Session, task_data: schemas.TaskCreate) -> models.Task:
    task = models.Task(**task_data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_all_tasks(db: Session):
    return db.query(models.Task).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task(db: Session, task_id: int, task_data: schemas.TaskUpdate):
    task = get_task_by_id(db, task_id)
    if not task:
        return None
    for field, value in task_data.model_dump().items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = get_task_by_id(db, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True


def mark_task_completed(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)
    if not task:
        return None
    task.status = models.TaskStatus.completed
    db.commit()
    db.refresh(task)
    return task