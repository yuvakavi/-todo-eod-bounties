from app.database import SessionLocal

from app.services.aggregation_service import (
    generate_weekly_summary
)


def weekly_summary_job():

    db = SessionLocal()

    result = generate_weekly_summary(db)

    print(result)