from pydantic import BaseModel


class Score(BaseModel):
    id: str
    game_id: str
    user_id: str
    score: float


class AssignResponse(BaseModel):
    message: str
    score: Score


class Leaderboard(BaseModel):
    user_id: str
    total_score: float


class GlobalLeaderboardResponse(BaseModel):
    leaderboard: Leaderboard


class GameLeaderboardResponse(BaseModel):
    Leaderboard: Leaderboard
