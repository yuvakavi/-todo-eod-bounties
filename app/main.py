from fastapi import FastAPI

from app.database import Base, engine

from app.models.user_model import User
from app.models.todo_model import Todo

from app.routes.todo_routes import router as todo_router


from app.models.eod_model import EOD

from app.routes.eod_routes import router as eod_router

from app.models.bounty_model import Bounty

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router)
app.include_router(eod_router)


@app.get("/")
def home():
    return {"message": "PULSE Running"}