import os
import requests

from dotenv import load_dotenv

from app.database import SessionLocal
from app.models.todo_model import Todo

load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")

USER_ID = "U06T83LP86P"


def get_todos():

    db = SessionLocal()

    todos = db.query(Todo).all()

    return todos


def send_dm(message):

    url = "https://slack.com/api/chat.postMessage"

    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "channel": USER_ID,
        "text": message
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    print(response.json())


def daily_job():

    todos = get_todos()

    message = "*Today's Tasks:*\n\n"

    for todo in todos:

        message += (
            f"• {todo.task} "
            f"({todo.priority}) "
            f"- {todo.status}\n"
        )

    send_dm(message)


daily_job()