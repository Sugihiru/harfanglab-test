import datetime

from pydantic import BaseModel


class VideoGameBase(BaseModel):
    name: str
    release_date: datetime.date
    studio: str
    ratings: int


class VideoGameCreate(VideoGameBase):
    pass


class VideoGame(VideoGameBase):
    id: int

    class Config:
        orm_mode = True
