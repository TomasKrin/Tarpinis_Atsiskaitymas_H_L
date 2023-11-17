from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.util import deprecations

deprecations.SILENCE_UBER_WARNING = True

engine = create_engine("sqlite:///higher_lower.db")
Base = declarative_base()


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    release_year = Column(String)
    rating = Column(Float)

    def __init__(self, name, release_year, rating):
        self.name = name
        self.release_year = release_year
        self.rating = rating


class PlayerScores(Base):
    __tablename__ = "player_scores"
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    score = Column(Integer)

    def __init__(self, nickname, score):
        self.nickname = nickname
        self.score = score


Base.metadata.create_all(engine)
