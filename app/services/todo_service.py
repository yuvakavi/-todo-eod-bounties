from sqlalchemy.orm import Session

from app.models.todo_model import Todo


def create_todo(db: Session, data: dict):

    todo = Todo(
        todo_id=data["todo_id"],
        task=data["task"],
        priority=data["priority"],
        status=data["status"],
        assigned_to=data["assigned_to"]
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def get_todos(db: Session):

    return db.query(Todo).all()
def update_todo_status(db: Session, todo_id: str, status: str):

    todo = db.query(Todo).filter(
        Todo.todo_id == todo_id
    ).first()

    if todo:

        todo.status = status

        db.commit()
        db.refresh(todo)

    return todo