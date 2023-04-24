import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.logger import logger
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

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
