import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")