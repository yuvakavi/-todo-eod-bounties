from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.services.todo_service import create_todo, get_todos

router = APIRouter()


@router.post("/todos")
def add_todo(data: dict):

    db: Session = SessionLocal()

    return create_todo(db, data)


@router.get("/todos")
def list_todos():

    db: Session = SessionLocal()

    return get_todos(db)
from app.services.todo_service import update_todo_status


@router.put("/todos/{todo_id}")
def update_todo(todo_id: str, status: str):

    db: Session = SessionLocal()

    return update_todo_status(db, todo_id, status)