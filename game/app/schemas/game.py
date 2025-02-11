from pydantic import BaseModel

from models import GameStatus


class GameCreate(BaseModel):
    game: str
    description: str


class GameResponse(BaseModel):
    id: str
    name: str
    description: str
    status: GameStatus
    upvotes: int
