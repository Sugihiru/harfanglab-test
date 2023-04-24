import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.logger import logger
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app import crud, database
from app.schemas import video_game as vg_schema

router = APIRouter(
    prefix="/videogames",
    tags=["videogames"],
)

bearer_auth = HTTPBearer()


@router.get("", response_model=list[vg_schema.VideoGame], include_in_schema=False)
@router.get("/", response_model=list[vg_schema.VideoGame])
def get_videogames(db: Session = Depends(database.get_db)):
    return crud.get_videogames(db)


@router.get("/{videogame_id}", response_model=vg_schema.VideoGame)
def get_videogame(videogame_id: int, db: Session = Depends(database.get_db)):
    game = crud.get_videogame(db, videogame_id)
    if not game:
        raise HTTPException(status_code=404, detail="Video game not found")
    return game


@router.post("", response_model=vg_schema.VideoGame, include_in_schema=False)
@router.post("/", response_model=vg_schema.VideoGame)
def create_videogame(
    game: vg_schema.VideoGameCreate, db: Session = Depends(database.get_db)
):
    return crud.create_videogame(db, game)
