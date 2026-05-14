from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class EOD(Base):

    __tablename__ = "eod_reports"

    id = Column(Integer, primary_key=True, index=True)

    employee_name = Column(String, nullable=False)

    completed_work = Column(Text, nullable=False)

    blockers = Column(Text, nullable=True)

    status = Column(String, default="submitted")