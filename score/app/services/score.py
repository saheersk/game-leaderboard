from sqlalchemy.orm import Session, func

from models import Score


def add_score(game_id: str, user_id: str, score: float, db: Session):
    score_entry = Score(game_id=game_id, user_id=user_id, score=score)
    db.add(score_entry)
    db.commit()
    db.refresh(score_entry)
    return score_entry


def get_global_leaderboard(db: Session):
    return db.query(Score.user_id, func.sum(Score.score).label("total_score"))\
        .group_by(Score.user_id)\
        .order_by(func.sum(Score.score).desc())\
        .limit(10)\
        .all()


def get_game_leaderboard(game_id: str, db: Session):
    return db.query(Score.user_id, func.sum(Score.score).label("total_score"))\
        .filter(Score.game_id == game_id)\
        .group_by(Score.user_id)\
        .order_by(func.sum(Score.score).desc())\
        .limit(10)\
        .all()
