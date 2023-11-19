from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.util import deprecations

deprecations.SILENCE_UBER_WARNING = True

engine = create_engine("sqlite:///higher_lower.db")
Base = declarative_base()


class Movies(Base):
    __tablename__: str = "movies"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    release_year: str = Column(String)
    rating: float = Column(Float)

    def __init__(self, name, release_year, rating) -> None:
        self.name: str = name
        self.release_year: str = release_year
        self.rating: float = rating


class PlayerScores(Base):
    __tablename__: str = "player_scores"
    id: int = Column(Integer, primary_key=True)
    nickname: str = Column(String)
    score: int = Column(Integer)

    def __init__(self, nickname, score) -> None:
        self.nickname: str = nickname
        self.score: int = score


Base.metadata.create_all(engine)
