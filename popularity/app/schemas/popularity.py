from pydantic import BaseModel


class PopularityScoreResponse(BaseModel):
    id: int
    game_id: str
    score: float
    computed_at: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
