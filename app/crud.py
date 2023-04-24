from sqlalchemy.orm import Session

from app.models import video_game as vg_model
from app.schemas import video_game as vg_schema


def get_videogame(db: Session, videogame_id: int):
    return db.query(vg_model.VideoGame).first()
    # return db.query(video_game.VideoGame).filter(models.User.id == user_id).first()


def create_videogame(db: Session, game: vg_schema.VideoGameCreate):
    db_game = vg_model.VideoGame(name=game.name)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
