from sqlalchemy import Column, Integer, String

from app.database import Base


class Bounty(Base):

    __tablename__ = "bounties"

    id = Column(Integer, primary_key=True, index=True)

    employee_name = Column(String, nullable=False)

    points = Column(Integer, default=0)

    reason = Column(String, nullable=False)