import os
import requests

from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler

# 🔹 Load Environment Variables
load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# 🔹 Agent Lab Channel ID
CHANNEL_ID = "C0AUCJY0ERM"


# 🔹 Fetch Members From Agent Lab
def get_channel_members():

    url = "https://slack.com/api/conversations.members"

    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}"
    }

    params = {
        "channel": CHANNEL_ID
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    data = response.json()

    print("\nCHANNEL MEMBERS RESPONSE:")
    print(data)

    if not data.get("ok"):

        print("\nSlack API Error:")
        print(data.get("error"))

        return []

    return data.get("members", [])


# 🔹 Get User Info
def get_user_info(user_id):

    url = "https://slack.com/api/users.info"

    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}"
    }

    params = {
        "user": user_id
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    data = response.json()

    user = data.get("user", {})

    return {
        "name": user.get(
            "real_name",
            "User"
        ),
        "user_id": user_id
    }


# 🔹 Generate AI TODO
def generate_todo():

    prompt = """
Generate 3 short productivity tasks.

Only output task names.

Example:
Build FastAPI APIs
Learn Slack orchestration
Take a short walk
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    raw_todo = result.get(
        "response",
        ""
    )

    print("\nOLLAMA RESPONSE:")
    print(raw_todo)

    lines = raw_todo.split("\n")

    tasks = []

    for line in lines:

        stripped = line.strip()

        if (
            stripped
            and len(stripped) < 50
            and ":" not in stripped
        ):

            tasks.append(stripped)

    # 🔹 Fallback Tasks
    if len(tasks) < 3:

        tasks = [
            "Build FastAPI APIs",
            "Learn Slack orchestration",
            "Take a short walk"
        ]

    final_tasks = []

    for i, task in enumerate(tasks[:3], start=1):

        final_tasks.append(
            f"{i}. {task.lstrip('- ').strip()}"
        )

    return "\n".join(final_tasks)


# 🔹 Send Personal DM
def send_dm(user_id, message):

    url = "https://slack.com/api/chat.postMessage"

    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "channel": user_id,
        "text": message
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    print("\nDM RESPONSE:")
    print(response.json())


# 🔹 Main Workflow
def daily_job():

    print("\nFetching Agent Lab Members...\n")

    members = get_channel_members()

    print("\nTOTAL MEMBERS:")
    print(len(members))

    for user_id in members:

        # 🔹 Skip Slackbot
        if user_id == "USLACKBOT":
            continue

        user = get_user_info(user_id)

        print(f"\nSending TODO to {user['name']}")

        todo = generate_todo()

        final_message = f"""
Hello {user['name']} 👋

Here are your tasks for today:

{todo}

- PULSE AI Workflow Bot
"""

        print("\nFINAL MESSAGE:")
        print(final_message)

        send_dm(
            user["user_id"],
            final_message
        )


# 🔹 Run Immediately
daily_job()


# 🔹 Daily Scheduler (9 AM)
scheduler = BlockingScheduler()

scheduler.add_job(
    daily_job,
    'cron',
    hour=9,
    minute=0
)

print("\nTodoBot Running...\n")

scheduler.start()