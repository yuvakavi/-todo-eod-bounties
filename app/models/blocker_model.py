from sqlalchemy import Column, Integer, String

from app.database import Base


class Blocker(Base):

    __tablename__ = "blockers"

    id = Column(Integer, primary_key=True)

    blocker = Column(String)

    severity = Column(String)

    owner = Column(String)