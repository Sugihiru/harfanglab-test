from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class VideoGame(Base):
    __tablename__ = "videogames"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    studio: str
    ratings: int
