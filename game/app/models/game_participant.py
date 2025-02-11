from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, Integer, func

from core.db import Base


class GameParticipant(Base):
    __tablename__ = "game_participants"

    id = Column(String, primary_key=True, index=True)
    game_id = Column(String, ForeignKey("games.id", ondelete="CASCADE"))
    contestant_id = Column(Integer, ForeignKey("contestants.id",
                                               ondelete="CASCADE"))
    joined_at = Column(TIMESTAMP, default=func.now())
    exited_at = Column(TIMESTAMP, nullable=True)
