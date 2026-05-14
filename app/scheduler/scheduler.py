from apscheduler.schedulers.blocking import (
    BlockingScheduler
)

from app.scheduler.daily_jobs import (
    send_morning_todos,
    send_eod_reminder,
    send_weekly_summary
)

scheduler = BlockingScheduler()

# Morning TODOs → 9:00 AM
scheduler.add_job(
    send_morning_todos,
    'cron',
    hour=9,
    minute=0
)

# EOD Reminder → 6:00 PM
scheduler.add_job(
    send_eod_reminder,
    'cron',
    hour=18,
    minute=0
)

# Weekly Summary → Friday 7 PM
scheduler.add_job(
    send_weekly_summary,
    'cron',
    day_of_week='fri',
    hour=19,
    minute=0
)

print("Scheduler Running...")

scheduler.start()