from sqlalchemy.orm import Session

from app.models import video_game


def get_videogame(db: Session, videogame_id: int):
    return db.query(video_game.VideoGame).first()
    # return db.query(video_game.VideoGame).filter(models.User.id == user_id).first()
