from sqlalchemy.orm import Session

from app.models.bounty_model import Bounty


def award_points(
    db: Session,
    employee_name: str,
    points: int,
    reason: str
):

    bounty = Bounty(
        employee_name=employee_name,
        points=points,
        reason=reason
    )

    db.add(bounty)

    db.commit()

    db.refresh(bounty)

    print(
        f"""
        REWARD ISSUED

        Employee: {employee_name}
        Points: {points}
        Reason: {reason}
        """
    )

    return bounty


def get_bounties(db: Session):

    return db.query(Bounty).all()