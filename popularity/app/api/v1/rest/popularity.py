from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas.popularity import PopularityScoreResponse
from models import PopularityScore
from core.db import get_db


popularity_route = APIRouter()


@popularity_route.get("/popularity-scores",
                      response_model=List[PopularityScoreResponse])
def get_popularity_scores(db: Session = Depends(get_db)):
    return db.query(PopularityScore).all()
