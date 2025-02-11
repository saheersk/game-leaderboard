from pydantic import BaseModel


class GameJoinResponse(BaseModel):
    id: str
    game_id: str
    contestant_id: int