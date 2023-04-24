from sqlalchemy.orm import Session

from app.models import video_game as vg_model
from app.schemas import video_game as vg_schema


def create_videogame(db: Session, game: vg_schema.VideoGameCreate):
    db_game = vg_model.VideoGame(
        name=game.name,
        studio=game.studio,
        release_date=game.release_date,
        ratings=game.ratings,
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_videogame(db: Session, videogame_id: int):
    return (
        db.query(vg_model.VideoGame)
        .filter(vg_model.VideoGame.id == videogame_id)
        .first()
    )


def get_videogames(db: Session):
    return db.query(vg_model.VideoGame).all()


def delete_videogame(db: Session, videogame_id: int):
    obj = (
        db.query(vg_model.VideoGame)
        .filter(vg_model.VideoGame.id == videogame_id)
        .first()
    )
    db.delete(obj)
    db.commit()
