from sqlalchemy.orm import Session

from app.models.todo_model import Todo
from app.models.eod_model import EOD
from app.models.bounty_model import Bounty


def generate_weekly_summary(db: Session):

    todos = db.query(Todo).all()

    eods = db.query(EOD).all()

    bounties = db.query(Bounty).all()

    completed_tasks = 0

    total_eods = len(eods)

    total_points = 0

    for todo in todos:

        if todo.status == "completed":

            completed_tasks += 1

    for bounty in bounties:

        total_points += bounty.points

    summary = {
        "completed_tasks": completed_tasks,
        "total_eods": total_eods,
        "total_reward_points": total_points
    }

    return summary

from app.database import SessionLocal

db = SessionLocal()

result = generate_weekly_summary(db)

print(result)