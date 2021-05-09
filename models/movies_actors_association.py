from sqlalchemy import Column, Integer, Table, ForeignKey
from base import Base

movies_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)
        