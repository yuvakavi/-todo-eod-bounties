from fastapi import APIRouter

router = APIRouter()


@router.get("/bounties")
def get_bounties():

    return {
        "message": "Bounty Route Working"
    }