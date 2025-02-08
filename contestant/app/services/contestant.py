from sqlalchemy.orm import Session

from app.models.contestant import Contestant
from app.schemas.contestant import ContestantCreate


def register_contestant(db: Session, contestant: ContestantCreate):
    db_contestant = Contestant(username=contestant.username,
                               age=contestant.age)
    db.add(db_contestant)
    db.commit()
    db.refresh(db_contestant)
    return db_contestant


def fetch_contestant(db: Session, contestant_id: int):
    return db.query(Contestant).filter(Contestant.id == contestant_id).first()
