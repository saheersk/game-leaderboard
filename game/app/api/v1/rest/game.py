from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from schemas.game import GameCreate, GameResponse
from services.game import register_game, get_game, stop_game


game_router = APIRouter()


@game_router.post("/games/", response_model=GameResponse)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    return register_game(game, db)


@game_router.put("/games/{game_id}/start", response_model=GameResponse)
def start_game(game_id: str, db: Session = Depends(get_db)):
    return get_game(game_id, db)


@game_router.put("/games/{game_id}/end", response_model=GameResponse)
def end_game(game_id: str, db: Session = Depends(get_db)):
    return stop_game(game_id, db)
