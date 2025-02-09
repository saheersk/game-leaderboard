from sqlalchemy import Column, String, Integer, TIMESTAMP, Enum, func

from core.db import Base


class GameStatus(str, Enum):
    NOT_STARTED = "not_started"
    ONGOING = "ongoing"
    ENDED = "ended"


class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(GameStatus), default=GameStatus.NOT_STARTED)
    upvotes = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
