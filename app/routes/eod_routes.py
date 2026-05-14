from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.services.eod_service import (
    create_eod,
    get_eods
)

router = APIRouter()


@router.post("/eod")
def submit_eod(data: dict):

    db: Session = SessionLocal()

    return create_eod(db, data)


@router.get("/eod")
def list_eods():

    db: Session = SessionLocal()

    return get_eods(db)