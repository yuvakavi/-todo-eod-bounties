from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)

    todo_id = Column(String, unique=True, nullable=False)

    task = Column(Text, nullable=False)

    priority = Column(String, nullable=False)

    status = Column(String, default="pending")

    assigned_to = Column(String, nullable=False)