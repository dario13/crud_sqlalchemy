from sqlalchemy import Column, String, Integer, Date
from models.movies_actors_association import movies_actors_association
from sqlalchemy.orm import relationship

from base import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    release_date = Column(Date)
    actors = relationship("Actor", secondary=movies_actors_association)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date