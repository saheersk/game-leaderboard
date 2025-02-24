from sqlalchemy import Column, Integer, String, func, TIMESTAMP

from app.core.db import Base


class Contestant(Base):
    __tablename__ = "contestants"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    created_at = Column(TIMESTAMP, default=func.now())