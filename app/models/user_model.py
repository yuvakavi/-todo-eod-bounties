from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    person_id = Column(String, unique=True, nullable=False)

    name = Column(String, nullable=False)

    role = Column(String, nullable=False)

    slack_id = Column(String, nullable=True)