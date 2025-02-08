from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.contestant import ContestantCreate, ContestantResponse
from app.services.contestant import register_contestant, fetch_contestant

router = APIRouter()


@router.post("/contestants", response_model=ContestantResponse)
def create_contestant(contestant: ContestantCreate,
                      db: Session = Depends(get_db)):
    return register_contestant(db, contestant)


@router.get("/contestants/{contestant_id}", response_model=ContestantResponse)
def get_contestant(contestant_id: int, db: Session = Depends(get_db)):
    return fetch_contestant(db, contestant_id)
