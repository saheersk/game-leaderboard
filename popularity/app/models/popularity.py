from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, \
      TIMESTAMP, func

from core.db import Base


class PopularityScore(Base):
    __tablename__ = "popularity_scores"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(String, ForeignKey("games.id"))
    score = Column(Float, default=0.0)
    computed_at = Column(DateTime, default=func.now)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())