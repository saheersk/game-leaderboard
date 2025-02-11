from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from schemas.game_participant import GameJoinResponse
from services.game_participant import add_me, remove_me


game_participant_router = APIRouter()


@game_participant_router.post("/games/{game_id}/join/{user_id}",
                              response_model=GameJoinResponse)
def join_game(game_id: str, user_id: str, db: Session = Depends(get_db)):
    return add_me(game_id, user_id, db)


@game_participant_router.post("/games/{game_id}/exit/{user_id}",
                              response_model=GameJoinResponse)
def exit_game(game_id: str, user_id: str, db: Session = Depends(get_db)):
    return remove_me(game_id, user_id, db)