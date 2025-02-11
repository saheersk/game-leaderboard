import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.game import GameCreate
from models import Game, GameStatus


def register_game(game: GameCreate, db: Session):
    db_game = Game(id=str(uuid.uuid4()), name=game.name,
                   description=game.description)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_game(game_id: str, db: Session):
    game = db.get(Game, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    if game.status != GameStatus.NOT_STARTED:
        raise HTTPException(status_code=400,
                            detail="Game is already started or ended")
    game.status = GameStatus.ONGOING
    db.commit()
    db.refresh(game)
    return game


def stop_game(game_id: str, db: Session):
    game = db.get(Game, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    if game.status != GameStatus.ONGOING:
        raise HTTPException(status_code=400, detail="Game is not ongoing")
    game.status = GameStatus.ENDED
    db.commit()
    db.refresh(game)
    return game
