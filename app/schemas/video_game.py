import datetime

from pydantic import BaseModel, Field


class VideoGameBase(BaseModel):
    name: str = Field(..., min_length=1)
    release_date: datetime.date
    studio: str = Field(..., min_length=1)
    ratings: int = Field(..., gt=0)


class VideoGameCreate(VideoGameBase):
    pass


class VideoGame(VideoGameBase):
    id: int

    class Config:
        orm_mode = True
