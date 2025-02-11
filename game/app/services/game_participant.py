import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from models import GameParticipant, Game, GameStatus


def add_me(game_id: str, user_id: int, db: Session):
    game = db.get(Game, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    if game.status != GameStatus.ONGOING:
        raise HTTPException(status_code=400, detail="Game is not ongoing")

    participant = GameParticipant(id=str(uuid.uuid4()), game_id=game_id,
                                  contestant_id=user_id)
    db.add(participant)
    db.commit()
    db.refresh(participant)
    return participant


def remove_me(game_id: str, user_id: int, db: Session):
    stmt = select(GameParticipant).where(
        GameParticipant.game_id == game_id,
        GameParticipant.contestant_id == user_id)
    participant = db.execute(stmt).scalar_one_or_none()
    if not participant:
        raise HTTPException(status_code=404,
                            detail="User not found in the game")
    participant.exited_at = func.now()
    db.commit()
    return participant
