
from sqlalchemy.orm import Session

from app.models.eod_model import EOD

from app.ai_router.extractor import extract_blocker_info

from app.services.escalation_service import (
    escalate_issue
)

from app.services.bounty_service import (
    award_points
)


def create_eod(db: Session, data: dict):

    eod = EOD(
        employee_name=data["employee_name"],
        completed_work=data["completed_work"],
        blockers=data["blockers"]
    )

    db.add(eod)

    db.commit()

    db.refresh(eod)

    analysis = extract_blocker_info(
        data["blockers"]
    )

    print("\nAI BLOCKER ANALYSIS")

    print(analysis)

    escalate_issue(analysis)
    award_points(
    db,
    data["employee_name"],
    10,
    "EOD Submission"
)

    return eod


def get_eods(db: Session):

    return db.query(EOD).all()