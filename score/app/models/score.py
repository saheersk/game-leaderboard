from sqlalchemy import Column, Integer, String, Float, DateTime, func

from core.db import Base


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_id = Column(String, index=True, nullable=False)
    user_id = Column(String, index=True, nullable=False)
    score = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"""<Score(game_id={self.game_id},
                user_id={self.user_id},
                score={self.score})>"""
