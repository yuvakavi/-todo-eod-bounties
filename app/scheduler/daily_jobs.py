from app.slackbot.morning_dm import daily_job

from app.database import SessionLocal

from app.services.aggregation_service import (
    generate_weekly_summary
)


def send_morning_todos():

    print("\nSending Morning TODOs")

    daily_job()


def send_eod_reminder():

    print("\nEOD Reminder")

    print("Please submit your EOD report.")


def send_weekly_summary():

    print("\nGenerating Weekly Summary")

    db = SessionLocal()

    summary = generate_weekly_summary(db)

    print(summary)