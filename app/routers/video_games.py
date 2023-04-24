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


@router.get("", include_in_schema=False)
@router.get("/")
def get_videogames():
    print("get_videogames")
    return "get_videogames"


@router.post("", response_model=vg_schema.VideoGame, include_in_schema=False)
@router.post("/", response_model=vg_schema.VideoGame)
def create_videogame(
    game: vg_schema.VideoGameCreate, db: Session = Depends(database.get_db)
):
    return crud.create_videogame(db, game)
