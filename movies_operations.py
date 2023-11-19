from sqlalchemy.orm import sessionmaker
from model import Movies, engine
from assets.movie_list import movies

Session = sessionmaker(bind=engine)
session = Session()


def add_all_movies() -> None:
    for name, year, rating in movies:
        session.add(Movies(name, year, rating))


def add_movie() -> None:
    pass


def edit_movie(movie_id) -> None:
    pass


session.commit()
session.close()
