from fastapi import APIRouter

router = APIRouter()


@router.get("/slack/status")
def slack_status():

    return {
        "message": "Slack Route Active"
    }