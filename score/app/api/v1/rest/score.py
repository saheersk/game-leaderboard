from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from services.score import add_score, get_game_leaderboard, \
      get_global_leaderboard
from schemas.score import AssignResponse, GameLeaderboardResponse, \
    GlobalLeaderboardResponse

score_router = APIRouter()


@score_router.post("/games/{game_id}/scores/{user_id}",
                   response_model=AssignResponse)
def assign_score(game_id: str, user_id: str, score: float,
                 db: Session = Depends(get_db)):
    score_entry = add_score(game_id, user_id, score, db)
    return {"message": "Score assigned successfully", "score": score_entry}


@score_router.get("/leaderboard/global/",
                  response_model=GlobalLeaderboardResponse)
def global_leaderboard(db: Session = Depends(get_db)):
    leaderboard = get_global_leaderboard(db)
    return {"leaderboard": [{"user_id": user_id,
                             "total_score": total_score}
                            for user_id, total_score in leaderboard]}


@score_router.get("/leaderboard/game/{game_id}",
                  response_model=GameLeaderboardResponse)
def game_leaderboard(game_id: str, db: Session = Depends(get_db)):
    leaderboard = get_game_leaderboard(game_id, db)
    return {"game_id": game_id,
            "leaderboard": [{"user_id": user_id, "total_score": total_score}
                            for user_id, total_score in leaderboard]}
